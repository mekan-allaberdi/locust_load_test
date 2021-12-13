## Installation

### Environment

- Python 3.8.5

### Virtual environment

    $ cd personio  # root directory
    $ python -m venv venv
    $ . venv/bin/activate

### Dependicies

    $ pip install -r requirements.txt

### Prerequisites:

Add credentials of users to `auth_params_list` in [common/secret.py](common/secret.py)

## Running

    $ locust

## Running with tags

    $ locust --tags list

## Running without some tags

    $ locust --exclude-tags unavailable
