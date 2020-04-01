.ONESHELL: #Kepp virtualenv sourced
install_dev_deps:
	. ./venv/bin/activate
	pip install --upgrade pip
	pip install cryptacular
	python setup.py install
	python setup.py develop

.ONESHELL: #Keep virtualenv sourced
venv36:
	python3.6 -m venv venv

.ONESHELL: #Keep virtualenv sourced
from_scratch:
	deactivate
	rm -fr venv
	make venv36
	make install_dev_deps



