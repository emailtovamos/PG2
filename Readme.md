Download code and go to code directory in command line

python3 -m venv django_env

source django_env/bin/activate


pip3 install -U pip setuptools wheel
pip3 install -U spacy

python3 -m spacy download en_core_web_trf

python3 -m spacy download en_core_web_sm

pip3 install -r requirements.txt

Add this file(http://www.orphadata.org/data/xml/en_product4.xml) in myproject/model folder

python myproject/manage.py runserver