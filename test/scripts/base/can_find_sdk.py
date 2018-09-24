#!/usr/bin/env python3
#
# Copyright (C) 2017 Pelagicore AB
# Copyright (C) 2018 Luoxft Sweden AB
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0
#

import os

PATH_TO_SDK_IN_VM = "/opt/pelux_sdk"

if not os.path.isdir(PATH_TO_SDK_IN_VM):
    exit(1)

# check sdk not empty
files_in_sdk_directory = os.listdir(PATH_TO_SDK_IN_VM)
print(files_in_sdk_directory)
if not files_in_sdk_directory:  # (seq is false if empty)
    exit(1)
