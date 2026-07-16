
from entities.contact import Contact

from use_cases.create_contact import CreateContact
from use_cases.list_contact import ListContacts
from use_cases.delete_contact import DeleteContact
from use_cases.update_contact import UpdateContact
from use_cases.search_contact import SearchContact


class ContactController:

    def __init__(self, repository):

        self.create = CreateContact(repository)
        self.list = ListContacts(repository)
        self.delete = DeleteContact(repository)
        self.update = UpdateContact(repository)
        self.search = SearchContact(repository)

    def add(self, id, name, phone, email):

        contact = Contact(id, name, phone, email)

        self.create.execute(contact)

    def list(self):

        return self.list.execute()

    def delete(self, id):

        self.delete.execute(id)

    def update(self, id, name, phone, email):

        contact = Contact(id, name, phone, email)

        self.update.execute(contact)

    def search(self, name):

        return self.search.execute(name)