import random
from common.instance_generator import random_person

from common.constants import (
    COVER_LETTER,
    EMAILS,
    FIRSTNAME,
    LASTNAME,
    LINKS,
    ONE_VALUE_FIELDS,
    MULTI_VALUE_FIELDS,
    FUNCTION_FIELDS,
    FIRST_NAME_GLOBAL,
    LAST_NAME_GLOBAL,
    NAME,
    SOCIAL_LINKS,
    PHONES,
)

from common.constants import social_links, phone_list, cover_letter_list
from common.utils import random_emais, with_opt_data

recruitee_person_data_format = {
    FIRST_NAME_GLOBAL: FIRSTNAME,
    LAST_NAME_GLOBAL: LASTNAME,
}

recruitee_optional_data = {
    MULTI_VALUE_FIELDS: {
        PHONES: phone_list,
        SOCIAL_LINKS: social_links,
        LINKS: social_links,
    },
    ONE_VALUE_FIELDS: {COVER_LETTER: cover_letter_list},
    FUNCTION_FIELDS: {EMAILS: random_emais},
}


@with_opt_data(recruitee_optional_data)
def random_candidate():
    person = random_person(recruitee_person_data_format)
    return {NAME: " ".join([person[FIRSTNAME], person[LASTNAME]])}
