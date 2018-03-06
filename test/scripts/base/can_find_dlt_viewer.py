#!/usr/bin/env python3
#
# Copyright (C) 2018 Luxoft
# All rights reserved
#

import os


def find_service(service_name, install_dir):
    service_path = format(install_dir)
    return service_name in os.listdir(service_path)


if __name__ == "__main__":
    service_name = "dlt_viewer"
    if not find_service(service_name, "/usr/bin"):
        raise Exception("Could not find dlt_viewer installed")
