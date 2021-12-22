import random
from common.constants import FIRST_NAME_GLOBAL, LAST_NAME_GLOBAL, GENDER, EMAIL
from common.constants import first_name_list, last_name_list, gender_list


def random_person(tool_attr_format):
    person = {GENDER: random.choice(gender_list)}

    first_name_format, last_name_format = (
        tool_attr_format[FIRST_NAME_GLOBAL],
        tool_attr_format[LAST_NAME_GLOBAL],
    )

    person[first_name_format] = random.choice(first_name_list[person[GENDER]])

    person[last_name_format] = random.choice(last_name_list)
    person[EMAIL] = (
        ".".join([person[first_name_format], person[last_name_format]])
        + "@vacuumlabs.com"
    )
    return person


def with_opt_data(data, optional_data):
    for option_key in optional_data:
        data[option_key] = random.choice(optional_data[option_key])
    return data
