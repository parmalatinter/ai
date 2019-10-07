.PHONY: bootstrap
bootstrap: bootstrap-python

bootstrap-python:
	virtualenv -p python env
	env/bin/pip install -r requirements/base.txt
	
bootstrap-python3:
	virtualenv -p python3 env
	env/bin/pip install -r requirements/base.txt

bootstrap-python2:
	virtualenv env-python2
	env-python2/bin/pip install -r requirements/base.txt

