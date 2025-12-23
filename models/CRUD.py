from connection import Connection

class Crud:

    @staticmethod
    def create_contact(first_name: str, last_name: str, phone_number: str):
        coon = Connection().get_connection()
        cursor = coon.cursor()
        cursor.execute("""
        INSERT INTO contacts 
        (first_name, last_name, phone_number) 
        VALUES (%s,%s,%s) """,(first_name,last_name,phone_number))
        coon.commit()
        cursor.close()
        coon.close()
        return {"message": "Contact created successfully"}

    @staticmethod
    def get_all_contacts():
        coon = Connection().get_connection()
        cursor = coon.cursor()
        cursor.execute("""SELECT * FROM contacts""")
        result = cursor.fetchall()
        cursor.close()
        coon.close()
        return result



print(Crud.get_all_contacts())












