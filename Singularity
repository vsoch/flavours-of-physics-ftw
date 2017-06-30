Bootstrap: docker
From: ubuntu:16.04

%setup
wget https://storage.googleapis.com/containers-ftw/flavours-of-physics-ftw/check_agreement.csv.zip -P data/input/
wget https://storage.googleapis.com/containers-ftw/flavours-of-physics-ftw/check_correlation.csv.zip -P data/input/
wget https://storage.googleapis.com/containers-ftw/flavours-of-physics-ftw/sample_submission.csv.zip -P data/input/
wget https://storage.googleapis.com/containers-ftw/flavours-of-physics-ftw/test.csv.zip -P data/input/
wget https://storage.googleapis.com/containers-ftw/flavours-of-physics-ftw/training.csv.zip -P data/input/

unzip data/input/check_agreement.csv.zip
unzip data/input/check_correlation.csv.zip
unzip data/input/sample_submission.csv.zip
unzip data/input/test.csv.zip
unzip data/input/training.csv.zip

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

%post
     
     # Data directories
     mkdir -p /data/input   # data included with container
     mkdir -p /data/work    # working directory
     mkdir -p /data/mnt     # mounted datasets

     # Result directories
     mkdir -p /result/analysis
     mkdir -p /result/web
     mkdir -p /result/pub

     # Working code directories
     mkdir -p /code/analysis
     mkdir -p /code/helpers
     mkdir -p /code/tests

     # Download evaluation functions

     apt-get update && apt-get install -y python git vim nginx
     wget https://bootstrap.pypa.io/get-pip.py
     python get-pip.py && rm get-pip.py
     pip install -y numpy scipy pandas scikit-learn ipython
     
     #########################################################
     # Install additional software / libraries here
     #########################################################


     #########################################################

     apt-get autoremove -y
     apt-get clean
