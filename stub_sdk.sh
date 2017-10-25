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

echo "Running stubbed sdk-self-extractor"

SDK_PATH=`dirname $0`

touch ${SDK_PATH}/environment-setup-stub.sh
touch ${SDK_PATH}/sysroot-stub
