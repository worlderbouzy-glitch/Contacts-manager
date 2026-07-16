
from abc import ABC, abstractmethod


class GroupRepository(ABC):

    @abstractmethod
    def add(self, group):
        pass

    @abstractmethod
    def get_by_id(self, group_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, group):
        pass

    @abstractmethod
    def delete(self, group_id):
        pass

    @abstractmethod
    def find_by_name(self, name):
        pass

    @abstractmethod
    def exists(self, group_id):
        pass

    @abstractmethod
    def count(self):
        pass