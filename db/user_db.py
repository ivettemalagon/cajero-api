from typing import Dict
from pydantic import BaseModel

#Definicion de UserInDB
class UserInDB(BaseModel):  #Herencia en Python, es el equivalente a User... extends BaseModel
    username: str   #Atributos.
    password: str   #Asi se define el tipo de dato
    balance: int

#Definicion de la base de datos ficticia
database_users = Dict[str, UserInDB]
database_users = {
    "camilo24": UserInDB(**{"username":"camilo24", #** hacen un mapeo
                            "password":"root",
                            "balance":12000}),
    "andres18": UserInDB(**{"username":"andres18",
                            "password":"hola",
                            "balance":34000}),
}

#Definicion de funciones sobre la base de datos ficticia (funcionan como getter y setter)
def get_user(username: str):    #Para obtener toda la informacion de un usuario solo con el username
    if username in database_users.keys():   
        return database_users[username]
    else:
        return None
def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db