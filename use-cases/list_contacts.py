

class ListContacts:

    def __init__(self, repository):
        self.repository = repository

    def execute(self):

        contact = self.repository.get_all()

        if contact is None:
            raise ValueError("Unable to retrieve contacts")
        if not isinstance(contact, list):
            raise TypeError("Repository must return a list of contacts")
        
        contact.sort(key=lambda c: c.name.lower())
        return contact