from datetime import datetime, timedelta
import random


def random_time(start_hour, end_hour):
    return "{:02d}:{:02d}".format(
        random.randint(start_hour, end_hour), random.randint(0, 59)
    )


def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))


def date_to_str(date):
    return date.strftime("%Y-%m-%d")

def random_date_str(start=datetime(2015, 1, 1), end=datetime.today()):
    return date_to_str(random_date(start, end))


def random_start_end_date():
    date = random_date(datetime(2018, 1, 1), datetime(2021, 12, 12))
    return date_to_str(date), date_to_str(date + timedelta(days=random.randint(1, 7)))


def get_next_token(func):
    def wrapper(*args, **kwargs):
        user = args[0].user
        response = func(*args, **kwargs)
        if "authorization" in response.headers:
            user.token = response.headers["authorization"].replace("Bearer ", "")
        else:
            user.authenticate()

    return wrapper


