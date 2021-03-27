https://arcane-retreat-46619.herokuapp.com/

Download code and go to code directory in command line

python3 -m venv django_env

source django_env/bin/activate

pip3 install -U pip setuptools wheel
pip3 install -U spacy

python3 -m spacy download en_core_web_trf

python3 -m spacy download en_core_web_sm

pip3 install -r requirements.txt

python myproject/manage.py runserver