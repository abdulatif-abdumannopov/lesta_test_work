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
## Create manage.py file
```manage.py
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```
## Create documents folder
