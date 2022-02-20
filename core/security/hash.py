""" hashing utilities """
from passlib.context import CryptContext

PWD_CONTEXT = CryptContext(schemes=['bcrypt'], deprecated='auto')


async def hash_string(plain_text: str) -> str:
    """
    hashes string to the provided context schemes

    Parameters:
    plain_text (str): string to be hashed

    Returns:
    str: hashed string of the arg
    """
    return PWD_CONTEXT.hash(plain_text)


async def verify_hash(plain_text: str, hashed_text: str) -> bool:
    """
    verify if the plain text and hashed text are equal

    Parameters:
    plain_text (str): plain string to be compared
    hashed_text (str): hashed string to be compared

    Returns:
    bool: boolean value based on comparison
    """
    return PWD_CONTEXT.verify(plain_text, hashed_text)
