
VENV_PYTHON=$(which) python

HOST=0.0.0.0
PORT=8000

SETTINGS_LOCAL=config.settings.local

APP_NAME=apps

run.local:
	$(VENV_PYTHON) manage.py runserver $(HOST):$(PORT) --settings=$(SETTINGS_LOCAL)

run.test:
	$(VENV_PYTHON) manage.py test $(APP_NAME)

run.db.container:
	cd .dbcontainer && sudo docker-compose up -d


run.app_setup.all:
	$(VENV_PYTHON) manage.py app_setup all