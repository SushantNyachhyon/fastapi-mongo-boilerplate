"""
user repository
"""
from abc import ABCMeta, abstractmethod

from .models import User


class UserAbstract:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def find_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    async def create(self, payload: dict) -> User:
        pass


class UserRepository(UserAbstract):

    def __init__(self):
        self.model = User

    async def find_by_email(self, email: str) -> User:
        return await self.model.find_one(self.model.email == email)

    async def create(self, payload: dict) -> User:
        return await self.model.insert(self.model(**payload))


def get_user_repo():
    return UserRepository()
