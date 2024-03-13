import os
import hashlib


def hash_password(password):
    """Hashes a password using the SHA256 algorithm.
    Args:
      password: The password to hash.
    Returns:
      A string representing the hashed password.
    """
    salt = os.urandom(8).hex()
    hashed_password = hashlib.sha256(salt+password).hexdigest()
    return hashed_password


def verify_password(password):
    # TDB
    ...
