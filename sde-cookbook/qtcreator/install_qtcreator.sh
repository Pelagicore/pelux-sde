#!/usr/bin/env bash

#
# Copyright (C) 2017 Pelagicore AB
# Copyright (C) 2018 Luxoft Sweden AB
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0
#

QT_INSTALL_DIR=$1

if [ "${QT_INSTALL_DIR}" = "" ]; then
    echo "Missing first argument qt-install-dir (absolute path)"
    exit 1
fi

# Create a scriptfile that allows qt-creator to install withouth UI
SCRIPT_FILE=$(mktemp "/tmp/qt-creator-installer-script-XXXXXX.qs")
echo "
// THIS FILE IS GENERATED DO NOT CHANGE

function Controller() {
    installer.autoRejectMessageBoxes();
    installer.installationFinished.connect(function() {
        gui.clickButton(buttons.NextButton);
    })
}

Controller.prototype.WelcomePageCallback = function() {
    gui.clickButton(buttons.NextButton, 3000);
}

Controller.prototype.CredentialsPageCallback = function() {
    gui.clickButton(buttons.NextButton);
}

Controller.prototype.IntroductionPageCallback = function() {
    gui.clickButton(buttons.NextButton);
}

Controller.prototype.TargetDirectoryPageCallback = function()
{
    gui.currentPageWidget().TargetDirectoryLineEdit.setText(\"${QT_INSTALL_DIR}\");
    gui.clickButton(buttons.NextButton);
}

Controller.prototype.ComponentSelectionPageCallback = function() {
    var widget = gui.currentPageWidget();
    gui.clickButton(buttons.NextButton);
}

Controller.prototype.LicenseAgreementPageCallback = function() {
    gui.currentPageWidget().AcceptLicenseRadioButton.setChecked(true);
    gui.clickButton(buttons.NextButton);
}

Controller.prototype.StartMenuDirectoryPageCallback = function() {
    gui.clickButton(buttons.NextButton);
}

Controller.prototype.ReadyForInstallationPageCallback = function()
{
    gui.clickButton(buttons.NextButton);
}

Controller.prototype.FinishedPageCallback = function() {
var checkBoxForm = gui.currentPageWidget().LaunchQtCreatorCheckBoxForm
if (checkBoxForm && checkBoxForm.launchQtCreatorCheckBox) {
    checkBoxForm.launchQtCreatorCheckBox.checked = false;
}
    gui.clickButton(buttons.FinishButton);
}

" > $SCRIPT_FILE

set -e

# Download qt-creator-installer
QT_INSTALLER=$(mktemp --dry-run "/tmp/qt-creator-installer-XXXXXXXX.run")
wget -O ${QT_INSTALLER} http://download.qt.io/official_releases/qtcreator/4.10/4.10.0/qt-creator-opensource-linux-x86_64-4.10.0.run

chmod +x ${QT_INSTALLER}
${QT_INSTALLER} --script "${SCRIPT_FILE}" --platform minimal

# Clean up
rm ${SCRIPT_FILE}
rm ${QT_INSTALLER}
