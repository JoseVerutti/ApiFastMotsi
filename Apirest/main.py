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

class Service_provider(BaseModel):
    id: Optional[str]
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

class Turist(BaseModel):
    id: Optional[str]=None
    name: str
    username: str
    password: str
    email: Text
    cell_number: int
    sex: bool
    created_at: datetime = datetime.now()

class Location(BaseModel):

    Activity_id:Optional[str]=None
    Country: str
    city: str
    postalcode: int
    is_location_exact: bool
    latitud:float
    longitud:float
    #altitud: Optional(float)=None



class Activiti(BaseModel):
    id: Optional[str]=None
    provider_id: Optional[str]=None
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

class Amenities(BaseModel):
    Activity_id: Optional[str]=None
    bebederos:bool
    alimentadores:bool
    capas:bool
    botas:bool
    binoculares:bool
    cafetera:bool
    tetera:bool
    senderos:bool
    casetas_de_avistamiento:bool
    fichas_de_aves_del_sitio:bool
    guia_de_avisturismo:bool

class MediaFile_User(BaseModel):
    user_id: Optional[str]=None
    type: str

class MediaFile_Activiti(BaseModel):
    Activity_id: Optional[str]=None
    type:str

class reservations(BaseModel):
    turist_id: Optional[str]=None
    Activity_id:Optional[str]=None
    state:str
    start: datetime
    end: datetime


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


@app.post("/api/user_t/")
#'''Esta es la ruta para crear usuarios de turista'''
async def create_turist(usuario: Turist):
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
async def get_turist_data(user_id):
    #user= lista_usuarios.select().where(lista_usuarios.id== user_id).first()
    user= dict_usuarios.select().where(dict_usuarios.id== user_id).first()

    if user:
        print(user)
    else:
        print("User not found")

@app.get("/api/user_sp")
#'''Esta es la ruta para consultar los datos de la vista de un service provider'''
async def get_serviceProvider_data():
    return("ruta del sp")

