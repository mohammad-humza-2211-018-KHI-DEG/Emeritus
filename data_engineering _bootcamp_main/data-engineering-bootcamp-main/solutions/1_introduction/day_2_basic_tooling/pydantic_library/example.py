from typing import List

import pydantic


class Hobby(pydantic.BaseModel):
    name: str
    is_a_team_hobby: bool


class Person(pydantic.BaseModel):
    first_name: str
    last_name: str
    hobbies: List[Hobby]


example = Person(
    first_name="John",
    last_name="Smith",
    hobbies=[Hobby(name="Football", is_a_team_hobby=True)],
)
example_as_dict = example.dict()
print(example_as_dict)
print(Person(**example_as_dict))

malformed_dictionary = {
    "first_name": "John",
    # The dictionary is malformed, because instead of `last_name` we have `surname`
    "surname": "Smith",
    "hobbies": [{"name": "Football", "is_a_team_hobby": True}],
}
print(Person(**malformed_dictionary))
