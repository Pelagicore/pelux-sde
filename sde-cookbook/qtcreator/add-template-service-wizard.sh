#!/usr/bin/env bash
#
# Copyright (C) 2017 Pelagicore AB
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0
#

WIZARD_REPO_NAME="template-service-wizard"
WIZARD_REPO_REVISION="c998e37203b663b352c2acd06c2255fd50a85ca1"

QTCREATOR_PATH="$1"
if [ "${QTCREATOR_PATH}" = "" ]; then
    echo "Missing first argument qtcreator-install-dir (absolute path)"
    exit 1
fi

TEMPLATES_PATH="${QTCREATOR_PATH}/share/qtcreator/templates/wizards"

mkdir -p ${TEMPLATES_PATH}
cd ${TEMPLATES_PATH}
git clone https://github.com/pelagicore/${WIZARD_REPO_NAME}
cd ${WIZARD_REPO_NAME}
git checkout ${WIZARD_REPO_REVISION}
