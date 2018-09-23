#!/usr/bin/env bash
#
# Copyright (C) 2018 Luxoft Sweden AB
#
# SPDX-License-Identifier: MPL-2.0
#

DLT_VIEWER_TMP_DIR=/tmp/github

DLT_REPO_NAME="dlt-viewer"
DLT_REPO_REVISION="4549ac888b7d66526bcde0145f3fb6280f626261"

mkdir -p ${DLT_VIEWER_TMP_DIR}
cd ${DLT_VIEWER_TMP_DIR}
git clone https://github.com/GENIVI/${DLT_REPO_NAME}
cd ${DLT_REPO_NAME}
git checkout ${DLT_REPO_REVISION}
mkdir build
cd build
if ! type "qmake" > /dev/null; then
	echo "Missing qmake-qt5 installation : dlt-viewer not installed"
	exit 1
fi
qmake ../BuildDltViewer.pro
make -j $1
sudo make install
sudo ldconfig
sudo rm -r ${DLT_VIEWER_TMP_DIR}
