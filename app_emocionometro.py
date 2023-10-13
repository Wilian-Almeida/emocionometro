#POST para Respostas
#URL: https://emocionometer02-default-rtdb.firebaseio.com/
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("build\emocionometer02-firebase-adminsdk-r0099-6993e0616a.json")
firebase_admin.initialize_app(cred)

from firebase_admin import db

ref = db.reference('https://emocionometer02-default-rtdb.firebaseio.com/Respostas')
data = ref.get()
print(data)
