#!/usr/bin/env bash
#
# Copyright (C) Luxoft 2018
#
# All rights reserved
#

DLT_VIEWER_TMP_DIR=/tmp/github

DLT_REPO_NAME="dlt-viewer"

mkdir -p ${DLT_VIEWER_TMP_DIR}
cd ${DLT_VIEWER_TMP_DIR}
git clone https://github.com/GENIVI/${DLT_REPO_NAME}
cd ${DLT_REPO_NAME}
mkdir build
cd build
if ! type "qmake" > /dev/null; then
	echo "Missing qmake-qt5 installation : dlt-viewer not installed"
	exit 1
fi
qmake ../BuildDltViewer.pro
make
sudo make install
sudo ldconfig
sudo rm -r ${DLT_VIEWER_TMP_DIR}
