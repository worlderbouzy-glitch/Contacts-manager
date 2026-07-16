from src.entities.contact import Contact

from tests import test_contact
from use_cases.create_contact import CreateContact
from use_cases.list_contact import ListContacts
from use_cases.delete_contact import DeleteContact
from presenters.contact_presenter import ContactPresenter
from interfaces.contact_repository import ContactRepository
from infrastructure.contact_repository_impl import ContactRepositoryImpl


def main():

    repository = ContactRepositoryImpl()

    create_contact = CreateContact(repository)
    list_contacts = ListContacts(repository)
    delete_contact = DeleteContact(repository)


    while True:

        print("\n===== GESTION CONTACTS =====")
        print("1. add contact")
        print("2. list contacts")
        print("3. delete contact")
        print("4. exit")


        choix = input("Choose an option : ")


        if choix == "1":

            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")

            contact_id = repository.count() + 1

            try:
                create_contact.execute(contact_id, name, phone, email)
                ContactPresenter.show_success("Contact added successfully!")
                ContactPresenter.show_contact(test_contact)
                print("Contact added successfully!")

            except ValueError as e:
                ContactPresenter.show_error(str(e))


        elif choix == "2":

            contacts = list_contacts.execute()

            if len(contacts) == 0:
                ContactPresenter.show_error("No contacts found.")

            else:
                print("\nList of contacts:")

                for contact in contacts:
                    print("----------------")
                    print("id :", contact.id)
                    print("Name :", contact.name)
                    print("Phone :", contact.phone)
                    print("Email :", contact.email)



        elif choix == "3":

            phone = input(
                "Enter the phone number of the contact to delete : "
            )

            delete_contact.execute(phone)

            print("Contact deleted.")



        elif choix == "4":

            print("Goodbye!")
            break


        else:
            print("Invalid choice!")



if __name__ == "__main__":
    main()
