.ONESHELL: #Keep virtualenv sourced
venv36:
	python3.6 -m venv venv

#.ONESHELL: #Keep virtualenv sourced
#build_and_test: from_scratch
#	python setup test

.ONESHELL:
clean_and_prepare:
	rm -fr venv
	make venv36
	. ./venv/bin/activate
	pip install --upgrade pip


.ONESHELL: #Keep virtualenv sourced
build_and_test: clean_and_prepare
	. ./venv/bin/activate
	pip install cryptacular
	python setup.py install
	python setup.py develop
	python setup.py test
	pytest .
