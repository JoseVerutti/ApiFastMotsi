import pyrebase
import pandas as pd

# --------------------------------CREDENCIALES APP--------------------------------

firebaseConfig = {
  'apiKey': "AIzaSyDLgWpWUOSR3cZebUyOOx-nBE_25q0y2yE",
  'authDomain': "motsi-id001.firebaseapp.com",
  'databaseURL': "https://motsi-id001-default-rtdb.firebaseio.com",
  'projectId': "motsi-id001",
  'storageBucket': "motsi-id001.appspot.com",
  'messagingSenderId': "800130546268",
  'appId': "1:800130546268:web:dfbb366f25a92bf2308499",
  'measurementId': "G-VLFWHRNBQC"
}
firebase = pyrebase.initialize_app(firebaseConfig)

# --------------------------------FUNCTIONS: CONEXION BASE DATOS--------------------------------
#FUNCTION: Se utiliza para traer todos los datos de la BD a un DF
def database():
    db = firebase.database()
    estaciones = db.get()
    data = pd.DataFrame(estaciones.val())
    return data

#FUNCTION: Se utiliza para insertar los datos del usuario en el CHILD 2 que es el de los USUARIOS
def insert(data, collection):
    try:
      db = firebase.database()
      db.child(collection).set(data)
      return('Datos almacenados')
    except Exception as e:
      print('-'*40,'\n','ha ocurrido un error:', '\n', e)
      return('Error', e)

def user_identi(var):
    db = firebase.database()
    usuarios = db.child("USUARIOS").order_by_child("usuario").equal_to('{}'.format(var)).get()
    filtro = usuarios.val()
    data = pd.DataFrame(filtro)
    change = data.transpose()
    usuario = change["usuario"].tolist()
    return usuario

def usuario_equal_usuario():
  db = firebase.database()
  usuarios = db.child("USUARIOS").get()
  filtro = usuarios.val()
  data = pd.DataFrame(filtro)
  return data

def usuario_equal_contrasena():
  db = firebase.database()
  usuarios = db.child("USUARIOS").get()
  filtro = usuarios.val()
  data = pd.DataFrame(filtro)
  return data
