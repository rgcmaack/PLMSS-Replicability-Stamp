#! /bin/bash

export CMAKE_BUILD_TYPE=MinSizeRel \
 CMAKE_GENERATOR=Ninja

# bring in additional apt sources
apt-get update && apt-get install --no-install-recommends -yqq ca-certificates && echo "deb [trusted=yes] https://apt.kitware.com/ubuntu/ focal main" > /etc/apt/sources.list.d/kitware.list && apt-get update

# install base development env
apt-get install --no-install-recommends -yqq \
    build-essential \
    ninja-build \
    cmake \
    dlocate \
    file \
    curl

# --------------------------------------------------------------------------

cp install-helper /usr/bin

cp pkg/ispc.sh /tmp
install-helper /tmp/ispc.sh

cp pkg/tbb.sh /tmp
install-helper /tmp/tbb.sh

cp pkg/embree.sh /tmp
install-helper /tmp/embree.sh

cp pkg/rkcommon.sh /tmp
install-helper /tmp/rkcommon.sh

cp pkg/openimagedenoise.sh /tmp
install-helper /tmp/openimagedenoise.sh

cp pkg/openvkl.sh /tmp
install-helper /tmp/openvkl.sh

cp pkg/ospray.sh /tmp
install-helper /tmp/ospray.sh

# install OSMesa
cp pkg/mesa.sh /tmp
install-helper /tmp/mesa.sh

# install ZFP
cp pkg/zfp.sh /tmp
install-helper /tmp/zfp.sh

# install Spectra
cp pkg/spectra.sh /tmp
install-helper /tmp/spectra.sh

# install ParaView
paraview=5.10.1
export PARAVIEW_VERSION=${paraview}

cp pkg/paraview.sh /tmp
install-helper /tmp/paraview.sh

# --------------------------------------------------------------------------

# install TTK
ttk=dev
export TTK_VERSION=${ttk}

export DEV=""

cp pkg/ttk.sh /tmp
install-helper /tmp/ttk.sh

# --------------------------------------------------------------------------

apt-get update && apt-get -yqq --no-install-recommends install $(cat /usr/local/.pkgs) gdb && apt-get clean && rm -rf /var/cache/apt/lists

export DEV="True"

cp pkg/ttk.sh /tmp
install-helper /tmp/ttk.sh
  
# --------------------------------------------------------------------------

cp --from=builder-ttk /usr/local /usr/local

apt-get update && apt-get -yqq --no-install-recommends install $(cat /usr/local/.pkgs) && apt-get clean && rm -rf /var/cache/apt/lists

# add current path to output result
cp noisyTerrain.vtu /home
cp noisyTerrainMSS.py /home

# run pvpython to generate examplle image
pvpython /home/noisyTerrainMSS.py

