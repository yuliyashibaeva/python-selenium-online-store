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

    @staticmethod
    #  the method to get static user data in case there is no need to create a new one
    #  there is a user with the following email and password on the test store
    def get_static_user_data() -> dict:
        user_data = {
            'first_name': 'Alyssa',
            'last_name': 'Cummings',
            'full_name': 'Alyssa Cummings',
            'user_email': 'wsnyder@example.com',
            'user_password': 'ehJ}Da13Z='
        }

        return user_data
