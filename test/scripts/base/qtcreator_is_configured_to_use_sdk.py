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

def find_term_in_file(search_term, filename):
    with open(filename) as f:
        content_of_file = f.readlines()
    content_of_file = "\n".join(content_of_file)
    return search_term in content_of_file


term = "PELUX-SDK"
assert find_term_in_file(term, "/opt/qtcreator/share/qtcreator/QtProject/qtcreator/profiles.xml")
assert find_term_in_file(term, "/opt/qtcreator/share/qtcreator/QtProject/qtcreator/toolchains.xml")
