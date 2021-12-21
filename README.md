## Installation

### Environment

- Python 3.8.5

### Virtual environment

    $ cd personio  # root directory
    $ python -m venv venv
    $ . venv/bin/activate

### Dependicies

    $ pip install -r requirements.txt

## Personio

### Prerequisites:

Add credentials of users to `auth_params_list` in [common/secret.py](common/secret.py)

### Running

    $  locust -f locustfiles/personio.py

### Running with tags

    $  locust -f locustfiles/personio.py --tags list

### Running without some tags

    $  locust -f locustfiles/personio.py --exclude-tags unavailable

## Workable

### Prerequisites:

Set Access Token value to `token` attribut of WorkableUser in [locustfiles/workable.py](locustfiles/workable.p)

### Running

    $  locust -f locustfiles/workable.py

### Running with tags

    $  locust -f locustfiles/workable.py --tags list

### Running without some tags

    $  locust -f locustfiles/workable.py --exclude-tags unavailable
