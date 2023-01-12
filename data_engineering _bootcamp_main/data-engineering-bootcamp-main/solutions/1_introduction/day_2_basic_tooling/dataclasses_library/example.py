from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str


instance = Person("John", "Smith")
print(instance)
print(instance == Person("John", "Smith"))
