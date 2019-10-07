# ai

## Setup

The following procedure describes how to create a virtualenv appropriate for
running the ai sample code:

```bash
#
# Set up the virtualenv and install required packages. By default the
# virtualenv will be setup to use python3. If python2 is desired, use the make
# target "bootstrap-python2" and the virtualenv will be created under
# "env-python2"
#
user@host: ~/ai$ make bootstrap

#
# Enter the virtualenv
#
user@host: ~/ai$ source env/bin/activate

#
# Create the ai-* launch entry points in the virtualenv. These entry points
# are aliases for the scripts which use the ai REST API to interact with an
# account (e.g. ai-market-order, ai-trades-list, etc.)
#
(env)user@host: ~/ai$ python setup.py develop
```

## Entering the ai environment

The ai virtualenv must be activated to ensure that the current
enviroment is set up correctly to run the sample code. This is done using the
virualenv's activate script:

```bash
user@host: ~/ai$ source env/bin/activate
(env)user@host: ~/ai$
```

The "(env)" prefix found in the prompt indicates that we are using the
virtualenv "env".  To leave the virtualenv, run the deactivate function:

```bash
(env)user@host: ~/ai$ deactivate
user@host: ~/ai$ 
```

## Sample Code

Following is a listing of the sample code provided. More details can be found
in the READMEs provided in each src directory.

| Source File | Entry Point | Description |
| ----------- | ----------- | ----------- |
| `src/test/test.py` | ai-test | execute test |

## Set Env

heroku config:set instrument=USD_JPY -a oandapy

pip freeze > requirements/base.txt
pip install -r requirements/base.txt