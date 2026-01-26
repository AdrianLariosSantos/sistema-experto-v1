import os
import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
try:
    from dotenv import load_dotenv
except Exception:
    try:
        from dotenv.main import load_dotenv
    except Exception as exc:
        raise RuntimeError(
            "No se encontró load_dotenv. Instala 'python-dotenv' y desinstala el paquete 'dotenv' si existe."
        ) from exc

load_dotenv()

db_user = os.getenv('DB_USER', 'root')
db_password = os.getenv('DB_PASSWORD', '')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', '3306')
db_name = os.getenv('DB_NAME', 'escalahamilton')

string_connection = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
connection = create_engine(
    string_connection,
    pool_pre_ping=True,
    pool_recycle=1800
)
sql = 'SELECT * FROM conocimiento'
datos = pd.read_sql_query(sql, connection)
df = pd.DataFrame(datos)

Total_Datos = len(datos)

pc1 = len(df[df['Clase'].str.contains('Depresion')])
pc2 = len(df[df['Clase'].str.contains('Ansiedad')])

Total_Depresion=len(df[df['Clase'].str.contains('Depresion')])
Total_Ansiedad=len(df[df['Clase'].str.contains('Ansiedad')])

#Conteo de datos Si
humor1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Humor']=='0')])
humor2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Humor']=='0')])
#Conteo de datos No
humor3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Humor']=='1')])
humor4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Humor']=='1')])

humor5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Humor']=='2')])
humor6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Humor']=='2')])

humor7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Humor']=='3')])
humor8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Humor']=='3')])

humor9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Humor']=='4')])
humor10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Humor']=='4')])

culpa1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Culpa']=='0')])
culpa2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Culpa']=='0')])

culpa3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Culpa']=='1')])
culpa4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Culpa']=='1')])

culpa5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Culpa']=='2')])
culpa6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Culpa']=='2')])

culpa7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Culpa']=='3')])
culpa8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Culpa']=='3')])

culpa9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Culpa']=='4')])
culpa10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Culpa']=='4')])

suicidio1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Suicidio']=='0')])
suicidio2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Suicidio']=='0')])

suicidio3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Suicidio']=='1')])
suicidio4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Suicidio']=='1')])

suicidio5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Suicidio']=='2')])
suicidio6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Suicidio']=='2')])

suicidio7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Suicidio']=='3')])
suicidio8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Suicidio']=='3')])

suicidio9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Suicidio']=='4')])
suicidio10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Suicidio']=='4')])

insomnioprecoz1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['IPrecoz']=='0')])
insomnioprecoz2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['IPrecoz']=='0')])

insomnioprecoz3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['IPrecoz']=='1')])
insomnioprecoz4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['IPrecoz']=='1')])

insomnioprecoz5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['IPrecoz']=='2')])
insomnioprecoz6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['IPrecoz']=='2')])

insomnioprecoz7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['IPrecoz']=='3')])
insomnioprecoz8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['IPrecoz']=='3')])

insomnioprecoz9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['IPrecoz']=='4')])
insomnioprecoz10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['IPrecoz']=='4')])

insomniointermedio1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['IIntermedio']=='0')])
insomniointermedio2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['IIntermedio']=='0')])

insomniointermedio3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['IIntermedio']=='1')])
insomniointermedio4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['IIntermedio']=='1')])

insomniointermedio5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['IIntermedio']=='2')])
insomniointermedio6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['IIntermedio']=='2')])

insomniointermedio7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['IIntermedio']=='3')])
insomniointermedio8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['IIntermedio']=='3')])

insomniointermedio9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['IIntermedio']=='4')])
insomniointermedio10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['IIntermedio']=='4')])

insomniotardio1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['ITardio']=='0')])
insomniotardio2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['ITardio']=='0')])

insomniotardio3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['ITardio']=='1')])
insomniotardio4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['ITardio']=='1')])

insomniotardio5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['ITardio']=='2')])
insomniotardio6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['ITardio']=='2')])

insomniotardio7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['ITardio']=='3')])
insomniotardio8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['ITardio']=='3')])

insomniotardio9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['ITardio']=='4')])
insomniotardio10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['ITardio']=='4')])

trabajo1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Trabajo']=='0')])
trabajo2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Trabajo']=='0')])

trabajo3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Trabajo']=='1')])
trabajo4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Trabajo']=='1')])

trabajo5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Trabajo']=='2')])
trabajo6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Trabajo']=='2')])

trabajo7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Trabajo']=='3')])
trabajo8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Trabajo']=='3')])

trabajo9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Trabajo']=='4')])
trabajo10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Trabajo']=='4')])

inhibicion1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Inhibicion']=='0')])
inhibicion2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Inhibicion']=='0')])

inhibicion3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Inhibicion']=='1')])
inhibicion4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Inhibicion']=='1')])

inhibicion5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Inhibicion']=='2')])
inhibicion6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Inhibicion']=='2')])

inhibicion7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Inhibicion']=='3')])
inhibicion8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Inhibicion']=='3')])

inhibicion9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Inhibicion']=='4')])
inhibicion10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Inhibicion']=='4')])

agitacion1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Agitacion']=='0')])
agitacion2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Agitacion']=='0')])

agitacion3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Agitacion']=='1')])
agitacion4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Agitacion']=='1')])

agitacion5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Agitacion']=='2')])
agitacion6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Agitacion']=='2')])

agitacion7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Agitacion']=='3')])
agitacion8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Agitacion']=='3')])

agitacion9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Agitacion']=='4')])
agitacion10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Agitacion']=='4')])
        
psiquica1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['APsiquica']=='0')])
psiquica2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['APsiquica']=='0')])

psiquica3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['APsiquica']=='1')])
psiquica4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['APsiquica']=='1')])

psiquica5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['APsiquica']=='2')])
psiquica6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['APsiquica']=='2')])

psiquica7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['APsiquica']=='3')])
psiquica8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['APsiquica']=='3')])

psiquica9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['APsiquica']=='4')])
psiquica10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['APsiquica']=='4')])
        
somatica1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['ASomatica']=='0')])
somatica2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['ASomatica']=='0')])

somatica3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['ASomatica']=='1')])
somatica4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['ASomatica']=='1')])

somatica5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['ASomatica']=='2')])
somatica6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['ASomatica']=='2')])

somatica7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['ASomatica']=='3')])
somatica8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['ASomatica']=='3')])

somatica9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['ASomatica']=='4')])
somatica10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['ASomatica']=='4')])

sgastrointestinales1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGastrointestinales']=='0')])
sgastrointestinales2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGastrointestinales']=='0')])

sgastrointestinales3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGastrointestinales']=='1')])
sgastrointestinales4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGastrointestinales']=='1')])

sgastrointestinales5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGastrointestinales']=='2')])
sgastrointestinales6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGastrointestinales']=='2')])

sgastrointestinales7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGastrointestinales']=='3')])
sgastrointestinales8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGastrointestinales']=='3')])

sgastrointestinales9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGastrointestinales']=='4')])
sgastrointestinales10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGastrointestinales']=='4')])
 
sgenerales1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGenerales']=='0')])
sgenerales2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGenerales']=='0')])

sgenerales3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGenerales']=='1')])
sgenerales4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGenerales']=='1')])

sgenerales5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGenerales']=='2')])
sgenerales6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGenerales']=='2')])

sgenerales7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGenerales']=='3')])
sgenerales8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGenerales']=='3')])

sgenerales9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGenerales']=='4')])
sgenerales10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGenerales']=='4')])

sgenitales1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGenitales']=='0')])
sgenitales2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGenitales']=='0')])

sgenitales3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGenitales']=='1')])
sgenitales4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGenitales']=='1')])

sgenitales5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGenitales']=='2')])
sgenitales6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGenitales']=='2')])

sgenitales7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGenitales']=='3')])
sgenitales8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGenitales']=='3')])

sgenitales9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SGenitales']=='4')])
sgenitales10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SGenitales']=='4')])

hipocondria1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Hipocondria']=='0')])
hipocondria2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Hipocondria']=='0')])

hipocondria3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Hipocondria']=='1')])
hipocondria4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Hipocondria']=='1')])

hipocondria5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Hipocondria']=='2')])
hipocondria6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Hipocondria']=='2')])

hipocondria7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Hipocondria']=='3')])
hipocondria8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Hipocondria']=='3')])

hipocondria9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Hipocondria']=='4')])
hipocondria10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Hipocondria']=='4')])

peso1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Peso']=='0')])
peso2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Peso']=='0')])

peso3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Peso']=='1')])
peso4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Peso']=='1')])

peso5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Peso']=='2')])
peso6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Peso']=='2')])

peso7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Peso']=='3')])
peso8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Peso']=='3')])

peso9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Peso']=='4')])
peso10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Peso']=='4')])

introspeccion1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Introspeccion']=='0')])
introspeccion2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Introspeccion']=='0')])

introspeccion3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Introspeccion']=='1')])
introspeccion4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Introspeccion']=='1')])

introspeccion5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Introspeccion']=='2')])
introspeccion6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Introspeccion']=='2')])

introspeccion7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Introspeccion']=='3')])
introspeccion8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Introspeccion']=='3')])

introspeccion9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Introspeccion']=='4')])
introspeccion10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Introspeccion']=='4')])

animoansioso1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['AnimoAnsioso']=='0')])
animoansioso2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['AnimoAnsioso']=='0')])

animoansioso3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['AnimoAnsioso']=='1')])
animoansioso4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['AnimoAnsioso']=='1')])

animoansioso5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['AnimoAnsioso']=='2')])
animoansioso6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['AnimoAnsioso']=='2')])

animoansioso7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['AnimoAnsioso']=='3')])
animoansioso8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['AnimoAnsioso']=='3')])

animoansioso9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['AnimoAnsioso']=='4')])
animoansioso10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['AnimoAnsioso']=='4')])

tension1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Tension']=='0')])
tension2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Tension']=='0')])

tension3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Tension']=='1')])
tension4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Tension']=='1')])

tension5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Tension']=='2')])
tension6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Tension']=='2')])

tension7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Tension']=='3')])
tension8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Tension']=='3')])

tension9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Tension']=='4')])
tension10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Tension']=='4')])

temores1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Temores']=='0')])
temores2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Temores']=='0')])

temores3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Temores']=='1')])
temores4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Temores']=='1')])

temores5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Temores']=='2')])
temores6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Temores']=='2')])

temores7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Temores']=='3')])
temores8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Temores']=='3')])

temores9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Temores']=='4')])
temores10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Temores']=='4')])

insomnio1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Insomnio']=='0')])
insomnio2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Insomnio']=='0')])

insomnio3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Insomnio']=='1')])
insomnio4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Insomnio']=='1')])

insomnio5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Insomnio']=='2')])
insomnio6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Insomnio']=='2')])

insomnio7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Insomnio']=='3')])
insomnio8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Insomnio']=='3')])

insomnio9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Insomnio']=='4')])
insomnio10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Insomnio']=='4')])

intelectual1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Intelectual']=='0')])
intelectual2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Intelectual']=='0')])

intelectual3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Intelectual']=='1')])
intelectual4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Intelectual']=='1')])

intelectual5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Intelectual']=='2')])
intelectual6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Intelectual']=='2')])

intelectual7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Intelectual']=='3')])
intelectual8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Intelectual']=='3')])

intelectual9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Intelectual']=='4')])
intelectual10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Intelectual']=='4')])

animodeprimido1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['AnimoDeprimido']=='0')])
animodeprimido2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['AnimoDeprimido']=='0')])

animodeprimido3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['AnimoDeprimido']=='1')])
animodeprimido4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['AnimoDeprimido']=='1')])

animodeprimido5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['AnimoDeprimido']=='2')])
animodeprimido6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['AnimoDeprimido']=='2')])

animodeprimido7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['AnimoDeprimido']=='3')])
animodeprimido8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['AnimoDeprimido']=='3')])

animodeprimido9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['AnimoDeprimido']=='4')])
animodeprimido10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['AnimoDeprimido']=='4')])

somaticosmusculares1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SomaticosMusculares']=='0')])
somaticosmusculares2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SomaticosMusculares']=='0')])

somaticosmusculares3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SomaticosMusculares']=='1')])
somaticosmusculares4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SomaticosMusculares']=='1')])

somaticosmusculares5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SomaticosMusculares']=='2')])
somaticosmusculares6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SomaticosMusculares']=='2')])

somaticosmusculares7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SomaticosMusculares']=='3')])
somaticosmusculares8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SomaticosMusculares']=='3')])

somaticosmusculares9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SomaticosMusculares']=='4')])
somaticosmusculares10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SomaticosMusculares']=='4')])

somaticossensoriales1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SomaticosSensoriales']=='0')])
somaticossensoriales2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SomaticosSensoriales']=='0')])

somaticossensoriales3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SomaticosSensoriales']=='1')])
somaticossensoriales4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SomaticosSensoriales']=='1')])

somaticossensoriales5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SomaticosSensoriales']=='2')])
somaticossensoriales6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SomaticosSensoriales']=='2')])

somaticossensoriales7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SomaticosSensoriales']=='3')])
somaticossensoriales8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SomaticosSensoriales']=='3')])

somaticossensoriales9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['SomaticosSensoriales']=='4')])
somaticossensoriales10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['SomaticosSensoriales']=='4')])

cardiovasculares1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Cardiovasculares']=='0')])
cardiovasculares2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Cardiovasculares']=='0')])

cardiovasculares3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Cardiovasculares']=='1')])
cardiovasculares4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Cardiovasculares']=='1')])

cardiovasculares5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Cardiovasculares']=='2')])
cardiovasculares6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Cardiovasculares']=='2')])

cardiovasculares7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Cardiovasculares']=='3')])
cardiovasculares8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Cardiovasculares']=='3')])

cardiovasculares9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Cardiovasculares']=='4')])
cardiovasculares10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Cardiovasculares']=='4')])

respiratorios1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Respiratorios']=='0')])
respiratorios2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Respiratorios']=='0')])

respiratorios3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Respiratorios']=='1')])
respiratorios4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Respiratorios']=='1')])

respiratorios5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Respiratorios']=='2')])
respiratorios6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Respiratorios']=='2')])

respiratorios7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Respiratorios']=='3')])
respiratorios8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Respiratorios']=='3')])

respiratorios9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Respiratorios']=='4')])
respiratorios10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Respiratorios']=='4')])

gastrointestinales1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Gastrointestinales']=='0')])
gastrointestinales2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Gastrointestinales']=='0')])

gastrointestinales3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Gastrointestinales']=='1')])
gastrointestinales4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Gastrointestinales']=='1')])

gastrointestinales5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Gastrointestinales']=='2')])
gastrointestinales6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Gastrointestinales']=='2')])

gastrointestinales7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Gastrointestinales']=='3')])
gastrointestinales8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Gastrointestinales']=='3')])

gastrointestinales9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Gastrointestinales']=='4')])
gastrointestinales10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Gastrointestinales']=='4')])

genitourionarios1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Genitourinarios']=='0')])
genitourionarios2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Genitourinarios']=='0')])

genitourionarios3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Genitourinarios']=='1')])
genitourionarios4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Genitourinarios']=='1')])

genitourionarios5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Genitourinarios']=='2')])
genitourionarios6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Genitourinarios']=='2')])

genitourionarios7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Genitourinarios']=='3')])
genitourionarios8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Genitourinarios']=='3')])

genitourionarios9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Genitourinarios']=='4')])
genitourionarios10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Genitourinarios']=='4')])

autonomos1 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Autonomos']=='0')])
autonomos2 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Autonomos']=='0')])

autonomos3 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Autonomos']=='1')])
autonomos4 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Autonomos']=='1')])

autonomos5 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Autonomos']=='2')])
autonomos6 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Autonomos']=='2')])

autonomos7 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Autonomos']=='3')])
autonomos8 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Autonomos']=='3')])

autonomos9 = len(datos.loc[datos['Clase'].str.contains('Depresion')&(datos['Autonomos']=='4')])
autonomos10 = len(datos.loc[datos['Clase'].str.contains('Ansiedad')&(datos['Autonomos']=='4')])

def clase_Depresion(Humor,Culpa,Suicidio,IPrecoz,IIntermedio,ITardio,Trabajo,Inhibicion,Agitacion,APsiquica,ASomatica,SGastrointestinales,SGenerales,SGenitales,Hipocondria,Peso,Introspeccion,AnimoAnsioso,Tension,Temores,Insomnio,Intelectual,AnimoDeprimido,SomaticosMusculares,SomaticosSensoriales,Cardiovasculares,Respiratorios,Gastrointestinales,Genitourinarios,Autonomos):
# =============================================================================
#     #Selección para Humor
# =============================================================================
    if Humor=="0":
        humor=humor1/Total_Depresion
    if Humor=="1":
        humor=humor3/Total_Depresion
    if Humor=="2":
        humor=humor5/Total_Depresion
    if Humor=="3":
        humor=humor7/Total_Depresion
    if Humor=="4":
        humor=humor9/Total_Depresion
# =============================================================================
#     #Seleccion para Culpa
# =============================================================================
    if Culpa=="0":
        culpa=culpa1/Total_Depresion
    if Culpa=="1":
        culpa=culpa3/Total_Depresion
    if Culpa=="2":
        culpa=culpa5/Total_Depresion
    if Culpa=="3":
        culpa=culpa7/Total_Depresion
    if Culpa=="4":
        culpa=culpa9/Total_Depresion
# =============================================================================
#     #Seleccion para Suicidio
# =============================================================================
    if Suicidio=="0":
        suicidio=suicidio1/Total_Depresion
    if Suicidio=="1":
        suicidio=suicidio3/Total_Depresion
    if Suicidio=="2":
        suicidio=suicidio5/Total_Depresion
    if Suicidio=="3":
        suicidio=suicidio7/Total_Depresion
    if Suicidio=="4":
        suicidio=suicidio9/Total_Depresion
# =============================================================================
#     #Seleccion de Insomnio Precoz
# =============================================================================
    if IPrecoz=="0":
        iprecoz=insomnioprecoz1/Total_Depresion
    if IPrecoz=="1":
        iprecoz=insomnioprecoz3/Total_Depresion
    if IPrecoz=="2":
        iprecoz=insomnioprecoz5/Total_Depresion
    if IPrecoz=="3":
        iprecoz=insomnioprecoz7/Total_Depresion
    if IPrecoz=="4":
        iprecoz=insomnioprecoz9/Total_Depresion
# =============================================================================
#     #Seleccion de Insomnio Intermedio
# =============================================================================
    if IIntermedio=="0":
        iintermedio=insomniointermedio1/Total_Depresion
    if IIntermedio=="1":
        iintermedio=insomniointermedio3/Total_Depresion
    if IIntermedio=="2":
        iintermedio=insomniointermedio5/Total_Depresion
    if IIntermedio=="3":
        iintermedio=insomniointermedio7/Total_Depresion
    if IIntermedio=="4":
        iintermedio=insomniointermedio9/Total_Depresion
# =============================================================================
#     #Seleccion de Insomnio Tardio
# =============================================================================
    if ITardio=="0":
        itardio=insomniotardio1/Total_Depresion
    if ITardio=="1":
        itardio=insomniotardio3/Total_Depresion
    if ITardio=="2":
        itardio=insomniotardio5/Total_Depresion
    if ITardio=="3":
        itardio=insomniotardio7/Total_Depresion
    if ITardio=="4":
        itardio=insomniotardio9/Total_Depresion    
# =============================================================================
#     #Seleccion de Trabajo
# =============================================================================
    if Trabajo=="0":
        trabajo=trabajo1/Total_Depresion
    if Trabajo=="1":
        trabajo=trabajo3/Total_Depresion
    if Trabajo=="2":
        trabajo=trabajo5/Total_Depresion
    if Trabajo=="3":
        trabajo=trabajo7/Total_Depresion
    if Trabajo=="4":
        trabajo=trabajo9/Total_Depresion
# =============================================================================
#     #Seleccion de Inhibicion
# =============================================================================
    if Inhibicion=="0":
        inhibicion=inhibicion1/Total_Depresion
    if Inhibicion=="1":
        inhibicion=inhibicion3/Total_Depresion
    if Inhibicion=="2":
        inhibicion=inhibicion5/Total_Depresion
    if Inhibicion=="3":
        inhibicion=inhibicion7/Total_Depresion
    if Inhibicion=="4":
        inhibicion=inhibicion9/Total_Depresion
# =============================================================================
#     #Seleccion de Agitacion
# =============================================================================
    if Agitacion=="0":
        agitacion=agitacion1/Total_Depresion
    if Agitacion=="1":
        agitacion=agitacion3/Total_Depresion
    if Agitacion=="2":
        agitacion=agitacion5/Total_Depresion
    if Agitacion=="3":
        agitacion=agitacion7/Total_Depresion   
    if Agitacion=="4":
        agitacion=agitacion9/Total_Depresion  
# =============================================================================
#     #Seleccion de APsiquica
# =============================================================================
    if APsiquica=="0":
        apsiquica=psiquica1/Total_Depresion
    if APsiquica=="1":
        apsiquica=psiquica3/Total_Depresion
    if APsiquica=="2":
        apsiquica=psiquica5/Total_Depresion
    if APsiquica=="3":
        apsiquica=psiquica7/Total_Depresion
    if APsiquica=="4":
        apsiquica=psiquica9/Total_Depresion
# =============================================================================
#     #Seleccion de ASomatica
# =============================================================================
    if ASomatica=="0":
        asomatica=somatica1/Total_Depresion
    if ASomatica=="1":
        asomatica=somatica3/Total_Depresion
    if ASomatica=="2":
        asomatica=somatica5/Total_Depresion
    if ASomatica=="3":
        asomatica=somatica7/Total_Depresion
    if ASomatica=="4":
        asomatica=somatica9/Total_Depresion
# =============================================================================
#     #Seleccion de SGastrointestinales
# =============================================================================
    if SGastrointestinales=="0":
        sgastrointestinales=sgastrointestinales1/Total_Depresion
    if SGastrointestinales=="1":
        sgastrointestinales=sgastrointestinales3/Total_Depresion
    if SGastrointestinales=="2":
        sgastrointestinales=sgastrointestinales5/Total_Depresion
    if SGastrointestinales=="3":
        sgastrointestinales=sgastrointestinales7/Total_Depresion
    if SGastrointestinales=="4":
        sgastrointestinales=sgastrointestinales9/Total_Depresion
# =============================================================================
#     #Seleccion de SGenerales
# =============================================================================
    if SGenerales=="0":
        sgenerales=sgenerales1/Total_Depresion
    if SGenerales=="1":
        sgenerales=sgenerales3/Total_Depresion
    if SGenerales=="2":
        sgenerales=sgenerales5/Total_Depresion
    if SGenerales=="3":
        sgenerales=sgenerales7/Total_Depresion
    if SGenerales=="4":
        sgenerales=sgenerales9/Total_Depresion
# =============================================================================
#     #Seleccion de SGenitales
# =============================================================================
    if SGenitales=="0":
        sgenitales=sgenitales1/Total_Depresion
    if SGenitales=="1":
        sgenitales=sgenitales3/Total_Depresion
    if SGenitales=="2":
        sgenitales=sgenitales5/Total_Depresion
    if SGenitales=="3":
        sgenitales=sgenitales7/Total_Depresion
    if SGenitales=="4":
        sgenitales=sgenitales9/Total_Depresion
# =============================================================================
#     #Seleccion de Hipocondria
# =============================================================================
    if Hipocondria=="0":
        hipocondria=hipocondria1/Total_Depresion
    if Hipocondria=="1":
        hipocondria=hipocondria3/Total_Depresion
    if Hipocondria=="2":
        hipocondria=hipocondria5/Total_Depresion
    if Hipocondria=="3":
        hipocondria=hipocondria7/Total_Depresion
    if Hipocondria=="4":
        hipocondria=hipocondria9/Total_Depresion
# =============================================================================
#     #Seleccion de Peso
# =============================================================================
    if Peso=="0":
        peso=peso1/Total_Depresion
    if Peso=="1":
        peso=peso3/Total_Depresion
    if Peso=="2":
        peso=peso5/Total_Depresion
    if Peso=="3":
        peso=peso7/Total_Depresion    
    if Peso=="4":
        peso=peso9/Total_Depresion
# =============================================================================
#     #Seleccion de Instrospeccion
# =============================================================================
    if Introspeccion=="0":
        introspeccion=introspeccion1/Total_Depresion
    if Introspeccion=="1":
        introspeccion=introspeccion3/Total_Depresion
    if Introspeccion=="2":
        introspeccion=introspeccion5/Total_Depresion
    if Introspeccion=="3":
        introspeccion=introspeccion7/Total_Depresion 
    if Introspeccion=="4":
        introspeccion=introspeccion9/Total_Depresion
# =============================================================================
#     #Seleccion de Animo Ansioso
# =============================================================================
    if AnimoAnsioso=="0":
        animoansioso=animoansioso1/Total_Depresion
    if AnimoAnsioso=="1":
        animoansioso=animoansioso3/Total_Depresion
    if AnimoAnsioso=="2":
        animoansioso=animoansioso5/Total_Depresion
    if AnimoAnsioso=="3":
        animoansioso=animoansioso7/Total_Depresion 
    if AnimoAnsioso=="4":
        animoansioso=animoansioso9/Total_Depresion
# =============================================================================
#     #Seleccion de Tension
# =============================================================================
    if Tension=="0":
        tension=tension1/Total_Depresion
    if Tension=="1":
        tension=tension3/Total_Depresion
    if Tension=="2":
        tension=tension5/Total_Depresion
    if Tension=="3":
        tension=tension7/Total_Depresion 
    if Tension=="4":
        tension=tension9/Total_Depresion
# =============================================================================
#     #Seleccion de Temores
# =============================================================================
    if Temores=="0":
        temores=temores1/Total_Depresion
    if Temores=="1":
        temores=temores3/Total_Depresion
    if Temores=="2":
        temores=temores5/Total_Depresion
    if Temores=="3":
        temores=temores7/Total_Depresion 
    if Temores=="4":
        temores=temores9/Total_Depresion
# =============================================================================
#     #Seleccion de Insomnio
# =============================================================================
    if Insomnio=="0":
        insomnio=insomnio1/Total_Depresion
    if Insomnio=="1":
        insomnio=insomnio3/Total_Depresion
    if Insomnio=="2":
        insomnio=insomnio5/Total_Depresion
    if Insomnio=="3":
        insomnio=insomnio7/Total_Depresion 
    if Insomnio=="4":
        insomnio=insomnio9/Total_Depresion
# =============================================================================
#     #Seleccion de Intelectual
# =============================================================================
    if Intelectual=="0":
        intelectual=intelectual1/Total_Depresion
    if Intelectual=="1":
        intelectual=intelectual3/Total_Depresion
    if Intelectual=="2":
        intelectual=intelectual5/Total_Depresion
    if Intelectual=="3":
        intelectual=intelectual7/Total_Depresion  
    if Intelectual=="4":
        intelectual=intelectual9/Total_Depresion
# =============================================================================
#     #Seleccion de Animo Deprimido
# =============================================================================
    if AnimoDeprimido=="0":
        animodeprimido=animodeprimido1/Total_Depresion
    if AnimoDeprimido=="1":
        animodeprimido=animodeprimido3/Total_Depresion
    if AnimoDeprimido=="2":
        animodeprimido=animodeprimido5/Total_Depresion
    if AnimoDeprimido=="3":
        animodeprimido=animodeprimido7/Total_Depresion
    if AnimoDeprimido=="4":
        animodeprimido=animodeprimido9/Total_Depresion
# =============================================================================
#     #Seleccion de Somaticos Musculares
# =============================================================================
    if SomaticosMusculares=="0":
        somusculares=somaticosmusculares1/Total_Depresion
    if SomaticosMusculares=="1":
        somusculares=somaticosmusculares3/Total_Depresion
    if SomaticosMusculares=="2":
        somusculares=somaticosmusculares5/Total_Depresion
    if SomaticosMusculares=="3":
        somusculares=somaticosmusculares7/Total_Depresion  
    if SomaticosMusculares=="4":
        somusculares=somaticosmusculares9/Total_Depresion
# =============================================================================
#     #Seleccion de Somaticos Sensoriales
# =============================================================================
    if SomaticosSensoriales=="0":
        sosensoriales=somaticossensoriales1/Total_Depresion
    if SomaticosSensoriales=="1":
        sosensoriales=somaticossensoriales3/Total_Depresion
    if SomaticosSensoriales=="2":
        sosensoriales=somaticossensoriales5/Total_Depresion
    if SomaticosSensoriales=="3":
        sosensoriales=somaticossensoriales7/Total_Depresion
    if SomaticosSensoriales=="4":
        sosensoriales=somaticossensoriales9/Total_Depresion
# =============================================================================
#     #Seleccion de Cardiovasculares
# =============================================================================
    if Cardiovasculares=="0":
        cardiovasculares=cardiovasculares1/Total_Depresion
    if Cardiovasculares=="1":
        cardiovasculares=cardiovasculares3/Total_Depresion
    if Cardiovasculares=="2":
        cardiovasculares=cardiovasculares5/Total_Depresion
    if Cardiovasculares=="3":
        cardiovasculares=cardiovasculares7/Total_Depresion  
    if Cardiovasculares=="4":
        cardiovasculares=cardiovasculares9/Total_Depresion
# =============================================================================
#     #Seleccion de Respiratorios
# =============================================================================
    if Respiratorios=="0":
        respiratorios=respiratorios1/Total_Depresion
    if Respiratorios=="1":
        respiratorios=respiratorios3/Total_Depresion
    if Respiratorios=="2":
        respiratorios=respiratorios5/Total_Depresion
    if Respiratorios=="3":
        respiratorios=respiratorios7/Total_Depresion 
    if Respiratorios=="4":
        respiratorios=respiratorios9/Total_Depresion 
# =============================================================================
#     #Seleccion de Gastrointestinales
# =============================================================================
    if Gastrointestinales=="0":
        agastrointestinales=gastrointestinales1/Total_Depresion
    if Gastrointestinales=="1":
        agastrointestinales=gastrointestinales3/Total_Depresion
    if Gastrointestinales=="2":
        agastrointestinales=gastrointestinales5/Total_Depresion
    if Gastrointestinales=="3":
        agastrointestinales=gastrointestinales7/Total_Depresion
    if Gastrointestinales=="4":
        agastrointestinales=gastrointestinales9/Total_Depresion
# =============================================================================
#     #Seleccion de Genitourinarios
# =============================================================================
    if Genitourinarios=="0":
        genitourinarios=genitourionarios1/Total_Depresion
    if Genitourinarios=="1":
        genitourinarios=genitourionarios3/Total_Depresion
    if Genitourinarios=="2":
        genitourinarios=genitourionarios5/Total_Depresion
    if Genitourinarios=="3":
        genitourinarios=genitourionarios7/Total_Depresion
    if Genitourinarios=="4":
        genitourinarios=genitourionarios9/Total_Depresion
# =============================================================================
#     #Seleccion de Autonomos
# =============================================================================
    if Autonomos=="0":
        autonomos=autonomos1/Total_Depresion
    if Autonomos=="1":
        autonomos=autonomos3/Total_Depresion
    if Autonomos=="2":
        autonomos=autonomos5/Total_Depresion
    if Autonomos=="3":
        autonomos=autonomos7/Total_Depresion
    if Autonomos=="4":
        autonomos=autonomos9/Total_Depresion  
    
    Calculo_PC1=((pc1/Total_Datos)*(humor* culpa* suicidio* iprecoz* iintermedio* itardio* trabajo* inhibicion* agitacion* apsiquica* asomatica* sgastrointestinales* sgenerales* sgenitales* hipocondria* peso* introspeccion* animoansioso* tension* temores* insomnio* intelectual* animodeprimido* somusculares* sosensoriales* cardiovasculares* respiratorios* agastrointestinales* genitourinarios* autonomos))
    return Calculo_PC1        


def clase_Ansiedad(Humor,Culpa,Suicidio,IPrecoz,IIntermedio,ITardio,Trabajo,Inhibicion,Agitacion,APsiquica,ASomatica,SGastrointestinales,SGenerales,SGenitales,Hipocondria,Peso,Introspeccion,AnimoAnsioso,Tension,Temores,Insomnio,Intelectual,AnimoDeprimido,SomaticosMusculares,SomaticosSensoriales,Cardiovasculares,Respiratorios,Gastrointestinales,Genitourinarios,Autonomos):
# =============================================================================
#     #Selección para Humor
# =============================================================================
    if Humor=="0":
        humor=humor2/Total_Ansiedad
    if Humor=="1":
        humor=humor4/Total_Ansiedad
    if Humor=="2":
        humor=humor6/Total_Ansiedad
    if Humor=="3":
        humor=humor8/Total_Ansiedad
    if Humor=="4":
        humor=humor10/Total_Ansiedad
# =============================================================================
#     #Seleccion para Culpa
# =============================================================================
    if Culpa=="0":
        culpa=culpa2/Total_Ansiedad
    if Culpa=="1":
        culpa=culpa4/Total_Ansiedad
    if Culpa=="2":
        culpa=culpa6/Total_Ansiedad
    if Culpa=="3":
        culpa=culpa8/Total_Ansiedad
    if Culpa=="4":
        culpa=culpa10/Total_Ansiedad
# =============================================================================
#     #Seleccion para Suicidio
# =============================================================================
    if Suicidio=="0":
        suicidio=suicidio2/Total_Ansiedad
    if Suicidio=="1":
        suicidio=suicidio4/Total_Ansiedad
    if Suicidio=="2":
        suicidio=suicidio6/Total_Ansiedad
    if Suicidio=="3":
        suicidio=suicidio8/Total_Ansiedad
    if Suicidio=="4":
        suicidio=suicidio10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Insomnio Precoz
# =============================================================================
    if IPrecoz=="0":
        iprecoz=insomnioprecoz2/Total_Ansiedad
    if IPrecoz=="1":
        iprecoz=insomnioprecoz4/Total_Ansiedad
    if IPrecoz=="2":
        iprecoz=insomnioprecoz6/Total_Ansiedad
    if IPrecoz=="3":
        iprecoz=insomnioprecoz8/Total_Ansiedad
    if IPrecoz=="4":
        iprecoz=insomnioprecoz10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Insomnio Intermedio
# =============================================================================
    if IIntermedio=="0":
        iintermedio=insomniointermedio2/Total_Ansiedad
    if IIntermedio=="1":
        iintermedio=insomniointermedio4/Total_Ansiedad
    if IIntermedio=="2":
        iintermedio=insomniointermedio6/Total_Ansiedad
    if IIntermedio=="3":
        iintermedio=insomniointermedio8/Total_Ansiedad
    if IIntermedio=="4":
        iintermedio=insomniointermedio10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Insomnio Tardio
# =============================================================================
    if ITardio=="0":
        itardio=insomniotardio2/Total_Ansiedad
    if ITardio=="1":
        itardio=insomniotardio4/Total_Ansiedad
    if ITardio=="2":
        itardio=insomniotardio6/Total_Ansiedad
    if ITardio=="3":
        itardio=insomniotardio8/Total_Ansiedad
    if ITardio=="4":
        itardio=insomniotardio10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Trabajo
# =============================================================================
    if Trabajo=="0":
        trabajo=trabajo2/Total_Ansiedad
    if Trabajo=="1":
        trabajo=trabajo4/Total_Ansiedad
    if Trabajo=="2":
        trabajo=trabajo6/Total_Ansiedad
    if Trabajo=="3":
        trabajo=trabajo8/Total_Ansiedad
    if Trabajo=="4":
        trabajo=trabajo10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Inhibicion
# =============================================================================
    if Inhibicion=="0":
        inhibicion=inhibicion2/Total_Ansiedad
    if Inhibicion=="1":
        inhibicion=inhibicion4/Total_Ansiedad
    if Inhibicion=="2":
        inhibicion=inhibicion6/Total_Ansiedad
    if Inhibicion=="3":
        inhibicion=inhibicion8/Total_Ansiedad  
    if Inhibicion=="4":
        inhibicion=inhibicion10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Agitacion
# =============================================================================
    if Agitacion=="0":
        agitacion=agitacion2/Total_Ansiedad
    if Agitacion=="1":
        agitacion=agitacion4/Total_Ansiedad
    if Agitacion=="2":
        agitacion=agitacion6/Total_Ansiedad
    if Agitacion=="3":
        agitacion=agitacion8/Total_Ansiedad
    if Agitacion=="4":
        agitacion=agitacion10/Total_Ansiedad   
# =============================================================================
#     #Seleccion de APsiquica
# =============================================================================
    if APsiquica=="0":
        apsiquica=psiquica2/Total_Ansiedad
    if APsiquica=="1":
        apsiquica=psiquica4/Total_Ansiedad
    if APsiquica=="2":
        apsiquica=psiquica6/Total_Ansiedad
    if APsiquica=="3":
        apsiquica=psiquica8/Total_Ansiedad
    if APsiquica=="4":
        apsiquica=psiquica10/Total_Ansiedad
# =============================================================================
#     #Seleccion de ASomatica
# =============================================================================
    if ASomatica=="0":
        asomatica=somatica2/Total_Ansiedad
    if ASomatica=="1":
        asomatica=somatica4/Total_Ansiedad
    if ASomatica=="2":
        asomatica=somatica6/Total_Ansiedad
    if ASomatica=="3":
        asomatica=somatica8/Total_Ansiedad
    if ASomatica=="4":
        asomatica=somatica10/Total_Ansiedad
# =============================================================================
#     #Seleccion de SGastrointestinales
# =============================================================================
    if SGastrointestinales=="0":
        sgastrointestinales=sgastrointestinales2/Total_Ansiedad
    if SGastrointestinales=="1":
        sgastrointestinales=sgastrointestinales4/Total_Ansiedad
    if SGastrointestinales=="2":
        sgastrointestinales=sgastrointestinales6/Total_Ansiedad
    if SGastrointestinales=="3":
        sgastrointestinales=sgastrointestinales8/Total_Ansiedad
    if SGastrointestinales=="4":
        sgastrointestinales=sgastrointestinales10/Total_Ansiedad
# =============================================================================
#     #Seleccion de SGenerales
# =============================================================================
    if SGenerales=="0":
        sgenerales=sgenerales2/Total_Ansiedad
    if SGenerales=="1":
        sgenerales=sgenerales4/Total_Ansiedad
    if SGenerales=="2":
        sgenerales=sgenerales6/Total_Ansiedad
    if SGenerales=="3":
        sgenerales=sgenerales8/Total_Ansiedad
    if SGenerales=="4":
        sgenerales=sgenerales10/Total_Ansiedad
# =============================================================================
#     #Seleccion de SGenitales
# =============================================================================
    if SGenitales=="0":
        sgenitales=sgenitales2/Total_Ansiedad
    if SGenitales=="1":
        sgenitales=sgenitales4/Total_Ansiedad
    if SGenitales=="2":
        sgenitales=sgenitales6/Total_Ansiedad
    if SGenitales=="3":
        sgenitales=sgenitales8/Total_Ansiedad
    if SGenitales=="4":
        sgenitales=sgenitales10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Hipocondria
# =============================================================================
    if Hipocondria=="0":
        hipocondria=hipocondria2/Total_Ansiedad
    if Hipocondria=="1":
        hipocondria=hipocondria4/Total_Ansiedad
    if Hipocondria=="2":
        hipocondria=hipocondria6/Total_Ansiedad
    if Hipocondria=="3":
        hipocondria=hipocondria8/Total_Ansiedad
    if Hipocondria=="4":
        hipocondria=hipocondria10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Peso
# =============================================================================
    if Peso=="0":
        peso=peso2/Total_Ansiedad
    if Peso=="1":
        peso=peso4/Total_Ansiedad
    if Peso=="2":
        peso=peso6/Total_Ansiedad
    if Peso=="3":
        peso=peso8/Total_Ansiedad    
    if Peso=="4":
        peso=peso10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Instrospeccion
# =============================================================================
    if Introspeccion=="0":
        introspeccion=introspeccion2/Total_Ansiedad
    if Introspeccion=="1":
        introspeccion=introspeccion4/Total_Ansiedad
    if Introspeccion=="2":
        introspeccion=introspeccion6/Total_Ansiedad
    if Introspeccion=="3":
        introspeccion=introspeccion8/Total_Ansiedad
    if Introspeccion=="4":
        introspeccion=introspeccion10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Animo Ansioso
# =============================================================================
    if AnimoAnsioso=="0":
        animoansioso=animoansioso2/Total_Ansiedad
    if AnimoAnsioso=="1":
        animoansioso=animoansioso4/Total_Ansiedad
    if AnimoAnsioso=="2":
        animoansioso=animoansioso6/Total_Ansiedad
    if AnimoAnsioso=="3":
        animoansioso=animoansioso8/Total_Ansiedad
    if AnimoAnsioso=="4":
        animoansioso=animoansioso10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Tension
# =============================================================================
    if Tension=="0":
        tension=tension2/Total_Ansiedad
    if Tension=="1":
        tension=tension4/Total_Ansiedad
    if Tension=="2":
        tension=tension6/Total_Ansiedad
    if Tension=="3":
        tension=tension8/Total_Ansiedad
    if Tension=="4":
        tension=tension10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Temores
# =============================================================================
    if Temores=="0":
        temores=temores2/Total_Ansiedad
    if Temores=="1":
        temores=temores4/Total_Ansiedad
    if Temores=="2":
        temores=temores6/Total_Ansiedad
    if Temores=="3":
        temores=temores8/Total_Ansiedad
    if Temores=="4":
        temores=temores10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Insomnio
# =============================================================================
    if Insomnio=="0":
        insomnio=insomnio2/Total_Ansiedad
    if Insomnio=="1":
        insomnio=insomnio4/Total_Ansiedad
    if Insomnio=="2":
        insomnio=insomnio6/Total_Ansiedad
    if Insomnio=="3":
        insomnio=insomnio8/Total_Ansiedad
    if Insomnio=="4":
        insomnio=insomnio10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Intelectual
# =============================================================================
    if Intelectual=="0":
        intelectual=intelectual2/Total_Ansiedad
    if Intelectual=="1":
        intelectual=intelectual4/Total_Ansiedad
    if Intelectual=="2":
        intelectual=intelectual6/Total_Ansiedad
    if Intelectual=="3":
        intelectual=intelectual8/Total_Ansiedad
    if Intelectual=="4":
        intelectual=intelectual10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Animo Deprimido
# =============================================================================
    if AnimoDeprimido=="0":
        animodeprimido=animodeprimido2/Total_Ansiedad
    if AnimoDeprimido=="1":
        animodeprimido=animodeprimido4/Total_Ansiedad
    if AnimoDeprimido=="2":
        animodeprimido=animodeprimido6/Total_Ansiedad
    if AnimoDeprimido=="3":
        animodeprimido=animodeprimido8/Total_Ansiedad
    if AnimoDeprimido=="4":
        animodeprimido=animodeprimido10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Somaticos Musculares
# =============================================================================
    if SomaticosMusculares=="0":
        somusculares=somaticosmusculares2/Total_Ansiedad
    if SomaticosMusculares=="1":
        somusculares=somaticosmusculares4/Total_Ansiedad
    if SomaticosMusculares=="2":
        somusculares=somaticosmusculares6/Total_Ansiedad
    if SomaticosMusculares=="3":
        somusculares=somaticosmusculares8/Total_Ansiedad
    if SomaticosMusculares=="4":
        somusculares=somaticosmusculares10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Somaticos Sensoriales
# =============================================================================
    if SomaticosSensoriales=="0":
        sosensoriales=somaticossensoriales2/Total_Ansiedad
    if SomaticosSensoriales=="1":
        sosensoriales=somaticossensoriales4/Total_Ansiedad
    if SomaticosSensoriales=="2":
        sosensoriales=somaticossensoriales6/Total_Ansiedad
    if SomaticosSensoriales=="3":
        sosensoriales=somaticossensoriales8/Total_Ansiedad
    if SomaticosSensoriales=="4":
        sosensoriales=somaticossensoriales10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Cardiovasculares
# =============================================================================
    if Cardiovasculares=="0":
        cardiovasculares=cardiovasculares2/Total_Ansiedad
    if Cardiovasculares=="1":
        cardiovasculares=cardiovasculares4/Total_Ansiedad
    if Cardiovasculares=="2":
        cardiovasculares=cardiovasculares6/Total_Ansiedad
    if Cardiovasculares=="3":
        cardiovasculares=cardiovasculares8/Total_Ansiedad
    if Cardiovasculares=="4":
        cardiovasculares=cardiovasculares10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Respiratorios
# =============================================================================
    if Respiratorios=="0":
        respiratorios=respiratorios2/Total_Ansiedad
    if Respiratorios=="1":
        respiratorios=respiratorios4/Total_Ansiedad
    if Respiratorios=="2":
        respiratorios=respiratorios6/Total_Ansiedad
    if Respiratorios=="3":
        respiratorios=respiratorios8/Total_Ansiedad
    if Respiratorios=="4":
        respiratorios=respiratorios10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Gastrointestinales
# =============================================================================
    if Gastrointestinales=="0":
        agastrointestinales=gastrointestinales2/Total_Ansiedad
    if Gastrointestinales=="1":
        agastrointestinales=gastrointestinales4/Total_Ansiedad
    if Gastrointestinales=="2":
        agastrointestinales=gastrointestinales6/Total_Ansiedad
    if Gastrointestinales=="3":
        agastrointestinales=gastrointestinales8/Total_Ansiedad
    if Gastrointestinales=="4":
        agastrointestinales=gastrointestinales10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Genitourinarios
# =============================================================================
    if Genitourinarios=="0":
        genitourinarios=genitourionarios2/Total_Ansiedad
    if Genitourinarios=="1":
        genitourinarios=genitourionarios4/Total_Ansiedad
    if Genitourinarios=="2":
        genitourinarios=genitourionarios6/Total_Ansiedad
    if Genitourinarios=="3":
        genitourinarios=genitourionarios8/Total_Ansiedad
    if Genitourinarios=="4":
        genitourinarios=genitourionarios10/Total_Ansiedad
# =============================================================================
#     #Seleccion de Autonomos
# =============================================================================
    if Autonomos=="0":
        autonomos=autonomos2/Total_Ansiedad
    if Autonomos=="1":
        autonomos=autonomos4/Total_Ansiedad
    if Autonomos=="2":
        autonomos=autonomos6/Total_Ansiedad
    if Autonomos=="3":
        autonomos=autonomos8/Total_Ansiedad
    if Autonomos=="4":
        autonomos=autonomos10/Total_Ansiedad
        
    Calculo_PC2=((pc2/Total_Datos)*(humor* culpa* suicidio* iprecoz* iintermedio* itardio* trabajo* inhibicion* agitacion* apsiquica* asomatica* sgastrointestinales* sgenerales* sgenitales* hipocondria* peso* introspeccion* animoansioso* tension* temores* insomnio* intelectual* animodeprimido* somusculares* sosensoriales* cardiovasculares* respiratorios* agastrointestinales* genitourinarios* autonomos))
    return Calculo_PC2  