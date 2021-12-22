import random

from common.constants import (
    FIRSTNAME,
    LASTNAME,
    GENDER,
    DISQUALIFIED,
    EDUCATION_ENTRIES,
    EXPERIENCE_ENTRIES,
    FIRST_NAME_GLOBAL,
    LAST_NAME_GLOBAL,
    HEADLINE,
    ONE_VALUE_FIELDS,
    SKILLS,
    SOCIAL_PROFILES,
    SUMMARY,
    ADDRESS,
    PHONE,
    COVER_LETTER,
    EDUCATION_ENTRIES,
    EXPERIENCE_ENTRIES,
    SKILLS,
    SOCIAL_PROFILES,
    DISQUALIFIED,
)

from common.constants import (
    position_list,
    summary_list,
    address_list,
    phone_list,
    cover_letter_list,
    education_entries_list,
    experience_entries_list,
    skill_list,
    social_profile_list,
)

from common.utils import with_opt_data
from common.instance_generator import random_person

workable_person_data_format = {
    FIRST_NAME_GLOBAL: FIRSTNAME,
    LAST_NAME_GLOBAL: LASTNAME,
}

workable_optional_data = {
    ONE_VALUE_FIELDS: {
        HEADLINE: position_list,
        SUMMARY: summary_list,
        ADDRESS: address_list,
        PHONE: phone_list,
        COVER_LETTER: cover_letter_list,
        EDUCATION_ENTRIES: education_entries_list,
        EXPERIENCE_ENTRIES: experience_entries_list,
        SKILLS: skill_list,
        SOCIAL_PROFILES: social_profile_list,
        DISQUALIFIED: [True, False],
    }
}


@with_opt_data(workable_optional_data)
def random_candidate():
    person = random_person(workable_person_data_format)

    if GENDER in person:
        person.pop(GENDER)
    return person


def random_comment():
    return {
        "comment": {
            "body": random.choice(
                [
                    "He is really good",
                    "Under performance",
                    "Does not have enough experience",
                ]
            ),
            "policy": random.sample(["recruiter", "simple"], random.randint(0, 2)),
            "attachment": {
                "name": "tiny.gif",
                "data": "R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=",
            },
        }
    }


def random_tags():
    return random.sample(
        [
            "globetrotter",
            "adventurer",
            "social",
            "engineering",
            "gold medalist",
            "high potential",
        ],
        random.randint(0, 3),
    )


def random_disqualification_reason():
    return (
        random.choice(
            [
                "Not fit",
                "Future opportunistic hire",
                "social",
                "Underqualified",
                "Withdrew",
                "Salary",
                "Passive/no response",
                "Accepted another offer",
            ]
        ),
    )
