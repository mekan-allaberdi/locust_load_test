## Installation

### Environment

- Python 3.8.5

### Virtual environment

    $ cd personio  # root directory
    $ python -m venv venv
    $ . venv/bin/activate

### Dependicies

    $ pip install -r requirements.txt

## Running

    $ locust

## Running with tags

    $ locust --tags list

## Running without some tags

    $ locust --exclude-tags unavailable
