import random

from common.utils import random_date_str, random_time, random_start_end_date
from common.constants import GENDER, FIRST_NAME, LAST_NAME, EMAIL, HIRE_DATE
from common.constants import gender_list, first_name_list, last_name_list, optional_data
from common.constants import NEW, UPDATE

from common.api_test_data import random_employee_id, random_time_off_type_id

from datetime import datetime


def random_employee():
    employee = {GENDER: random.choice(gender_list)}
    employee = {}
    employee[FIRST_NAME] = random.choice(first_name_list["male"])
    employee[LAST_NAME] = random.choice(last_name_list)
    employee[EMAIL] = (
        ".".join([employee[FIRST_NAME], employee[LAST_NAME]]) + "@vacuumlabs.com"
    )

    for option_key in optional_data:
        employee[option_key] = random.choice(optional_data[option_key])

    employee[HIRE_DATE] = random_date_str()

    return employee


def random_attendance(ACTION=UPDATE):
    attendance = {
        "date": random_date_str(),
        "start_time": random_time(8, 11),
        "end_time": random_time(13, 18),
        "break": random.randint(0, 12) * 5,
        "comment": random.choice(
            ["I was productive as hell", "I was lazy", "I was sick"]
        ),
    }
    if ACTION == NEW:
        attendance["employee"] = random_employee_id()

    return attendance


def random_attendance_list():
    attendance_count = random.randint(1, 5)
    return [random_attendance(NEW) for _ in range(attendance_count)]


def random_time_off():
    start_date, end_date = random_start_end_date()
    return {
        "employee_id": random_employee_id(),
        "time_off_type_id": random_time_off_type_id(),
        "start_date": start_date,
        "end_date": end_date,
        "half_day_start": str(random.randint(0, 1)),
        "half_day_end": str(random.randint(0, 1)),
    }


def form_data(payload):
    return "&".join(["=".join([key, str(value)]) for key, value in payload.items()])
