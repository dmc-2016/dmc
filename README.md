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

If you are using windows, you also need to install git:

* [git](https://git-scm.com/download/win)

and then add the path to your installation (for example, "C:\Program Files\Git\usr\bin") into your system's %PATH% variable. If you don't know how to do this, you can look at [these instructions](http://www.computerhope.com/issues/ch000549.htm). This will allow us to remotely access the VM using git's SSH client. If you are using OSX, an SSH client is already included.

### Getting started with Github

All of the work you will do for this class, including downloading the setup files for your VM as well as completing and handing in lab assignments will be done through this Github repository. Github is a [distributed revision control](https://en.wikipedia.org/wiki/Distributed_revision_control) tool that is extremely popular with software developers. It is used by developers to manage code and other files related to projects, and to organize it in a way that makes it easy to develop projects within a team. With text and other [human-readable](https://en.wikipedia.org/wiki/Human-readable_medium) files, Github can keep track of changes being made, allowing you to easily see which parts of the project are being developed, and to roll back changes if necessary. Github also provides several other features useful for software development, including different access control to different parts of the project, bug tracking, feature requests, task management, and wikis for every project. You can think of Github as Google Docs, in that it keeps track of changes in text documents and allows collaboration on documents between different team members. Unlike Google Docs, however, Github is much more structured, and uses explicit changes or 'commits' to keep track of the changes being made by each person on the team.

Github will allow us to keep track of our code as we develop the lab assignments, and to streamline the process of handing them in. In the process, we will learn some of the standards of how code is developed in the real world. If you've never used it before, Github can seem a bit daunting and even somewhat counter-intuitive. Luckily, Github provides many [resources](https://help.github.com/articles/good-resources-for-learning-git-and-github/) for learning the system by following step-by-step [tutorials](https://guides.github.com/). I recommend you at least go through the ['Hello World'](https://guides.github.com/activities/hello-world/) tutorial before proceeding with the rest of this lab.

Note: Github is based on the [Git](https://git-scm.com/) version control system, which is used completely through the command line (by typing text commands rather than clicking buttons on a graphic user interface). However, Github also provides a standalone [desktop client](https://desktop.github.com/) with a graphic user interface which can be easier to use for beginners. The client has all the features you will need to complete these labs, so you should not have to use the command line interface, but feel free to learn, explore, and use it if you are comfortable with it.

### Forking and Branching, Push and Pulling

To structure collaboration and keep track of document revisions, Github is based on a very specific [workflow](https://guides.github.com/introduction/flow/). Each project is contained within its own **repository**, which you can think of as a folder on your desktop. This repository exists on Github's servers, but you can also **clone** the repository to your desktop, where it will live inside a specified folder (usually called Git or Github within your My Documents folder). The Github software will then take care of syncing your local folder to the contents of the repository.

Each repository can contain multiple **branches** or versions of the project. When you start a project, by default all of your changes will go on the *master* branch, which is the main version of your project. At any point you can start another branch, which will replicate all your files and allow you to make changes without affecting the master branch. In software development this is used to test out ideas or features in a safe way, while master maintains the latest stable working version of the code. At any point you can merge the contents of a branch with the master, and the Github interface will help you to look through the changes and handle any conflicts. 

When you make a change to a document locally, Github will not automatically save the changes to the repository. To update the project with your changes, you need to push a **commit** to the repository. The commit tracks every change made to every document since the last commit, and provides a clear revision history of the project. At any point, you can step through the commits to undo any changes that have been made.

In addition to storing and tracking your own projects, Github provides several options for contributing to other people's projects. By default, all code on Github is open-source, meaning everyone can see the code freely. However, you cannot make changes or 'commit' to it without being granted permission by the repository's owners. Another way to contribute to a project is to **fork** the project, or create your own version of the repository under your own account. This fork will function just like the main repository, allowing you to make changes and push commits to it, but will exist separately. You are free to keep developing this fork on your own, and even spin it off as its own separate project. If at any point you want to contribute your changes to the main project, you can submit a **pull request**, which will alert the repository owners of any changes you have made, and give them the chance to either accept the pull request and merge in the code, or deny it and keep their code as it is. This fork/pull request workflow is quite common in [open-source software development](https://en.wikipedia.org/wiki/Open-source_software_development), where many people might be contributing to a project without a higher level organization structure.

### Cloning the repository

To get started, go to https://github.com/ and sign up for a free account:

![GitHub account](/images/github01.png)




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
