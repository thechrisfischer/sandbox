#!/bin/bash

cd /etc/yum.repos.d/
wget http://dev.centos.org/~tru/devtools/devtools.repo
yum install -y devtoolset-1.0-gcc m4 openssl-devel db4-devel boost-devel git jansson jansson-devel gcc automake libcurl-devel
source /opt/centos/devtoolset-1.0/enable
mkdir -p /opt/src
cd /opt/src/
git clone https://github.com/ig0tik3d/darkcoin-cpuminer-1.2.git
cd darkcoin-cpuminer-1.2
bash autogen.sh
make clean 
./configure CFLAGS="-O3 -msse2"
make 
mkdir -p /opt/cpuminer/bin
cp -va /opt/src/darkcoin-cpuminer-1.2/minerd /opt/cpuminer/bin/minerd

# mine with 
#/opt/cpuminer/bin/minerd -a X11 -o stratum+tcp://x11.ltcrabbit.com:3332 -u flatlandfool.rig2x11 -p rigs
