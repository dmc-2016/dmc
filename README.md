# DMC 2016 Virtual Machine

This Vagrant setup automates the installation of a full Machine Learning software stack running on Ubuntu 14.04.

What's in the box:
* [Keras](http://keras.io/) - minimalist, highly modular neural networks (NN) library.
* [Theano](http://deeplearning.net/software/theano/) - library to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently.
* [Tensorflow](https://www.tensorflow.org/versions/r0.7/api_docs/index.html) - library for numerical computation using data flow graphs.
* [Scikit-learn](http://scikit-learn.org/) - a basic library for many ML algorithms beyond NN.
* [Jupyter](http://jupyter.readthedocs.org/en/latest/index.html) - web application to create, share documents that contain live code, equations, visualizations and explanatory text.

![Keras](http://imgur.com/nE0of8d.jpg "Keras")
![Theano](http://i.imgur.com/Bb5SHxW.png "Theano")
![TensorFlow](http://imgur.com/rwISEz5.jpg "TensorFlow")
![Jupyter](http://i.imgur.com/zpzIAml.jpg "Jupyter")
![Scikit-learn](http://i.imgur.com/EmaCyZO.png "Scikit-learn")

# What is this for?

Going through the following process will set up a virtual Linux environment on your computer, and use Vagrant to automatically set it up with all the tools we will use in class. The goal of this process is to create an easily reproduceable programming environment which gives everyone in the class the exact same setup regardless of what computer they are using.

This is preferrable for several reasons:

* In this class, we will not be using traditional software packages which can be easily installed for different operating systems (OS). Most of our work will be based in Python, which is a lower-level programming language which has different installation procedures and might function differently under different OS. We will also rely on a number of different libraries and packages that run on top of Python. Each of these packages also has a different installation process that varies by OS. Some have a number of dependencies and some have to be built from source code, which can be a very challenging and frustrating process, depending on your experience with computer programming and the machine you are working on.  By automating the installation process this setup takes most of the difficulty out of this setup.

* Most of us do not use Linux on our computers. However, Linux is a great platform for computer programming. Most of the packages we will be using are easier to install and perform better on Linux. Because MacOSX is based on the same UNIX architecture as Linux it tends to be pretty good as well, with some caveats. Windows can be much more difficult to work with, and some of the packages we will use do not support it. This setup gives you the best of both worlds: a virtual Linux machine custom-made for this class which runs alongside your current setup.

This process has been tested to work identically regardless of which version of Windows or OSX you are using. As long as you can install VirtualBox and Vagrant and have a connection to the internet everything should just work. This ensures that the process of installing all the packages is as easy as possible and that everyone will have the same exact setup and will be using the same exact versions of all the software. This means we can to spend less time troubleshooting everyone's individual setup!!
 
There are, however, some limitations:

* While it should be sufficient for all of the examples done in class, the virtual machine (VM) will not be as efficient or high-performing as an embedded solution.
* The VM cannot support GPU for accelerated computing, even if you have one installed in your machine.
* The VM is provisioned with limited RAM and hard disk memory, so might not be able to handle larger machine learning tasks.

For these reasons, you may eventually consider an embedded solution working directly within OSX or Windows, or even create a separate partition on your machine to work directly in Linux. This might be beneficial or even necessary as you start to work on bigger problems for your research project. However, you should start wtih this setup first, at least until you get familiar with the example problems and all the different packages. Also, given the number of people in the class, *any custom setup will be done with your own effort and at your own risk, and I will not be able to troubleshoot any individual installation issues, apart from what is covered here*.

With that out of the way, let's begin...

# Installation

You must install VirtubalBox and Vagrant before continuing:

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

At the top of the page under "VirtualBox platform packages" download the installation file according to your operating system (Windows or OSX) and go through the installation process.

* [Vagrant](https://www.vagrantup.com/downloads.html)

Select your operating system to download the installation file, then go through the installation process.

### Cloning the repository

sdfsdf


### Setting up the VM

Once Vagrant and VirtualBox are installed, clone this repository or import `Vagrantfile` and `bootstrap.sh` in a directory.

From this directory, let's start your Vagrant box by typing in your terminal (it might take some time to download the Ubuntu image):

    $ vagrant up
Once the setup is complete, just run:
    
    $ vagrant ssh
You are in! Now, let's train your first recurrent neuronal network:

    $ python keras/examples/addition_rnn.py

If you can see that, it means that you setup is working and that you are training your recurrent neuronnal network to perform addition!
![addition_rnn-screenshot](http://i.imgur.com/u06tE6B.png)

To go through the code step by step, type:

    $ jupyter notebook --no-browser --ip=0.0.0.0 --FileContentsManager.root_dir=/home/vagrant/keras/examples/

Open a browser and browse http://127.0.0.1:8888

# Tips and tricks

To access files present on your computer from your Vagrant/Ubuntu machine, go to the `/vagrant` directory which is mounted to the directory you started you Vagrant box from:

    $ cd /vagrant/

To get a list of available vagrant commands (from your host computer), just type:

    $ vagrant

If you want to start your virtual machine from scratch, disconnect from it and from your host computer run:

    $ vagrant destroy
    $ vagrant up
