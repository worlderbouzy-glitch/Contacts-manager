import unittest

from src.entities.contact import Contact


class TestContact(unittest.TestCase):

    def test_create_valid_contact(self):
        contact = Contact(1, "jean", "12345678", "JEAN@MAIL.COM")

        self.assertEqual(contact.id, 1)
        self.assertEqual(contact.name, "Jean")          # .title() aplike
        self.assertEqual(contact.phone, "12345678")
        self.assertEqual(contact.email, "jean@mail.com")  # .lower() aplike

    def test_invalid_id_raises_error(self):
        with self.assertRaises(ValueError):
            Contact(0, "Jean", "12345678", "jean@mail.com")

    def test_empty_name_raises_error(self):
        with self.assertRaises(ValueError):
            Contact(1, "   ", "12345678", "jean@mail.com")

    def test_short_name_raises_error(self):
        with self.assertRaises(ValueError):
            Contact(1, "J", "12345678", "jean@mail.com")

    def test_phone_with_letters_raises_error(self):
        with self.assertRaises(ValueError):
            Contact(1, "Jean", "1234abcd", "jean@mail.com")

    def test_phone_too_short_raises_error(self):
        with self.assertRaises(ValueError):
            Contact(1, "Jean", "1234", "jean@mail.com")

    def test_invalid_email_raises_error(self):
        with self.assertRaises(ValueError):
            Contact(1, "Jean", "12345678", "jeanmail.com")  # manke '@'

    def test_to_dict(self):
        contact = Contact(1, "Jean", "12345678", "jean@mail.com")
        expected = {
            "id": 1,
            "name": "Jean",
            "phone": "12345678",
            "email": "jean@mail.com",
        }
        self.assertEqual(contact.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
