#!/bin/bash
#
# Copyright (C) 2017 Pelagicore AB
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0# Copyright (C) 2017 Pelagicore AB
#

SDK_SELF_EXTRACTOR=$1
PELUX_SDK_DESTINATION="/opt/pelux_sdk"

# Because we copy the self-extracting-installer from /vagrant/ to
# /opt/pelux_sdk and we changed that its not directly in /vagrant/
# but instead /vagrant/test/stubs/name_sdk.sh, we only need the
# name of the installer, not the path, therefor the basename.
PATH_TO_SDK_SELF_EXTRACTOR="${PELUX_SDK_DESTINATION}/`basename ${SDK_SELF_EXTRACTOR}`"

# Copy sdk file to pelux sdk destination
mkdir -p ${PELUX_SDK_DESTINATION}
cp -r /vagrant/${SDK_SELF_EXTRACTOR} ${PELUX_SDK_DESTINATION}

# Unpack the sdk
chmod +x ${PATH_TO_SDK_SELF_EXTRACTOR}
printf "${PELUX_SDK_DESTINATION}\nY\n" | ${PATH_TO_SDK_SELF_EXTRACTOR}

# Remove the self extractor
rm ${PATH_TO_SDK_SELF_EXTRACTOR} -f
