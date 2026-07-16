import unittest

from use_cases.create_contact import CreateContact


class FakeRepository:
   
    def __init__(self):
        self.contacts = []

    def add(self, contact):
        self.contacts.append(contact)

    def find_by_phone(self, phone):
        for contact in self.contacts:
            if contact.phone == phone:
                return contact
        return None


class TestCreateContact(unittest.TestCase):

    def setUp(self):
       
        self.repository = FakeRepository()
        self.create_contact = CreateContact(self.repository)

    def test_create_contact_success(self):
        contact = self.create_contact.execute(1, "Jean", "12345678", "jean@mail.com")

        self.assertEqual(contact.name, "Jean")
        self.assertEqual(len(self.repository.contacts), 1)

    def test_create_contact_empty_name_raises_error(self):
        with self.assertRaises(ValueError):
            self.create_contact.execute(1, "   ", "12345678", "jean@mail.com")

    def test_create_contact_invalid_phone_raises_error(self):
        with self.assertRaises(ValueError):
            self.create_contact.execute(1, "Jean", "abc", "jean@mail.com")

    def test_create_contact_invalid_email_raises_error(self):
        with self.assertRaises(ValueError):
            self.create_contact.execute(1, "Jean", "12345678", "jeanmail.com")

    def test_create_contact_duplicate_phone_raises_error(self):
        self.create_contact.execute(1, "Jean", "12345678", "jean@mail.com")

        with self.assertRaises(ValueError):
            self.create_contact.execute(2, "Pierre", "12345678", "pierre@mail.com")


if __name__ == "__main__":
    unittest.main()
