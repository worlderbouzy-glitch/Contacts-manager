
from interfaces.contact_repository import ContactRepository
from infrastructure.database import contacts


class ContactRepositoryImpl(ContactRepository):

    def add(self, contact):
        contacts.append(contact)

    def get_by_id(self, contact_id):

        for contact in contacts:
            if contact.id == contact_id:
                return contact

        return None

    def get_all(self):
        return contacts

    def update(self, contact):

        for index, current_contact in enumerate(contacts):

            if current_contact.id == contact.id:
                contacts[index] = contact
                return

    def delete(self, contact_id):

        for contact in contacts:

            if contact.id == contact_id:
                contacts.remove(contact)
                return

    def find_by_name(self, name):

        for contact in contacts:

            if contact.name.lower() == name.lower():
                return contact

        return None

    def find_by_phone(self, phone):

        for contact in contacts:

            if contact.phone == phone:
                return contact

        return None

    def find_by_email(self, email):

        for contact in contacts:

            if contact.email.lower() == email.lower():
                return contact

        return None

    def exists(self, contact_id):

        return self.get_by_id(contact_id) is not None

    def count(self):

        return len(contacts)