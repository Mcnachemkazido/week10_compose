
class Contact:
    def __init__(self,first_name: str,last_name: str,phone_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def get_contact(self):
        return {
            "first_name":self.first_name,
            "last_name":self.last_name,
            "phone_number":self.phone_number
        }

