#!/bin/bash
python_interpreter=""

read -p "┌────────────────────┐
| Python interpreter |
└────────────────────┘
Default: /usr/bin/python
(Сlick Enter for choose default)
If you wont to change, write: " python_interpreter


if [ -z "$python_interpreter" ]; then
    /usr/bin/python -m venv env
else
    `$python_interpreter -m venv env`
fi

source env/bin/activate
pip install -U pip && pip install -r src/requirements.txt

python src/manage.py collectstatic --noinput
python src/manage.py makemigrations --name alter_db_table
python src/manage.py migrate
python src/build.py
python src/manage.py runserver --insecure