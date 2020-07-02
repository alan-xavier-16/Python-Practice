import re


class Contact:
    """A class for a single contact"""

    def __init__(self, auto=False):
        """Contact details"""
        if not auto:
            self._get_contact_input()
        else:
            self.name = auto["name"]
            self.phone = auto["phone"]
            self.email = auto["email"]

    def to_dict(self):
        """Convert to a dictionary"""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

    def show_self(self):
        """Show a printout of contact"""
        print(
            f"name: {self.name}, phone: {self.phone}, email: {self.email}")

    def update(self):
        """Update contact details"""
        self.show_self()
        self._get_contact_input()
        return self

    def _get_contact_input(self, name="", phone="", email=""):
        """Validate contact details before returning Contact object"""
        while True:
            # Regex
            phone_re = "\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}"
            email_re = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

            # User Inputs
            name = input("Name: ")
            phone = input("Phone Number: ")
            email = input("Email Address: ")
            try:
                if len(name) == 0:
                    raise Exception(f"Name is required")
                elif not re.search(phone_re, phone):
                    raise Exception(f"{phone} is an invalid phone number")
                elif not re.search(email_re, email):
                    raise Exception(f"{email} is an invalid email")
            except Exception as err:
                print(
                    f"Exception Type: {type(err).__name__}\nError: {err}")
            else:
                self.name = name
                self.phone = phone
                self.email = email
                break
