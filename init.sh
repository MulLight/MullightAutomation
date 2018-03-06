#!/bin/bash

connectivity=`ifconfig | grep -c "192"`
if [ $connectivity -lt 1 ]
then 
echo "Not connected"
fi

git stash
git stash clear
git pull

pip3list=`pip3 list`

tornado=`echo $pip3list | grep -c tornado`
if [ $tornado -lt 1 ]
then
pip3 install tornado
fi

motor=`echo $pip3list | grep -c motor`
if [ $motor -lt 1 ]
then
pip3 install motor
fi

openpyxl=`echo $pip3list | grep -c openpyxl`
if [ $openpyxl -lt 1 ]
then
pip3 install openpyxl
fi

serial=`echo $pip3list | grep -c serial`
if [ $tornado -lt 1 ]
then
pip3 install serial
fi

pymongo=`echo $pip3list | grep -c pymongo`
if [ $tornado -lt 1 ]
then
pip3 install pymongo
fi


python3 main.py &
