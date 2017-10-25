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
PATH_TO_SDK_SELF_EXTRACTOR="${PELUX_SDK_DESTINATION}/${SDK_SELF_EXTRACTOR}"

# Copy sdk file to pelux sdk destination
mkdir -p ${PELUX_SDK_DESTINATION}
cp -r /vagrant/${SDK_SELF_EXTRACTOR} ${PELUX_SDK_DESTINATION}

# Unpack the sdk
printf "${PELUX_SDK_DESTINATION}\nY\n" | ${PATH_TO_SDK_SELF_EXTRACTOR}

# Remove the self extractor
rm ${PATH_TO_SDK_SELF_EXTRACTOR} -f
