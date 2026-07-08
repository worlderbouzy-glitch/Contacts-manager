

class CreateContact:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, contact, id, name, firstname, email, phone):
        self.repository.create(contact, id, name, firstname, email, phone)
        if not name.strip():
            raise ValueError("the name is empty")
        if not firstname.strip():
            raise ValueError("the firstname is empty")
        if "@" not in email:
            raise ValueError("the email is empty")
        if not phone.isdigit():
            raise ValueError("the phone number is invalid")
        if len(phone)<8:
            raise ValueError("the number is too short")
        
        contact = self.repository.get_all()
         
        for contact in contact:
            if contact.name == name and contact.firstname == firstname:
                raise ValueError("the contact already exists")

        from entities.contact import Contact      
        new_contact = Contact(id, name, firstname, email, phone)

        self .repository.create(new_contact)
        return new_contact    