import random

from common.utils import random_date_str, random_time, random_start_end_date

from common.constants import (
    NEW,
    UPDATE,
    GENDER,
    HIRE_DATE,
    personio_optional_data,
    personio_person_data_format,
)

from common.instance_generator import random_person, with_opt_data

from api.personio.data import random_employee_id, random_time_off_type_id


def random_employee():
    employee = random_person(personio_person_data_format)
    employee[HIRE_DATE] = random_date_str()
    return with_opt_data(employee, personio_optional_data)


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
        "employee_id": random_employee_id("personio"),
        "time_off_type_id": random_time_off_type_id(),
        "start_date": start_date,
        "end_date": end_date,
        "half_day_start": str(random.randint(0, 1)),
        "half_day_end": str(random.randint(0, 1)),
    }


def form_data(payload):
    return "&".join(["=".join([key, str(value)]) for key, value in payload.items()])
