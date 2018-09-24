#!/usr/bin/env python3
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

import os

UNAME_VERSION_STRING = os.uname().version
if "ubuntu" not in UNAME_VERSION_STRING.lower():
    exit(1)
