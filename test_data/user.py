"""
The module contains the methods to generate fake user data.
"""

from faker import Faker


class User:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.full_name = None
        self.email = None
        self.password = None

    def generate_user_data(self):
        fake = Faker()

        first_name = fake.first_name_female()
        last_name = fake.last_name_female()

        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.email = fake.email()
        self.password = fake.password()

    def __str__(self):
        return f"User name is '{self.full_name}', email is '{self.email}', password is '{self.password}'"
