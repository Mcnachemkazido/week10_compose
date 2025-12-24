from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from utils.CRUD import Crud
from models.contact import Contact

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
        return Crud.create_contact(object_contact.contact_to_dict())
    except Exception as e:
        print(e)


@app.get("/contacts")
def get_all_contacts():
    try:
        return Crud.get_all_contacts()
    except Exception as e:
        print(e)


@app.put("/contacts/{id}")
def update_contact(id,data:UserContact):
    try:
        object_contact = Contact(data.first_name, data.last_name, data.phone_number)
        return Crud.update_contact(id,object_contact.contact_to_dict())
    except Exception as e:
        print(e)



@app.delete("/contacts/{id}")
def delete_contact(id):
    try:
        return Crud.delete_contact(id)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)