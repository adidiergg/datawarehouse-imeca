from fastapi import FastAPI,HTTPException
import psycopg2

host = '127.0.0.1'
port = 5432
user = 'postgres'
password = '1234'
database='postgres'

app = FastAPI()

from fastapi import FastAPI
app = FastAPI()

"""

VEHICULOS

"""
 
@app.get('/getVehiclesByYear/{year}')
async def getVehiclesByYear(year:int):
    try:
        conn = psycopg2.connect(host=host,port=port,user=user,password=password,database=database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT da.periodo,de.nombre,da.numero FROM vehiculos da  INNER JOIN delegaciones de ON da.id_delegacion=de.id_delegacion WHERE da.periodo=%(year)s """,{'year':year})
        datos = cursor.fetchall()
        print(datos)
        
        if len(datos)!=0:
            resultado = []
            for i in datos:
                resultado.append({'año':i[0] ,'lugar':i[1] ,'vehiculos':i[2] })
                
            conn.close()
            return {'data':resultado}
        else:
            conn.close()
            return HTTPException(status_code=404, detail="no se encontro el recurso")
    except:
        return HTTPException(status_code=500, detail="Error de conexion con la base de datos")
    


@app.get('/getVehiclesByPlace/{place}')
async def getVehiclesByPlace(place:int):
    try:
        conn = psycopg2.connect(host=host,port=port,user=user,password=password,database=database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT da.periodo,de.nombre,da.numero FROM vehiculos da  INNER JOIN delegaciones de ON da.id_delegacion=de.id_delegacion WHERE da.id_delegacion=%(place)s """,{'place':place})
        datos = cursor.fetchall()
        delegacion = ""
        print(datos)
        if len(datos)!=0:
            resultado = []
            for i in datos:
                resultado.append({'año':i[0] ,'vehiculos':i[2] })
                delegacion=i[1]
            conn.close()
            return {'lugar':delegacion ,'data':resultado}
        else:
            conn.close()
            return HTTPException(status_code=404, detail="no se encontro el recurso")
    except:
        return HTTPException(status_code=500, detail="Error de conexion con la base de datos")
    
    
@app.get('/getAllVehicles/')
async def getAllVehicles():
    try:
        conn = psycopg2.connect(host=host,port=port,user=user,password=password,database=database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT da.periodo,de.nombre,da.numero FROM vehiculos da  INNER JOIN delegaciones de ON da.id_delegacion=de.id_delegacion """)
        datos = cursor.fetchall()
        delegacion = ""
        print(datos)
        if len(datos)!=0:
            resultado = []
            for i in datos:
                resultado.append({'año':i[0] ,'lugar':i[1],'vehiculos':i[2] })
                delegacion=i[1]
            conn.close()
            return {'data':resultado}
        else:
            conn.close()
            return HTTPException(status_code=404, detail="no se encontro el recurso")
    except:
        return HTTPException(status_code=500, detail="Error de conexion con la base de datos")
    
    
"""

ACCIDENTES

"""

@app.get('/getAccidentsByYear/{year}')
async def getAccidentsByYear(year:int):
    try:
        conn = psycopg2.connect(host=host,port=port,user=user,password=password,database=database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT da.periodo,de.nombre,da.numero FROM accidentes da  INNER JOIN delegaciones de ON da.id_delegacion=de.id_delegacion WHERE da.periodo=%(year)s """,{'year':year})
        datos = cursor.fetchall()
        print(datos)
        
        if len(datos)!=0:
            resultado = []
            for i in datos:
                resultado.append({'año':i[0] ,'lugar':i[1] ,'accidentes':i[2] })
                
            conn.close()
            return {'data':resultado}
        else:
            conn.close()
            return HTTPException(status_code=404, detail="no se encontro el recurso")
    except:
        return HTTPException(status_code=500, detail="Error de conexion con la base de datos")
    


@app.get('/getAccidentsByPlace/{place}')
async def getAccidentsByPlace(place:int):
    try:
        conn = psycopg2.connect(host=host,port=port,user=user,password=password,database=database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT da.periodo,de.nombre,da.numero FROM accidentes da  INNER JOIN delegaciones de ON da.id_delegacion=de.id_delegacion WHERE da.id_delegacion=%(place)s """,{'place':place})
        datos = cursor.fetchall()
        delegacion = ""
        print(datos)
        if len(datos)!=0:
            resultado = []
            for i in datos:
                resultado.append({'año':i[0] ,'accidentes':i[2] })
                delegacion=i[1]
            conn.close()
            return {'lugar':delegacion,'data':resultado}
        else:
            conn.close()
            return HTTPException(status_code=404, detail="no se encontro el recurso")
    except:
        return HTTPException(status_code=500, detail="Error de conexion con la base de datos")
    
    
@app.get('/getAllAccidents/')
async def getAllAccidents():
    try:
        conn = psycopg2.connect(host=host,port=port,user=user,password=password,database=database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT da.periodo,de.nombre,da.numero FROM accidentes da  INNER JOIN delegaciones de ON da.id_delegacion=de.id_delegacion """)
        datos = cursor.fetchall()
        delegacion = ""
        print(datos)
        if len(datos)!=0:
            resultado = []
            for i in datos:
                resultado.append({'año':i[0] ,'lugar':i[1],'accidentes':i[2] })
                delegacion=i[1]
            conn.close()
            return {'data':resultado}
        else:
            conn.close()
            return HTTPException(status_code=404, detail="no se encontro el recurso")
    except:
        return HTTPException(status_code=500, detail="Error de conexion con la base de datos")
    
   