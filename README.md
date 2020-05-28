# Kats Blog

![Python 3.7.7](https://img.shields.io/badge/Python-3.7.7-blue)

## Set up locally

```sh
pip3 install -r requirements.txt
flask db upgrade
python3 app.py
open http://127.0.0.1:5000/
```

## Deploy to Google Cloud

Enter the following commands in a Google Cloud shell (SSH):

```sh
cd /var/www/katsblog
git pull origin master
pip install -r requirements.txt
flask db upgrade
sudo systemctl restart katsblog
```
