#!/bin/bash

#build th project 
echo "Building the project..." 
python3.6.8 -m pip install -r requirements.txt 

echo "Make Migration..." 
python3.6.8 manage.py makemigrations --noinput 
python3.6.8 manage.py migrate --noinput 

echo "Collect Static..." 
python3.6.8 manage.py collectstatic --noinput --clear