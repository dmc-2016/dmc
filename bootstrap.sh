#!/bin/bash

##################################
#       DMC Virtual Machine      #
#       by Danil Nagy            #
##################################

function install {
    echo installing "$1"
    shift
    apt-get -y install "$@" >/dev/null 2>&1
}

function pip_install {
    echo installing "$1"
    shift
    pip install "$@" >/dev/null 2>&1
}

function conda_install {
    echo installing "$1"
    shift
    conda install -y "$@" #>/dev/null 2>&1
}

echo "updating package information"
apt-get -y update >/dev/null 2>&1

echo "downloading anaconda"
wget --progress=bar:force https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O /home/vagrant/anaconda.sh

echo "installing anaconda"
bash /home/vagrant/anaconda.sh -b -p /home/vagrant/anaconda2 #install anaconda
rm /home/vagrant/anaconda.sh #delete downloaded installation file
echo "source /vagrant/export.sh" >> /home/vagrant/.bashrc #set anaconda as default python
export PATH="/home/vagrant/anaconda2/bin:$PATH"

conda_install "pil" pil
conda_install "seaborn" seaborn
conda_install "scikit-learn" scikit-learn
conda_install "jupyter" jupyter

# Theano
install 'g++' g++ 
conda_install "pydot" pydot-ng
pip_install 'theano' theano

# Keras
conda_install "h5py" h5py
pip_install 'keras' keras
mkdir /home/vagrant/keras
git clone https://github.com/fchollet/keras /home/vagrant/keras/ >/dev/null 2>&1

# Tensorflow
echo "installing tensorflow"
conda install -c conda-forge -y tensorflow >/dev/null 2>&1

# Miscellaneous
# install 'hdf5' libhdf5-7

echo 'All set!'