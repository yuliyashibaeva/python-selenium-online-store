"""
The module contains the methods to generate random user data.
"""

from faker import Faker
from faker.providers import person, internet
from string import ascii_letters, digits, punctuation
from random import choices, shuffle


class UserAccountDataGeneration:
    @staticmethod
    def generate_user_data() -> dict:
        user_data = {}

        # user name
        fake = Faker()
        fake.add_provider(person)
        first_name = fake.first_name_female()
        last_name = fake.last_name_female()

        user_data["first_name"] = first_name
        user_data["last_name"] = last_name
        user_data["full_name"] = first_name + " " + last_name

        # user email
        fake.add_provider(internet)
        user_data["user_email"] = fake.email()

        # user password
        password = choices(ascii_letters, k=6)
        password.extend(choices(digits, k=2))
        password.extend(choices(punctuation, k=2))
        shuffle(password)
        user_data["user_password"] = "".join(password)

        return user_data
