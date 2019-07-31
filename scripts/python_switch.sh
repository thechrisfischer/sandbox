#!/bin/bash

#check which version avaliable

brew switch python

#switch to old version of python

brew switch python 3.6.5

#list all packages from 3.6.5, and save to txt

pip3 freeze | cut -d'=' -f1 > python3.6-requirements.txt

#switch back to latest version of python

brew switch python 3.7.0

#install and upgrade all packages from 3.6.5

pip3 install --upgrade -r python3.6-requirements.txt

#delete txt

rm python3.6-requirements.txt
