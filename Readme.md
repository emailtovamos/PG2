**Link to Heroku app**: https://arcane-retreat-46619.herokuapp.com/


**Instructions to run locally:**

- Download code and go to code directory in command line: 

    `git clone https://github.com/emailtovamos/PG2.git`

    `cd PG2/`

- Create and activate virtual environment:

    `python3 -m venv django_env`

    `source django_env/bin/activate`

- Spacy related commands:

    `pip3 install -U pip setuptools wheel`

    `pip3 install -U spacy`

    `python3 -m spacy download en_core_web_sm`

    (`python3 -m spacy download en_core_web_trf` -> For more accuracy but not part of the code now)

- Install requirements:

    `pip3 install -r requirements.txt`

- Run server: 

    `python myproject/manage.py runserver`

- Go to the link and enter text to get expected diseases. Accuracy won't be great due to no full check and usage of smaller spacy package.