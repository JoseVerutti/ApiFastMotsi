from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text, Optional
from datetime import date, datetime
import json
from database import *
from uuid import uuid4 as uniqueID

# --------------------------------------- VARIABLES ---------------------------------------
dict_usuarios= []
app = FastAPI(title="motsi",
    description="Api Rest del mvp de Motsi",
    version="0.5")
#-----------------------------Schemas------------------------------------------------------

class User(BaseModel):
    id: Optional[str]=None
    name: str
    username: str
    password: str
    email: Text
    cell_number: int
    sex: str
    created_at: Optional[str]=datetime.now()
    # profile_pic: { "id": , "url":  }
    # date_of_birth: 
    # content: Text
    # city: str
    # state_long: str
    # state_short: str
    # country_long: str
    # country_short: str


class Activiti(BaseModel):
    id: Optional[str]=None 
    idPrestador: str
    title: str
    content : str
    status: bool
    price: float
    isNegotiable: bool 
    # propertyType: 
    # condition: None
    # rating: None
    # ratingCount: None
    contactNumber: int
    # amenities: None


# --------------------------------------- ON EVENT ---------------------------------------

@app.on_event('startup')
def startup():
    #if conecction.is_closed:
    #    conecction.conecct()
    pass

# pip install virtualenv
# virtualenv env
# cd env/scripts
# activate
# pip install gunicorn pyrebase4 requests flask pandas
# pip install yagmail Flask-WTF Werkzeug Flask-Login smtplib functools


@app.on_event('startup')
def shutdown():
    pass

# --------------------------------------- RUTAS ---------------------------------------
@app.get('/')
async def index():
    return("Hola Motsi")

@app.get("/user")
async def user():
    return("user")

#----------------RUTAS: Actividades-------------------------------------------------------


@app.post("/api/activities")
#'''Ruta para crear una actividad'''
async def create_activity():
    return("Actividad creada")

@app.get("/api/activities")
#'''Ruta para mostrar las actividades'''
async def get_activity_data():
    return("Actividad obtenida")

@app.delete("/api/activities")
#'''Ruta para eliminar una actividad'''
async def delete_activity_data():
    return("Actividad eliminada")

@app.put("/api/activities")
#'''Ruta para editar una actividad'''
async def update_activity_data():
    return("Actividad editada exitosamente")

    
#----------------RUTRAS: Usuarios-------------------------------------------------------


@app.post("/api/user_t")
#'''Esta es la ruta para crear usuarios de turista'''
async def create_turist(usuario: User):
    try:
        usuario.id = str(uniqueID())
        usuario.created_at = str(datetime.now())
        dict_usuarios = (usuario.dict())
        result = insert(dict_usuarios, 'usuarios')
        return(result)
    except Exception as e:
        print('-'*40,'\n','ha ocurrido un error:', '\n', e)
@app.get("/api/user_t")
#'''Esta es la ruta para consultar la lista de usuarios'''
async def get_turist_data():
    return(lista_usuarios)

@app.get("/api/user_sp")
#'''Esta es la ruta para consultar los datos de la vista de un service provider'''
async def get_serviceProvider_data():
    return("ruta del sp")

