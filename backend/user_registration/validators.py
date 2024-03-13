"""
Validators using descriptors
Fields -
    f_name
    m_name
    l_name
    primary_contact_number
    secondary_contact_number
    primary_email_address
    secondary_email_address
    password
    address
    pincode
"""
import re
import os
import hashlib


class FName:
    def __init__(self):
        self.f_name = ""

    def __get__(self, instance, owner):
        return self.f_name

    def __set__(self, instance, value):
        self.validate(value)
        self.f_name = value

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("First Name should be a string")


class LName:
    def __init__(self):
        self.l_name = ""

    def __get__(self, instance, owner):
        return self.l_name

    def __set__(self, instance, value):
        self.validate(value)
        self.l_name = value

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("Last Name should be a string")


class MName:
    def __init__(self):
        self.m_name = ""

    def __get__(self, instance, owner):
        return self.m_name

    def __set__(self, instance, value):
        self.validate(value)
        self.m_name = value

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("Middle Name should be a string")


class PrimaryContactNumber:
    def __init__(self):
        self.p_c_num = ""

    def __get__(self, instance, owner):
        return self.p_c_num

    def __set__(self, instance, value):
        self.validate(value)
        self.p_c_num = value.strip().replace(" ", "")

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("Phone number should be a string")
        if len(value.strip().replace(" ", "")) != 10:
            raise ValueError("Phone number must be of 10 digits.")
        if not value.isdigit():
            raise ValueError("Phone number must be in digits.")


class SecondaryContactNumber:
    def __init__(self):
        self.s_c_num = ""

    def __get__(self, instance, owner):
        return self.s_c_num

    def __set__(self, instance, value):
        self.validate(value)
        self.s_c_num = value.strip().replace(" ", "")

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("Phone number should be a string")
        if len(value.strip().replace(" ", "")) != 10:
            raise ValueError("Phone number must be of 10 digits.")
        if not value.isdigit():
            raise ValueError("Phone number must be in digits.")


class PrimaryEmailAddress:
    def __init__(self):
        self.p_email = ""

    def __get__(self, instance, owner):
        return self.p_email

    def __set__(self, instance, value):
        self.validate(value)
        self.p_email = value

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("Email address should be a string")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.match(regex, value):
            raise ValueError("Enter a completely valid email address.")


class SecondaryEmailAddress:
    def __init__(self):
        self.s_email = ""

    def __get__(self, instance, owner):
        return self.s_email

    def __set__(self, instance, value):
        self.validate(value)
        self.s_email = value

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("Email address should be a string")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.match(regex, value):
            raise ValueError("Enter a completely valid email address.")


class Password:
    def __init__(self):
        self.p_word = ""

    def __get__(self, instance, owner):
        return self.p_word

    def __set__(self, instance, value):
        self.validate(value)
        self.p_word = self.hash_password(value.encode('utf-8'))

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("Email address should be a string")
        regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z \d@$!#%*?&]{8,20}$'
        if not re.match(regex, value):
            raise ValueError("Password must contain at least one upper case Alphabet, one lower case Alphabet,"
                             "one numerical digit and it must be 8 to 20 characters long.")

    def hash_password(self, value):
        """Hashes a password using the SHA256 algorithm.
        Args:
          value: The password to hash. (encoded)
        Returns:
          A string representing the hashed password.
        """
        hashed_password = hashlib.sha256(value).hexdigest()
        return hashed_password


class Address:
    def __init__(self):
        self.address = ""

    def __get__(self, instance, owner):
        return self.address

    def __set__(self, instance, value):
        self.validate(value)
        self.address = value

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("Address Must be string")


class Pincode:
    def __init__(self):
        self.pincode = ""

    def __get__(self, instance, owner):
        return self.pincode

    def __set__(self, instance, value):
        self.validate(value)
        self.pincode = value

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("Pin Code Must be string")
        if len(value.strip().replace(" ", "")) != 6:
            raise ValueError("Pincode must be of 8 digits.")
        if not value.isdigit():
            raise ValueError("Pincode must be in digits.")

