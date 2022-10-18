from xml.dom import NotFoundErr
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
accidente = etl.fromcsv("d/INEGI_exporta_13_10_2022_22_45_51.csv",encoding='latin-1',delimiter=",")
skip_rows = etl.skip(accidente,7)
solo_cdmx = etl.cut(skip_rows,0,' Azcapotzalco',' Coyoacán',
    ' Cuajimalpa de Morelos',' Gustavo A. Madero' ,' Iztacalco' ,' Iztapalapa',
    ' La Magdalena Contreras',' Milpa Alta' ,' Álvaro Obregón',' Tláhuac',' Tlalpan',
     ' Xochimilco',' Benito Juárez' ,' Cuauhtémoc' , ' Miguel Hidalgo' ,
     ' Venustiano Carranza'
)
eliminar_none = etl.selectisnot(solo_cdmx,field=' ',value=None)
cambiar_header = etl.setheader(eliminar_none,['year','Azcapotzalco','Coyoacán',
    'Cuajimalpa de Morelos','Gustavo A. Madero' ,'Iztacalco' ,'Iztapalapa',
    'La Magdalena Contreras','Milpa Alta' ,'Álvaro Obregón','Tláhuac','Tlalpan',
     'Xochimilco','Benito Juárez' ,'Cuauhtémoc' , 'Miguel Hidalgo' ,
     'Venustiano Carranza'])

sin_comentarios = etl.skipcomments(cambiar_header,'FUENTE: INEGI. Estadísticas de accidentes de tránsito terrestre en zonas urbanas y suburbanas.')

#... table8 = etl.convert(table1, ('foo', 'bar', 'baz'), str)
convertir_year = etl.convert(sin_comentarios,{'year':int,
    'Azcapotzalco':lambda v: int(v.replace(",",'')),
    'Coyoacán':lambda v: int(v.replace(",",'')),
    'Cuajimalpa de Morelos':lambda v: int(v.replace(",",'')),
    'Gustavo A. Madero':lambda v: int(v.replace(",",'')),
    'Iztacalco':lambda v: int(v.replace(",",'')),
    'Iztapalapa':lambda v: int(v.replace(",",'')),
    'La Magdalena Contreras':lambda v: int(v.replace(",",'')),
    'Milpa Alta':lambda v: int(v.replace(",",'')),
    'Álvaro Obregón':lambda v: int(v.replace(",",'')),
    'Tláhuac':lambda v: int(v.replace(",",'')),
    'Tlalpan':lambda v: int(v.replace(",",'')),
     'Xochimilco':lambda v: int(v.replace(",",'')),
     'Benito Juárez':lambda v: int(v.replace(",",'')),
     'Cuauhtémoc':lambda v: int(v.replace(",",'')),
     'Miguel Hidalgo':lambda v: int(v.replace(",",'')),
     'Venustiano Carranza':lambda v: int(v.replace(",",''))
                                              })

#convertir_year = etl.convertnumbers(sin_comentarios)

seleccionar_year = etl.select(convertir_year,lambda tabla: tabla.year in range(2010,2022))

#print(seleccionar_year)

convertir_array = etl.toarray(seleccionar_year)

delegaciones = {
    'Azcapotzalco':1,
    'Coyoacán':2,
    'Cuajimalpa de Morelos':3,
    'Gustavo A. Madero':4,
    'Iztacalco':5,
    'Iztapalapa':6,
    'La Magdalena Contreras':7,
    'Milpa Alta':8,
    'Álvaro Obregón':9,
    'Tláhuac':10,
    'Tlalpan':11,
     'Xochimilco':12,
     'Benito Juárez':13,
     'Cuauhtémoc':14,
     'Miguel Hidalgo':15,
     'Venustiano Carranza':16
}
datos = []

for i in convertir_array:
    datos.append((i[0],1,i[1]))
    datos.append((i[0],2,i[2]))
    datos.append((i[0],3,i[3]))
    datos.append((i[0],4,i[4]))
    datos.append((i[0],5,i[5]))
    datos.append((i[0],6,i[6]))
    datos.append((i[0],7,i[7]))
    datos.append((i[0],8,i[8]))
    datos.append((i[0],9,i[9]))
    datos.append((i[0],10,i[10]))
    datos.append((i[0],11,i[11]))
    datos.append((i[0],12,i[12]))
    datos.append((i[0],13,i[13]))
    datos.append((i[0],14,i[14]))
    datos.append((i[0],15,i[15]))
    datos.append((i[0],16,i[16]))
    
    
x = np.array(datos,dtype='int,int,int')
nuevo_formato = etl.fromarray(x)
cambiar_header = etl.setheader(nuevo_formato,['periodo','id_delegacion','numero'])
convertir_numeros = etl.convertnumbers(cambiar_header)

conexion = psycopg2.connect(database=database, 
                            user=user, password=password,
                            host=host, port=port)
etl.todb(convertir_numeros, conexion, 'accidentes')




