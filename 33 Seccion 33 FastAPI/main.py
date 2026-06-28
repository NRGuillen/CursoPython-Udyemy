import uvicorn
from fastapi import FastAPI
from routers.messages import router

app = FastAPI()

# router lo cogemos de messages importando las rutas que tenemos ahi
"""Esto sirve para acceder a los endpoints de messages, es decir, en la ulr
al poner /messages, seria el equivalente a ir al archivo messages y tener solo esas rutas,
una vez puesto /messages debemos de poner la ruta a la que queramos ir, http://127.0.0.1:8000/messages/ejemplo"""
app.include_router(router, prefix="/messages", tags=["messages"]) # los tags solo es para la documentacion y agrupar rutas por modulos, en este caso agrupadas por messages etc
@app.get('/')
def read_data():
    return {"message" : 'Mi primer endpoint en FastAPI'}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

