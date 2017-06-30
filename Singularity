Bootstrap: docker
From: ubuntu:16.04

%files
-R analysis/* /code/analysis
-R data/input/* /data/input

%labels
CONTAINERSFTW_TEMPLATE ubuntu16.04-python2
CONTAINERSFTW_COMPETITION_HOST containersftw
CONTAINERSFTW_COMPETITION_NAME 

%environment
CONTAINERSFTW_DATA=/data/input
CONTAINERSFTW_RESULT=/code/analysis/results/submission
CONTAINERSFTW_WORK=/code/analysis
export CONTAINERSFTW_DATA
export CONTAINERSFTW_RESULT
export CONTAINERSFTW_WORK

%runscript

     # This will generate the scientific result!
     /usr/bin/python /code/analysis/main.py


%setup

     # Data directories
     mkdir -p $SINGULARITY_ROOTFS/data/input   # data included with container
     mkdir -p $SINGULARITY_ROOTFS/data/work    # working directory
     mkdir -p $SINGULARITY_ROOTFS/data/mnt     # mounted datasets

     # Result directories
     mkdir -p $SINGULARITY_ROOTFS/code/results/submission
     mkdir -p $SINGULARITY_ROOTFS/code/results/web
     mkdir -p $SINGULARITY_ROOTFS/code/results/pub

     # Working code directories
     mkdir -p $SINGULARITY_ROOTFS/code/analysis
     mkdir -p $SINGULARITY_ROOTFS/code/tests

     /bin/bash functions/download_data.sh

%post
     
     # Download evaluation functions

     apt-get update && apt-get install -y python git vim nginx wget
     wget https://bootstrap.pypa.io/get-pip.py
     python get-pip.py && rm get-pip.py
     pip install numpy scipy pandas scikit-learn ipython
     
     #########################################################
     # Install additional software / libraries here
     #########################################################


     #########################################################

     apt-get autoremove -y
     apt-get clean
