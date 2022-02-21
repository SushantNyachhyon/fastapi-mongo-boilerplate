"""
branch repository
"""
from abc import ABCMeta, abstractmethod

from .models import Branch


class BranchAbstract:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def find_by_id(self, branch_id: str):
        pass


class BranchRepository(BranchAbstract):
    def __init__(self):
        self.model = Branch

    async def find_by_id(self, branch_id: str):
        pass
