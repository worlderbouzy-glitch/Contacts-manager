

class DeleteContact:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, id):
        contact = self.repository.get_all()

        for contact in contact:
            if contact.id == id:
                self.repository.delete(id)
                return contact
        raise ValueError("contact intouvable")    