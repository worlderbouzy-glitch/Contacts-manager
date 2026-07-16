

from abc import ABC, abstractmethod


class ContactRepository(ABC):

    @abstractmethod
    def add(self, contact):
        pass

    @abstractmethod
    def get_by_id(self, contact_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, contact):
        pass

    @abstractmethod
    def delete(self, contact_id):
        pass

    @abstractmethod
    def find_by_name(self, name):
        pass

    @abstractmethod
    def find_by_phone(self, phone):
        pass

    @abstractmethod
    def find_by_email(self, email):
        pass

    @abstractmethod
    def exists(self, contact_id):
        pass

    @abstractmethod
    def count(self):
        pass