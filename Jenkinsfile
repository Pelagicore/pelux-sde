#!/usr/bin/groovy

/*
 *  Copyright (C) 2017 Pelagicore AB
 * 
 *  This Source Code Form is subject to the terms of the Mozilla Public
 *  License, v. 2.0. If a copy of the MPL was not distributed with this
 *  file, You can obtain one at http://mozilla.org/MPL/2.0/.
 * 
 *  SPDX-License-Identifier: MPL-2.0# Copyright (C) 2017 Pelagicore AB
 */


node ("PyTest") {
    stage("Checkout") {
        checkout scm
        sh 'git submodule update --init'
    }

    stage("Run tests") {
        sh "test/run-tests.sh"
    }
}
