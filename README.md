# TF - IDF counter from .TXT format file

## Clone repository
```bash
git clone https://github.com/abdulatif-abdumannopov/lesta_test_work
```
## Create *venv* file and install *django*
```bash
python -m venv venv
pip install django
```
## Create your Django Project
```bash
    django-admin startproject DjangoProject
```
## Add application in settings.py and static files
```settings.py
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
]

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
```
## Create /documents folder in your main project directory
```
ваш-репозиторий/
├── document/
├── manage.py
├── app/
├── templates/
├── static/
├── .venv
```
