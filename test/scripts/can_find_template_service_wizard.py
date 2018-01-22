#!/usr/bin/env python3
#
# Copyright (C) 2017 Pelagicore AB
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# SPDX-License-Identifier: MPL-2.0
#

import os


def find_template(template_name, qtcreator_install_dir):
    template_path = "{}/share/qtcreator/templates/wizards/".format(qtcreator_install_dir)
    return template_name in os.listdir(template_path)



if __name__ == "__main__":
    template_name = "template-service-wizard"
    if not find_template(template_name, "/opt/qtcreator"):
        raise Exception("Could not find template")
