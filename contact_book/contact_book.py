import os
import pandas as pd
from contact import Contact


class ContactBook:
    """Overall class for managing contacts"""

    def __init__(self):
        """Initialize a contact book"""
        self.contacts = []
        self._get_book_details()
        self._get_contacts_list()

    def _check_existing(self):
        """Check if contact book exists in a CSV file"""
        try:
            if not os.path.exists(self.save_path):
                return False
            else:
                return True
        except Exception as err:
            print(
                f"Exception: {type(err).__name__}\nError: {err}")

    def _get_contacts_list(self):
        """Create contact list from Pandas DataFrame if existing"""
        try:
            if self._check_existing():
                contacts_df = pd.read_csv(self.save_path, index_col=0)
                for row_label, row in contacts_df.iterrows():
                    auto = {
                        "name": row["name"], "phone": row["phone"], "email": row["email"]}
                    self.add_contact(auto)
        except Exception as err:
            print(
                f"Exception: {type(err).__name__}\nError: {err}")

    def _get_book_details(self):
        """Get contact book details"""
        user = input("What is your name?: ")
        try:
            if len(user) == 0:
                raise Exception(f"A search parameter is required")
        except Exception as err:
            print(
                f"Exception Type: {type(err).__name__}\nError: {err}")
        else:
            self.user = user.lower()
            self.name = f"{self.user}.csv"
            self.save_path = os.path.join(os.getcwd(), self.name)

    def run_program(self):
        """Start main contact book loop"""
        command_str = "Starting...\nNote the following commands:\n\tSA - Shows all contacts,\n\tSO - Show specific contact,\n\tA - Add new contact,\n\tU - Update contact\n\tR - Remove contact\n\tQ - Exit"
        print(command_str, end="\n\n")

        while True:
            user_input = input("What would you like to do?: ")
            if user_input.lower() == "sa":
                self.show_contacts()
            elif user_input.lower() == "so":
                self.show_contact()
            elif user_input.lower() == "a":
                self.add_contact()
            elif user_input.lower() == "u":
                self.update_contact()
            elif user_input.lower() == "r":
                self.remove_contact()
            elif user_input.lower() == "q":
                self.save_to_sheet()
                break
            else:
                print("Command is invalid")

    def show_contacts(self):
        """Show contact book"""
        if not self.contacts:
            print("Contact list is empty", end="\n\n")
        else:
            print("Displaying ALL contacts")
            for contact in self.contacts:
                contact.show_self()
            print()

    def show_contact(self):
        """Show requested contact"""
        try_again = True
        while try_again:
            contact = self._find_contact()
            if contact:
                print(f"Contact found")
                contact.show_self()
                try_again = False
            else:
                try_again = input("Contact not found, try again? (y/n): ")
                if try_again.lower() == "n":
                    try_again = False

    def _find_contact(self):
        """Find existing contact"""
        detail = input("Contact name, phone or email to search for:  ")
        try:
            if len(detail) == 0:
                raise Exception(f"A search parameter is required")
        except Exception as err:
            print(
                f"Exception: {type(err).__name__}\nError: {err}")
        else:
            for contact in self.contacts:
                for key, value in contact.to_dict().items():
                    if value == detail:
                        return contact

    def add_contact(self, auto=False):
        """Add new contact to list"""
        # Verify contact information
        if not auto:
            new_contact = Contact()
        else:
            new_contact = Contact(auto)
        try:
            self.contacts.append(new_contact)
            print(f"{new_contact.name} added", end="\n\n")
        except Exception as err:
            print(f"Exception Type: {type(err).__name__}")

    def remove_contact(self):
        """Remove contact from list"""
        try_again = True
        while try_again:
            contact_to_remove = self._find_contact()
            if contact_to_remove:
                self.contacts = [
                    contact for contact in self.contacts if contact != contact_to_remove]
                try_again = False
                print("Contact removed...", end="\n\n")
            else:
                try_again = input("Contact not found, try again? (y/n): ")
                if try_again.lower() == "n":
                    try_again = False

    def update_contact(self):
        """Update existing contact"""
        try_again = True
        while try_again:
            contact_to_update = self._find_contact()
            if contact_to_update:
                self.contacts = [
                    contact.update() if contact == contact_to_update else contact for contact in self.contacts]
                print("Contact updated...", end="\n\n")
                try_again = False
            else:
                try_again = input("Contact not found, try again? (y/n): ")
                if try_again.lower() == "n":
                    try_again = False

    def save_to_sheet(self):
        """Save to CSV file"""
        try:
            # Create Pandas DataFrame
            contacts_df = self._create_dataframe()

            # Create a Series for each contact & append to dataframe
            idx = 0
            for contact in self.contacts:
                new_contact = pd.Series(
                    data=[contact.name, contact.phone, contact.email], index=contact.to_dict().keys(), name=idx)
                idx += 1
                contacts_df = contacts_df.append(new_contact)

            # Save to file
            contacts_df.to_csv(self.save_path)
        except Exception as err:
            print(
                f"Exception: {type(err).__name__}\nError: {err}")
        else:
            pass

    def _create_dataframe(self):
        """Create Empty Pandas DataFrame"""
        try:
            data = {
                "name": [],
                "phone": [],
                "email": []
            }
            return pd.DataFrame(data=data)
        except Exception as err:
            print(
                f"Exception: {type(err).__name__}\nError: {err}")


if __name__ == "__main__":
    # Make an instance of contact book & run commands
    book = ContactBook()
    book.run_program()
