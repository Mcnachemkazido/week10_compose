from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from app.utils.crud import DatabaseService
from app.models.contact import Contact

class UserContact(BaseModel):
    contact_id:int | None
    first_name:str
    last_name:str
    phone_number:str

app = FastAPI()

@app.post("/contacts")
def create_contact(data:UserContact):
    try:
        object_contact = Contact(data.first_name,data.last_name,data.phone_number)
        return DatabaseService.create_contact(object_contact.contact_to_dict())
    except Exception as e:
        print(e)


@app.get("/contacts")
def get_all_contacts():
    try:
        data =  DatabaseService.get_all_contacts()
        data_list = []
        for row in data:
            object_contact = Contact(row[1],row[2],row[3],row[0])
            data_list.append(object_contact.contact_to_dict())
        return data_list
    except Exception as e:
        print(e)


@app.put("/contacts/{id}")
def update_contact(id,data:UserContact):
    try:
        object_contact = Contact(data.first_name, data.last_name, data.phone_number)
        return DatabaseService.update_contact(id,object_contact.contact_to_dict())
    except Exception as e:
        print(e)



@app.delete("/contacts/{id}")
def delete_contact(id):
    try:
        return DatabaseService.delete_contact(id)
    except Exception as e:
        print(e)