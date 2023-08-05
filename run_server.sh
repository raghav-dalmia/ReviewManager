sudo cd /home/ubuntu/project/ReviewManager
source venv/bin/activate
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo systemctl restart nginx
