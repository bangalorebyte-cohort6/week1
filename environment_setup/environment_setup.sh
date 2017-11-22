#!/bin/bash

#Shell envioronment setup for linux and mac OS ased systems to install all the components
PLATFORM="unknown"
HOST_TYPE=`uname`
COURSE_TYPE=$1

#Detect the OS type
echo "Setting Environement for $HOST_TYPE and $COURSE_TYPE"

if [ "$HOST_TYPE" = "Darwin" ]; then
    platform="MacOS"

    #Install home brew

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    brew install bash-completion
    brew install python3
    brew link python3
    brew update
    pip3 install --upgrade pip
    brew install gsl
    brew install git
    
    pip3 install virtualenv
    pip3 install sed
    pip3 install awk
    pip3 install wget
    pip3 install requests
    pip3 install sublime
    pip3 install networkX
    brew install nginx	
    brew install rsync
    pip3 install sqlite3
    
    if [ "$COURSE_TYPE" = "FULL_STACK_WEB" ]; then 
    	echo "Setting up development environment for Full Stack Web Development"
        pip3 install django
    	pip3 install sqlalchemy
    	pip3 install flask
    	pip3 install psycopg2
    	pip3 install lxml

    elif [ "$COURSE_TYPE" = "DATA_SCIENCE" ]; then
    	echo "Setting up development environment for Data Engineering"
    	brew install hadoop
    	pip3 install numpy
    	pip3 install pandas
    	pip3 install statsmodels
    	pip3 install bs4
    	pip3 install scikit-learn
    	pip3 install clang
    	pip3 install nltk
    	pip3 install scrapy
    	pip3 install seaborn
    	pip3 install bokeh
    	pip3 install spark
    	pip3 install tensorflow
     fi

     echo "Setup Complete for $COURSETYPE for system $UNAMESTR "
     echo "Welcome to Byte Dev : Ready to Rock n Roll"    

elif [ "$HOST_TYPE" = "Linux" ]; then
    platform="Linux"
 
#Python and Linux based package installation
   
    sudo apt-get -y install build-essential
    sudo apt-get -y install git
    sudo apt-get -y install bash-completion
    sudo apt-get -y install wget

    sudo apt-get -y install python3 python3-dev
    sudo apt-get -y install libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
    sudo apt-get -y install python3-setuptools
    sudo apt-get -y install gsl-bin libgsl-dev
    sudo apt-get -y install mongodb
    sudo easy_install3 pip
    sudo pip3 install virtualenv
    sudo pip3 install requests
    sudo pip3 install sqlite3

    if [" $COURSE_TYPE " = "FULL_STACK_WEB" ]; then 
    	echo "Setting up development environment for Full Stack Web Development"
        sudo pip3 install django
	sudo pip3 install psycopg2
	sudo pip3 install networkX
    	sudo pip3 install flask
    	sudo pip3 install redis

    elif [" $COURSE_TYPE " = "DATA_SCIENCE"]; then
	echo "Setting up development environement for Data Engineering"    	
    	 
    	sudo pip3 install numpy
    	sudo pip3 install scipy
    	sudo pip3 install pandas
    	sudo pip3 install bs4
    	sudo pip3 install statsmodels
    	sudo pip3 install nltk
    	sudo pip3 install scrapy
    	sudo pip3 install seaborn
    	sudo pip3 install bokeh
    
    	sudo pip3 install pymysql
    	sudo pip3 install sqlalchemy
    	sudo pip3 install spark
    	sudo pip3 install tensorflow
    	sudo pip3 install lxml
     fi

     echo "Setup Complete for $COURSETYPE for system $UNAMESTR "
     echo "Welcome to Byte Dev : Ready to Rock n Roll"    

fi

