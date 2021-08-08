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
    description="Api Rest del primer mvp de Motsi",
    version="0.5")


#-----------------------------Schemas------------------------------------------------------

class Service_provider(BaseModel):
    '''Esquema que gestiona los datos del prestador de servicios '''
    id: Optional[str] 
    firstName: str
    lastName: str
    email: Text
    username: str
    password: str
    # description:str
    # cell_number: int
    # sex: str
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
    '''  Esquema que gestiona los datos de los turistas    '''
    id: Optional[str]=None
    name: str
    description:str
    username: str
    password: str
    email: Text
    cell_number: int
    sex: bool
    created_at: datetime = datetime.now()

class Location(BaseModel):
    '''     Esquema que gestiona las Ubicaciones de las actividades    '''
    Activity_id:Optional[str]=None
    Country: str
    city: str
    postalcode: Optional[int]
    is_location_exact: bool
    latitud:float
    longitud:float
    altitud: Optional[float]=None



class Activity(BaseModel):
    '''  Esquema que gestiona las actividad o experiencia turistica   '''
    id: Optional[str]=None
    title: str
    description:str
    price: float

    # provider_id: Optional[str]=None
    # title: str
    # description:str
    # content : str
    # status: bool
    # price: float
    # isNegotiable: bool 
    # contactNumber: int
    # propertyType: 
    # condition: None
    # rating: None
    # ratingCount: None
    # amenities: None

class Amenities(BaseModel):
    ''' Esquema que gestiona los implementos "Plus" de las actividades    '''
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
    ''' Esquema que gestiona las Archivos multimedia de los usuarios   '''
    user_id: Optional[str]=None
    type: str

class MediaFile_Activity(BaseModel):
    '''  Esquema que gestiona los Archivos multimedia de las actividades   '''
    Activity_id: Optional[str]=None
    type:str

class reservations(BaseModel):
    '''  Esquema que gestiona las reservas de actividades del turista   '''
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


@app.post("/api/activity")
async def create_activity(activity: Activity):
    '''Ruta para crear una actividad'''
    activity.id = 'activity1'
    dict_activity = (activity.dict())
    result = genericInsertBD(dict_activity, 'actividades')
    return("Actividad creada")

@app.get("/api/activity")
async def get_activity_data():
    '''Ruta para mostrar las actividades'''
    return("Actividad obtenida")

@app.delete("/api/activity")
async def delete_activity_data():
    '''Ruta para eliminar una actividad'''
    return("Actividad eliminada")

@app.put("/api/activity")
async def update_activity_data():
    '''Ruta para editar una actividad'''
    return("Actividad editada exitosamente")

    
#----------------GIANPIER -------------------------------------------------------
#----------------GIANPIER -------------------------------------------------------


@app.post("/api/user_POST/")
async def create_turist(usuario: Turist):
    '''Esta es la ruta para crear usuarios de turista'''
    try:
        usuario.id = str(uniqueID())
        usuario.created_at = str(datetime.now())
        dict_usuarios = (usuario.dict())
        result = insertBD(dict_usuarios, 'usuarios')
        return(result)
    except Exception as e:
        print('-'*40,'\n','ha ocurrido un error:', '\n', e)

class userGet(BaseModel):
    userName:str


@app.get("/api/user_GET/")
async def create_turist(usuario: userGet):
    '''Esta es la ruta para obtener usuarios'''
    try:
        print('hizo get')
        response = obtenerBD("usuarios", usuario.userName)
        return(response)

    except Exception as e:
        print('-'*40,'\n','ha ocurrido un error:', '\n', e)


#----------------RUTAS: Usuarios turista-------------------------------------------------------

@app.get("/api/user_t/{user_id}")
async def get_turist_data(user_id):
    '''Esta es la ruta para consultar la lista de usuarios'''
    user= dict_usuarios.select().where(dict_usuarios.id== user_id).first()
    if user:
        print(user)
    else:
        print("User not found")

@app.delete("/api/user_t/{user_id}")

async def delete_turist_data(user_id):
    '''Esta es la ruta para Eliminar un usuario'''
    try:
        pass
    except Exception as e:
        print('-'*40,'\n','ha ocurrido un error:', '\n', e)

@app.put("/api/user_t/{user_id}")

async def update_turist_data(user_id):
    '''Esta es la ruta para actualizar la lista de usuarios'''
    try:
        pass
    except Exception as e:
        print('-'*40,'\n','ha ocurrido un error:', '\n', e)


#----------------RUTAS: Usuarios prestador de servicios-------------------------------------------------------


@app.post("/api/user_sp/")

async def create_Service_provider(usuario: Service_provider):
    '''Esta es la ruta para crear usuarios de Service_provider'''
    try:
        usuario.id = str(uniqueID())
        usuario.created_at = str(datetime.now())
        dict_usuarios = (usuario.dict())
        result = insert(dict_usuarios, 'usuarios')
        return(result)
    except Exception as e:
        print('-'*40,'\n','ha ocurrido un error:', '\n', e)

@app.get("/api/user_sp/{user_id}")

async def get_Service_provider_data(user_id):
    '''Esta es la ruta para consultar la lista de Service_provider'''
    user= dict_usuarios.select().where(dict_usuarios.id== user_id).first()
    if user:
        print(user)
    else:
        print("User not found")

@app.delete("/api/user_sp/{user_id}")
async def delete_Service_provider_data(user_id):
    '''Esta es la ruta para eliminar de la lista un Service_provider'''
    try:
        pass
    except Exception as e:
        print('-'*40,'\n','ha ocurrido un error:', '\n', e)

@app.put("/api/user_sp/{user_id}")
async def update_Service_provider_data(user_id):
    '''Esta es la ruta para actualizar los datos de Service_provider'''
    try:
        pass
    except Exception as e:
        print('-'*40,'\n','ha ocurrido un error:', '\n', e)

