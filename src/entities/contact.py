
from os import name

from frameworks.config import MIN_NAME_LENGTH

class Contact:


    def __init__(self, contact_id, name, phone, email):

        self.set_id(contact_id)
        self.set_name(name)
        self.set_phone(phone)
        self.set_email(email)

    def set_id(self, contact_id):

        if contact_id <= 0:
            raise ValueError("Contact ID must be greater than zero.")

        self.id = contact_id

    def set_name(self, name):

        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        if not name.strip():
            raise ValueError("Name cannot be empty.")

        if len(name) < 2:
            raise ValueError("Name must contain at least 2 characters.")

        self.name = name.strip().title()

    def set_phone(self, phone):

        phone = str(phone).strip()

        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits.")

        if len(phone) < 8:
            raise ValueError("Phone number must contain at least 8 digits.")

        self.phone = phone

    def set_email(self, email):

        email = email.strip()

        if "@" not in email or "." not in email:
            raise ValueError("Invalid email address.")

        self.email = email.lower()

    def update_contact(self, name, phone, email):

        self.set_name(name)
        self.set_phone(phone)
        self.set_email(email)

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

    def __str__(self):

        return (
            f"Contact ID : {self.id}\n"
            f"Name       : {self.name}\n"
            f"Phone      : {self.phone}\n"
            f"Email      : {self.email}"
        )