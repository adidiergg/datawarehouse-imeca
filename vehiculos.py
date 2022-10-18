import petl as etl
import psycopg2
import numpy as np

#datos de conexion base de datos
host = '127.0.0.1'
port = 5432
user = 'postgres'
password = '1234'
database = 'postgres'

#extracion de informacion

vehiculo = etl.fromxlsx("e/vehiculos_00.xlsx")

#remover desde 1980 a 2009
remover_year = etl.cutout(vehiculo,'1980')
for i in range(1981,2010):
    remover_year = etl.cutout(remover_year,str(i))
    
#remover columnas innecesarias
remover_columnas = etl.cutout(remover_year,'cve_municipio')
remover_columnas = etl.cutout(remover_columnas,'unidad_medida')
remover_columnas = etl.cutout(remover_columnas,'indicador')
remover_columnas = etl.cutout(remover_columnas,'id_indicador')
#print(etl.header(remover_columnas))
#print(remover_columnas)

#seleccionar filas con el identificador de la CDMX
solo_cdmx = etl.select(remover_columnas,lambda tabla: tabla.cve_entidad=='09' and (tabla.desc_municipio!='Estatal' or tabla.desc_municipio!='Otros estados') )
solo_cdmx = etl.select(solo_cdmx,lambda tabla: tabla.desc_municipio!='Estatal')
solo_cdmx = etl.select(solo_cdmx,lambda tabla: tabla.desc_municipio!='Otros estados')

#solo_cdmx = etl.selectisnot(solo_cdmx,field='desc_municipio',value=' Otros estados')
#solo_cdmx1 = etl.selectisnot(solo_cdmx,field='desc_municipio',value="Estatal")
#print(etl.nrows(solo_cdmx))
#print(etl.tail(solo_cdmx))
convertir = etl.convertnumbers(solo_cdmx)

remover_columnas = etl.cutout(convertir,'cve_entidad')
remover_columnas = etl.cutout(remover_columnas,'desc_entidad')

convertir_array = etl.toarray(remover_columnas)

#datos = [tuple(('periodo','delegacion','numero'))]
datos = []
for i,v in enumerate(convertir_array):
    datos.append((2010,i+1,v[1]))
    datos.append((2011,i+1,v[2]))
    datos.append((2012,i+1,v[3]))
    datos.append((2013,i+1,v[4]))
    datos.append((2014,i+1,v[5]))
    datos.append((2015,i+1,v[6]))
    datos.append((2016,i+1,v[7]))
    datos.append((2017,i+1,v[8]))
    datos.append((2018,i+1,v[9]))
    datos.append((2019,i+1,v[10]))
    datos.append((2020,i+1,v[11]))
    datos.append((2021,i+1,v[12]))

x = np.array(datos,dtype='int,int,int')
nuevo_formato = etl.fromarray(x)
cambiar_header = etl.setheader(nuevo_formato,['periodo','id_delegacion','numero'])
convertir_numeros = etl.convertnumbers(cambiar_header)

conexion = psycopg2.connect(database=database, 
                            user=user, password=password,
                            host=host, port=port)
etl.todb(convertir_numeros, conexion, 'vehiculos')