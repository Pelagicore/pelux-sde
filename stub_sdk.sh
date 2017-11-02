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

echo " \
export SDKTARGETSYSROOT=/opt/pelux_sdk/sysroots/aarch64-gnu-linux \
export CCACHE_PATH=/opt/pelux_sdk/sysroots/i686-oesdk-linux/usr/bin:/opt/pelux_sdk/sysroots/i686-oesdk-linux/usr/bin/../i686-oesdk-linux/bin:/opt/pelux_sdk/sysroots/i686-oesdk-linux/usr/bin/aarch64-gnu-     linux:/opt/pelux_sdk/sysroots/i686-oesdk-linux/usr/bin/true:/opt/pelux_sdk/sysroots/i686-oesdk-linux/usr/bin/true:$CCACHE_PATH \
export PKG_CONFIG_SYSROOT_DIR=$SDKTARGETSYSROOT \
export PKG_CONFIG_PATH=$SDKTARGETSYSROOT/usr/lib/pkgconfig \
export CONFIG_SITE=/opt/pelux_sdk/site-config-aarch64-gnu-linux \
export OECORE_NATIVE_SYSROOT=\"/opt/pelux_sdk/sysroots/i686-oesdk-linux\" \
export OECORE_TARGET_SYSROOT=\"$SDKTARGETSYSROOT\" \
export OECORE_ACLOCAL_OPTS=\"-I /opt/pelux_sdk/sysroots/i686-oesdk-linux/usr/share/aclocal\" \
unset command_not_found_handle \
export CC=true \
export CXX=true \
export CPP=true \
export AS=true \
export LD=true \
export GDB=true \
export STRIP=true \
export RANLIB=true \
export OBJCOPY=true \
export OBJDUMP=true \
export AR=true \
export NM=true \
export M4=m4 \
export TARGET_PREFIX=true \
export QMAKESPEC=stub
export CONFIGURE_FLAGS=\"--target=aarch64-gnu-linux --host=aarch64-gnu-linux --build=i686-linux --with-libtool-sysroot=$SDKTARGETSYSROOT\" \
export CFLAGS=\" -O2 -pipe -g -feliminate-unused-debug-types \" \
export CXXFLAGS=\" -O2 -pipe -g -feliminate-unused-debug-types \" \
export LDFLAGS=\"-Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed\" \
export CPPFLAGS=\"\" \
export KCFLAGS=\"--sysroot=$SDKTARGETSYSROOT\" \
export OECORE_DISTRO_VERSION=\"11.0.0\" \
export OECORE_SDK_VERSION=\"nodistro.0\" \
export ARCH=arm64 \
export CROSS_COMPILE=true \
" > ${SDK_PATH}/environment-setup-stub

touch ${SDK_PATH}/sysroot-stub
