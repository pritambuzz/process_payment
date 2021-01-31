.ONESHELL:

.PHONY: clean install tests run all

database_init:
	python manage.py db init

database_migrate:
	python manage.py db migrate

database_upgrade:
	python manage.py db upgrade

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	virtualenv -p python3 process_payment; \
	. process_payment/bin/activate
	pip3 install -r requirements.txt

tests:
	. process_payment/bin/activate; \
	python manage.py test

run:
	. process_payment/bin/activate; \
	python manage.py run

all: install clean database_init database_migrate database_upgrade run
