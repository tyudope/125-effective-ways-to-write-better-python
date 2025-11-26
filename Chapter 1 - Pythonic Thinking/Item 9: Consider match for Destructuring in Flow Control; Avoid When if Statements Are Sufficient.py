import enum

class ColorEnum(enum.Enum):

    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"


def take_enum_action(light):

    match light:
        case ColorEnum.RED:
            print("Stop")
        case ColorEnum.YELLOW:
            print("Slow down")
        case ColorEnum.GREEN:
            print("Go!")
        case _:
            raise RuntimeError


take_enum_action(ColorEnum.RED)


# Deserialize JSON

from dataclasses import dataclass

@dataclass
class PersonCustomer:
    first_name : str
    last_name : str

@dataclass
class BusinessCustomer:
    company_name : str


record1 = """{"customer" : {"last" : "Ross" , "first" : "Bob"}}"""
record2 = """{"customer" : {"entity" : "Sabanci Holding"}}"""

import json
def deserialize(data):
    record = json.loads(data)
    match record:
        case {"customer" : {"last" : last_name,
                            "first" : first_name}}:
            return PersonCustomer(first_name, last_name)

        case {"customer" : {"entity" : company_name}}:
            return BusinessCustomer(company_name)

        case _:
            raise ValueError("Unknown Record Type")


print("Record 1: " , deserialize(record1))
print("Record 2: " , deserialize(record2))