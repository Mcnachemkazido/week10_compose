from db.connection import Database

class DatabaseService:

    @staticmethod
    def create_contact(data: dict[str,str|int]) -> dict[str,str|int]:
        coon = Database().get_connection()
        cursor = coon.cursor()
        cursor.execute("""
        INSERT INTO contacts 
        (first_name, last_name, phone_number) 
        VALUES (%s,%s,%s) """
        ,(data["first_name"],data["last_name"],data["phone_number"]))

        new_id = cursor.lastrowid
        coon.commit()
        cursor.close()
        coon.close()
        return {"message": "Contact created successfully","id":new_id}


    @staticmethod
    def get_all_contacts() -> list[list[str|int]]:
        coon = Database().get_connection()
        cursor = coon.cursor()
        cursor.execute("""SELECT * FROM contacts""")
        result = cursor.fetchall()
        cursor.close()
        coon.close()
        return result


    @staticmethod
    def update_contact(item_id: int,data: dict[str,str|int]) -> dict[str,bool]:
        coon = Database().get_connection()
        cursor = coon.cursor()
        cursor.execute(f"""
                UPDATE contacts
                SET first_name = %s ,last_name = %s ,phone_number = %s
                WHERE id  = %s """,
                (data["first_name"],data["last_name"],data["phone_number"],item_id))
        coon.commit()
        cursor.close()
        cursor.close()
        return {"message":True}


    @staticmethod
    def delete_contact(item_id: int) -> dict[str,bool]:
        coon = Database().get_connection()
        cursor = coon.cursor()
        cursor.execute("""DELETE FROM contacts
                            WHERE id = %s""",(item_id,))
        coon.commit()
        cursor.close()
        coon.close()
        return {"message":True}



















