from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from models.CRUD import Crud

class Contact(BaseModel):
    first_name:str
    last_name:str
    phone_number:str

app = FastAPI()

@app.post("/contacts")
def create_contact(data:Contact):
    return Crud.create_contact(data)


@app.get("/contacts")
def get_all_contacts():
    return Crud.get_all_contacts()


@app.put("/contacts/{id}")
def update_contact(id,data:Contact):
    return Crud.update_contact(id,data)


@app.delete("/contacts/{id}")
def delete_contact(id):
    return Crud.delete_contact(id)



if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)