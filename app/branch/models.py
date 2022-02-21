"""
branch models
"""
from core.models import DocumentFactory


class Branch(DocumentFactory):
    """
    branch document class
    """

    class Collection:
        name = 'branches'
