
from src.entities.contact import Contact


class CreateContact:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, contact_id, name, phone, email):

        if not name.strip():
            raise ValueError("Name cannot be empty.")

        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits.")

        if len(phone) < 8:
            raise ValueError("Phone number is too short.")

        if "@" not in email:
            raise ValueError("Invalid email address.")

        if self.repository.find_by_phone(phone):
            raise ValueError("Phone number already exists.")

        new_contact = Contact(
            contact_id,
            name,
            phone,
            email
        )

        self.repository.add(new_contact)

        return new_contact