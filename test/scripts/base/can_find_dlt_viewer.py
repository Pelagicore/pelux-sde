
#
# Copyright (C) 2018 Luxoft
#
# SPDX-License-Identifier: MPL-2.0
#

import os


def find_service(service_name, install_dir):
    service_path = format(install_dir)
    return service_name in os.listdir(service_path)


if __name__ == "__main__":
    SERVICE_NAME = "dlt_viewer"
    if not find_service(SERVICE_NAME, "/usr/bin"):
        raise Exception("Could not find " + SERVICE_NAME + " installed")
