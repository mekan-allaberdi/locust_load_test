from datetime import datetime, timedelta
import random


def random_time(start_hour=9, end_hour=18):
    """
    Parameters
    ----------
    start_hour: int
    end_hour: int

    Returns
    -------
    string
        time in 'hh:mmm' format between start_hour and end_hour.
    """
    assert 0 <= start_hour <= end_hour <= 23

    return "{:02d}:{:02d}".format(
        random.randint(start_hour, end_hour), random.randint(0, 59)
    )


def random_date(start_date=datetime(2021, 12, 20), end_date=datetime.today()):
    """
    Parameters
    ----------
    start_date: datetime
    end_date: datetime

    Returns
    -------
    datetime
        Random date between given start and end date.
    """
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))


def date_to_str(date):
    """
    Parameters
    ----------
    start_date: datetime

    Returns
    -------
    string
        Date in 'yyyy-mm-dd' format.
    """
    return date.strftime("%Y-%m-%d")


def random_date_str(start_date=datetime(2015, 1, 1), end_date=datetime.today()):
    """
    Parameters
    ----------
    start_date: datetime
    end_date: datetime

    Returns
    -------
    string
        Random date in 'yyyy-mm-dd' format between given start and end date.
    """
    return date_to_str(random_date(start_date, end_date))


def random_start_end_date():
    """
    Generates random two dates in 'yyyy-mm-dd' format between 2018.01.01 and 2021-12-12.

    Returns
    ----------
    start_date: string
    end_date: string
        The start_date date always comes before the end_date.
    """
    date = random_date(datetime(2015, 1, 1), datetime(2018, 1, 1))
    return date_to_str(date), date_to_str(date + timedelta(days=random.randint(1, 7)))


def get_next_token(func):
    """
    Getting next token from the response headers.
    """

    def wrapper(*args, **kwargs):
        user = args[0].user
        response = func(*args, **kwargs)
        if "authorization" in response.headers:
            user.token = response.headers["authorization"].replace("Bearer ", "")
        else:
            user.authenticate()

    return wrapper


def with_opt_data(optional_data):
    def wrap(f):
        def wrapped_f(*args):
            data = f(*args)
            for option_key in optional_data:
                data[option_key] = random.choice(optional_data[option_key])
            return data

        return wrapped_f

    return wrap