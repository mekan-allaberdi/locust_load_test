import random
from api.lever.data import OWNER_ID_LIST, STAGE_ID_LIST, random_posting
from common.instance_generator import random_person

from common.constants import (
    EMAILS,
    FIRSTNAME,
    HEADLINE,
    LASTNAME,
    LINKS,
    ONE_VALUE_FIELDS,
    MULTI_VALUE_FIELDS,
    FUNCTION_FIELDS,
    FIRST_NAME_GLOBAL,
    LAST_NAME_GLOBAL,
    NAME,
    OWNER,
    POSTINGS,
    PHONES,
    SOURCES,
    STAGE,
    TAGS,
)

from common.constants import (
    social_links,
    phone_list,
    phone_types,
    position_list,
    tag_list,
    source_list,
)
from common.utils import random_emais, with_opt_data


def random_phones():
    phones = random.sample(phone_list, random.randint(1, 3))
    return [{"value": phone, "type": random.choice(phone_types)} for phone in phones]


def random_tags():
    return random.sample(tag_list, random.randint(3, 8))


lever_person_data_format = {
    FIRST_NAME_GLOBAL: FIRSTNAME,
    LAST_NAME_GLOBAL: LASTNAME,
}

lever_optional_data = {
    MULTI_VALUE_FIELDS: {
        LINKS: social_links,
        SOURCES: source_list,
    },
    ONE_VALUE_FIELDS: {
        HEADLINE: position_list,
        STAGE: STAGE_ID_LIST,
        OWNER: OWNER_ID_LIST,
    },
    FUNCTION_FIELDS: {
        EMAILS: random_emais,
        PHONES: random_phones,
        POSTINGS: random_posting,
        TAGS: random_tags,
    },
}


@with_opt_data(lever_optional_data)
def random_opportunity():
    person = random_person(lever_person_data_format)
    return {NAME: " ".join([person[FIRSTNAME], person[LASTNAME]])}
