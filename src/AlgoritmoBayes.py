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

def _select_prob(value, counts, total):
    try:
        idx = int(value)
    except (TypeError, ValueError):
        return 0
    if idx < 0 or idx >= len(counts) or total == 0:
        return 0
    return counts[idx] / total

def clase_Depresion(Humor,Culpa,Suicidio,IPrecoz,IIntermedio,ITardio,Trabajo,Inhibicion,Agitacion,APsiquica,ASomatica,SGastrointestinales,SGenerales,SGenitales,Hipocondria,Peso,Introspeccion,AnimoAnsioso,Tension,Temores,Insomnio,Intelectual,AnimoDeprimido,SomaticosMusculares,SomaticosSensoriales,Cardiovasculares,Respiratorios,Gastrointestinales,Genitourinarios,Autonomos):
    humor = _select_prob(Humor, (humor1, humor3, humor5, humor7, humor9), Total_Depresion)
    culpa = _select_prob(Culpa, (culpa1, culpa3, culpa5, culpa7, culpa9), Total_Depresion)
    suicidio = _select_prob(Suicidio, (suicidio1, suicidio3, suicidio5, suicidio7, suicidio9), Total_Depresion)
    iprecoz = _select_prob(IPrecoz, (insomnioprecoz1, insomnioprecoz3, insomnioprecoz5, insomnioprecoz7, insomnioprecoz9), Total_Depresion)
    iintermedio = _select_prob(IIntermedio, (insomniointermedio1, insomniointermedio3, insomniointermedio5, insomniointermedio7, insomniointermedio9), Total_Depresion)
    itardio = _select_prob(ITardio, (insomniotardio1, insomniotardio3, insomniotardio5, insomniotardio7, insomniotardio9), Total_Depresion)
    trabajo = _select_prob(Trabajo, (trabajo1, trabajo3, trabajo5, trabajo7, trabajo9), Total_Depresion)
    inhibicion = _select_prob(Inhibicion, (inhibicion1, inhibicion3, inhibicion5, inhibicion7, inhibicion9), Total_Depresion)
    agitacion = _select_prob(Agitacion, (agitacion1, agitacion3, agitacion5, agitacion7, agitacion9), Total_Depresion)
    apsiquica = _select_prob(APsiquica, (psiquica1, psiquica3, psiquica5, psiquica7, psiquica9), Total_Depresion)
    asomatica = _select_prob(ASomatica, (somatica1, somatica3, somatica5, somatica7, somatica9), Total_Depresion)
    sgastrointestinales = _select_prob(SGastrointestinales, (sgastrointestinales1, sgastrointestinales3, sgastrointestinales5, sgastrointestinales7, sgastrointestinales9), Total_Depresion)
    sgenerales = _select_prob(SGenerales, (sgenerales1, sgenerales3, sgenerales5, sgenerales7, sgenerales9), Total_Depresion)
    sgenitales = _select_prob(SGenitales, (sgenitales1, sgenitales3, sgenitales5, sgenitales7, sgenitales9), Total_Depresion)
    hipocondria = _select_prob(Hipocondria, (hipocondria1, hipocondria3, hipocondria5, hipocondria7, hipocondria9), Total_Depresion)
    peso = _select_prob(Peso, (peso1, peso3, peso5, peso7, peso9), Total_Depresion)
    introspeccion = _select_prob(Introspeccion, (introspeccion1, introspeccion3, introspeccion5, introspeccion7, introspeccion9), Total_Depresion)
    animoansioso = _select_prob(AnimoAnsioso, (animoansioso1, animoansioso3, animoansioso5, animoansioso7, animoansioso9), Total_Depresion)
    tension = _select_prob(Tension, (tension1, tension3, tension5, tension7, tension9), Total_Depresion)
    temores = _select_prob(Temores, (temores1, temores3, temores5, temores7, temores9), Total_Depresion)
    insomnio = _select_prob(Insomnio, (insomnio1, insomnio3, insomnio5, insomnio7, insomnio9), Total_Depresion)
    intelectual = _select_prob(Intelectual, (intelectual1, intelectual3, intelectual5, intelectual7, intelectual9), Total_Depresion)
    animodeprimido = _select_prob(AnimoDeprimido, (animodeprimido1, animodeprimido3, animodeprimido5, animodeprimido7, animodeprimido9), Total_Depresion)
    somusculares = _select_prob(SomaticosMusculares, (somaticosmusculares1, somaticosmusculares3, somaticosmusculares5, somaticosmusculares7, somaticosmusculares9), Total_Depresion)
    sosensoriales = _select_prob(SomaticosSensoriales, (somaticossensoriales1, somaticossensoriales3, somaticossensoriales5, somaticossensoriales7, somaticossensoriales9), Total_Depresion)
    cardiovasculares = _select_prob(Cardiovasculares, (cardiovasculares1, cardiovasculares3, cardiovasculares5, cardiovasculares7, cardiovasculares9), Total_Depresion)
    respiratorios = _select_prob(Respiratorios, (respiratorios1, respiratorios3, respiratorios5, respiratorios7, respiratorios9), Total_Depresion)
    agastrointestinales = _select_prob(Gastrointestinales, (gastrointestinales1, gastrointestinales3, gastrointestinales5, gastrointestinales7, gastrointestinales9), Total_Depresion)
    genitourinarios = _select_prob(Genitourinarios, (genitourionarios1, genitourionarios3, genitourionarios5, genitourionarios7, genitourionarios9), Total_Depresion)
    autonomos = _select_prob(Autonomos, (autonomos1, autonomos3, autonomos5, autonomos7, autonomos9), Total_Depresion)
    
    Calculo_PC1=((pc1/Total_Datos)*(humor* culpa* suicidio* iprecoz* iintermedio* itardio* trabajo* inhibicion* agitacion* apsiquica* asomatica* sgastrointestinales* sgenerales* sgenitales* hipocondria* peso* introspeccion* animoansioso* tension* temores* insomnio* intelectual* animodeprimido* somusculares* sosensoriales* cardiovasculares* respiratorios* agastrointestinales* genitourinarios* autonomos))
    return Calculo_PC1        


def clase_Ansiedad(Humor,Culpa,Suicidio,IPrecoz,IIntermedio,ITardio,Trabajo,Inhibicion,Agitacion,APsiquica,ASomatica,SGastrointestinales,SGenerales,SGenitales,Hipocondria,Peso,Introspeccion,AnimoAnsioso,Tension,Temores,Insomnio,Intelectual,AnimoDeprimido,SomaticosMusculares,SomaticosSensoriales,Cardiovasculares,Respiratorios,Gastrointestinales,Genitourinarios,Autonomos):
    humor = _select_prob(Humor, (humor2, humor4, humor6, humor8, humor10), Total_Ansiedad)
    culpa = _select_prob(Culpa, (culpa2, culpa4, culpa6, culpa8, culpa10), Total_Ansiedad)
    suicidio = _select_prob(Suicidio, (suicidio2, suicidio4, suicidio6, suicidio8, suicidio10), Total_Ansiedad)
    iprecoz = _select_prob(IPrecoz, (insomnioprecoz2, insomnioprecoz4, insomnioprecoz6, insomnioprecoz8, insomnioprecoz10), Total_Ansiedad)
    iintermedio = _select_prob(IIntermedio, (insomniointermedio2, insomniointermedio4, insomniointermedio6, insomniointermedio8, insomniointermedio10), Total_Ansiedad)
    itardio = _select_prob(ITardio, (insomniotardio2, insomniotardio4, insomniotardio6, insomniotardio8, insomniotardio10), Total_Ansiedad)
    trabajo = _select_prob(Trabajo, (trabajo2, trabajo4, trabajo6, trabajo8, trabajo10), Total_Ansiedad)
    inhibicion = _select_prob(Inhibicion, (inhibicion2, inhibicion4, inhibicion6, inhibicion8, inhibicion10), Total_Ansiedad)
    agitacion = _select_prob(Agitacion, (agitacion2, agitacion4, agitacion6, agitacion8, agitacion10), Total_Ansiedad)
    apsiquica = _select_prob(APsiquica, (psiquica2, psiquica4, psiquica6, psiquica8, psiquica10), Total_Ansiedad)
    asomatica = _select_prob(ASomatica, (somatica2, somatica4, somatica6, somatica8, somatica10), Total_Ansiedad)
    sgastrointestinales = _select_prob(SGastrointestinales, (sgastrointestinales2, sgastrointestinales4, sgastrointestinales6, sgastrointestinales8, sgastrointestinales10), Total_Ansiedad)
    sgenerales = _select_prob(SGenerales, (sgenerales2, sgenerales4, sgenerales6, sgenerales8, sgenerales10), Total_Ansiedad)
    sgenitales = _select_prob(SGenitales, (sgenitales2, sgenitales4, sgenitales6, sgenitales8, sgenitales10), Total_Ansiedad)
    hipocondria = _select_prob(Hipocondria, (hipocondria2, hipocondria4, hipocondria6, hipocondria8, hipocondria10), Total_Ansiedad)
    peso = _select_prob(Peso, (peso2, peso4, peso6, peso8, peso10), Total_Ansiedad)
    introspeccion = _select_prob(Introspeccion, (introspeccion2, introspeccion4, introspeccion6, introspeccion8, introspeccion10), Total_Ansiedad)
    animoansioso = _select_prob(AnimoAnsioso, (animoansioso2, animoansioso4, animoansioso6, animoansioso8, animoansioso10), Total_Ansiedad)
    tension = _select_prob(Tension, (tension2, tension4, tension6, tension8, tension10), Total_Ansiedad)
    temores = _select_prob(Temores, (temores2, temores4, temores6, temores8, temores10), Total_Ansiedad)
    insomnio = _select_prob(Insomnio, (insomnio2, insomnio4, insomnio6, insomnio8, insomnio10), Total_Ansiedad)
    intelectual = _select_prob(Intelectual, (intelectual2, intelectual4, intelectual6, intelectual8, intelectual10), Total_Ansiedad)
    animodeprimido = _select_prob(AnimoDeprimido, (animodeprimido2, animodeprimido4, animodeprimido6, animodeprimido8, animodeprimido10), Total_Ansiedad)
    somusculares = _select_prob(SomaticosMusculares, (somaticosmusculares2, somaticosmusculares4, somaticosmusculares6, somaticosmusculares8, somaticosmusculares10), Total_Ansiedad)
    sosensoriales = _select_prob(SomaticosSensoriales, (somaticossensoriales2, somaticossensoriales4, somaticossensoriales6, somaticossensoriales8, somaticossensoriales10), Total_Ansiedad)
    cardiovasculares = _select_prob(Cardiovasculares, (cardiovasculares2, cardiovasculares4, cardiovasculares6, cardiovasculares8, cardiovasculares10), Total_Ansiedad)
    respiratorios = _select_prob(Respiratorios, (respiratorios2, respiratorios4, respiratorios6, respiratorios8, respiratorios10), Total_Ansiedad)
    agastrointestinales = _select_prob(Gastrointestinales, (gastrointestinales2, gastrointestinales4, gastrointestinales6, gastrointestinales8, gastrointestinales10), Total_Ansiedad)
    genitourinarios = _select_prob(Genitourinarios, (genitourionarios2, genitourionarios4, genitourionarios6, genitourionarios8, genitourionarios10), Total_Ansiedad)
    autonomos = _select_prob(Autonomos, (autonomos2, autonomos4, autonomos6, autonomos8, autonomos10), Total_Ansiedad)
        
    Calculo_PC2=((pc2/Total_Datos)*(humor* culpa* suicidio* iprecoz* iintermedio* itardio* trabajo* inhibicion* agitacion* apsiquica* asomatica* sgastrointestinales* sgenerales* sgenitales* hipocondria* peso* introspeccion* animoansioso* tension* temores* insomnio* intelectual* animodeprimido* somusculares* sosensoriales* cardiovasculares* respiratorios* agastrointestinales* genitourinarios* autonomos))
    return Calculo_PC2  