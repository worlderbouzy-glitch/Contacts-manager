

class UpdateContact:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, contact, id, name, firstname, email, phone):
        self.repository.update(contact, id, name, firstname, email, phone)

        conatct = self.repository.get_all()

        contact=None
        for c in conatct:
            if c.id == id:
               contact=c
               break
        if contact is None:
            raise ValueError("contact intouvable")
        if not name.strip():
            raise ValueError("the name is empty")
        if not firstname.strip():
            raise ValueError("the firstname is empty")
        
        if not phone.isdigit():
            raise ValueError("the phone number is invalid")
        

        contact.name = name
        contact.firstname = firstname
        contact.email = email
        contact.phone = phone
        self.repository.update(contact)
        return contact