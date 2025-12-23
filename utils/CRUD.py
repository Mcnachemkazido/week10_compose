from db.connection import Connection

class Crud:

    @staticmethod
    def create_contact(data):
        coon = Connection().get_connection()
        cursor = coon.cursor()
        cursor.execute("""
        INSERT INTO contacts 
        (id,first_name, last_name, phone_number) 
        VALUES (%s,%s,%s,%s) """
        ,(data["contact_id"],data["first_name"],data["last_name"],data["phone_number"]))

        new_id = cursor.lastrowid
        coon.commit()
        cursor.close()
        coon.close()
        return {"message": "Contact created successfully","id":new_id}


    @staticmethod
    def get_all_contacts():
        coon = Connection().get_connection()
        cursor = coon.cursor()
        cursor.execute("""SELECT * FROM contacts""")
        result = cursor.fetchall()
        cursor.close()
        coon.close()
        return result


    @staticmethod
    def update_contact(item_id: int,data):
        coon = Connection().get_connection()
        cursor = coon.cursor()
        cursor.execute(f"""
                UPDATE contacts
                SET id = %s ,first_name = %s ,last_name = %s ,phone_number = %s
                WHERE id  = %s """,
                (item_id,data["first_name"],data["last_name"],data["phone_number"],item_id))
        coon.commit()
        cursor.close()
        cursor.close()
        return {"message":"true"}


    @staticmethod
    def delete_contact(item_id: int):
        coon = Connection().get_connection()
        cursor = coon.cursor()
        cursor.execute("""DELETE FROM contacts
                            WHERE id = %s""",(item_id,))
        coon.commit()
        cursor.close()
        coon.close()
        return {"message":"true"}



print(Crud.get_all_contacts())



















