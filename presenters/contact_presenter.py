class ContactPresenter:
   
    @staticmethod
    def show_contact(contact):
        print("----------------")
        print("ID    :", contact.id)
        print("Name  :", contact.name)
        print("Phone :", contact.phone)
        print("Email :", contact.email)

    @staticmethod
    def show_contact_list(contacts):
        if len(contacts) == 0:
            print("No contacts found.")
            return

        print("\nList of contacts:")

        for contact in contacts:
            ContactPresenter.show_contact(contact)

    @staticmethod
    def show_success(message):
        print("✅", message)

    @staticmethod
    def show_error(message):
        print("❌ Error:", message)
