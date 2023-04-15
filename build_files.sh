echo "BUILD START" 
python -m pip install -r requirements.txt
python manage.py artibot_backend --noinput --clear
echo "BUILD END" 