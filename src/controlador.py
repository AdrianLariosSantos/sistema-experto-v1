#Importación de los modulos
import os
from flask import Flask, redirect, url_for, render_template, request, make_response
from flask_mysqldb import MySQL
try:
    from dotenv import load_dotenv
except Exception:
    try:
        from dotenv.main import load_dotenv
    except Exception as exc:
        raise RuntimeError(
            "No se encontró load_dotenv. Instala 'python-dotenv' y desinstala el paquete 'dotenv' si existe."
        ) from exc
from bayes_model import clase_Ansiedad, clase_Depresion
#import matplotlib.pyplot as plt

load_dotenv()

app = Flask(__name__)

# Estableciendo la conexion con la base de datos.
app.config['MYSQL_HOST'] = os.getenv('DB_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('DB_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD', '')
app.config['MYSQL_DB'] = os.getenv('DB_NAME', 'escalahamilton')
app.config['MYSQL_PORT'] = int(os.getenv('DB_PORT', '3306'))

mysql = MySQL(app)

Resultado_Final = ""

#Página principal
@app.route('/')
def home():
    return render_template('Index.html')


@app.route('/Test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        def get_value(key):
            value = request.form.get(key)
            if value is None or value == "":
                return None
            return str(value)

        # Primero dos datos.
        genero = get_value('Genero')
        edad = get_value('Edad')

        # Cuestionario de los Sintomas de la Depresion.
        humordepresivo = get_value('Humordepresivo')
        sentimientoculpa = get_value('Sentimientoculpa')
        suicidio = get_value('Suicidio')
        insomnioprecoz = get_value('Insomnioprecoz')
        insomniointermedio = get_value('Insomniointermedio')
        insomniotardio = get_value('Insomniotardio')
        trabajo = get_value('Trabajoactividades')
        inhibicion = get_value('Inhibicionpsicomotora')
        agitacion = get_value('Agitacionpsicomotora')
        ansiedadpsiquica = get_value('Ansiedadpsiquica')
        ansiedadsomatica = get_value('Ansiedadsomatica')
        somaticosgastrointestinales = get_value('Somaticosgastrointestinales')
        somaticosgenerales = get_value('Somaticosgenerales')
        genitales = get_value('Genitales')
        hipocondria = get_value('Hipocondria')
        peso = get_value('Peso')
        introspeccion = get_value('Introspeccion')

        # Cuestionario de los Sintomas de la Ansiedad
        estadoansioso = get_value('Estadoansioso')
        tension = get_value('Tension')
        temores = get_value('Temores')
        insomnio = get_value('Insomnio')
        intelectual = get_value('Intelectual')
        estadodeprimido = get_value('Estadodeprimido')
        musculares = get_value('Musculares')
        sensoriales = get_value('Sensoriales')
        cardiovasculares = get_value('Cardiovasculares')
        respiratorios = get_value('Respiratorios')
        gastrointestinales = get_value('Gastrointestinales')
        genitourinarios = get_value('Genitourinarios')
        autonomos = get_value('Autonomos')

        required_values = [
            genero, edad, humordepresivo, sentimientoculpa, suicidio, insomnioprecoz, insomniointermedio,
            insomniotardio, trabajo, inhibicion, agitacion, ansiedadpsiquica, ansiedadsomatica,
            somaticosgastrointestinales, somaticosgenerales, genitales, hipocondria, peso, introspeccion,
            estadoansioso, tension, temores, insomnio, intelectual, estadodeprimido, musculares, sensoriales,
            cardiovasculares, respiratorios, gastrointestinales, genitourinarios, autonomos
        ]

        if any(value is None for value in required_values):
            return render_template('Test.html', error='Completa todas las preguntas para continuar.'), 400

        # Algoritmo de Bayes Ingenuo
        ListaPC1 = []
        ListaPC2 = []

        ListaPC1.append(clase_Depresion(humordepresivo, sentimientoculpa, suicidio, insomnioprecoz, insomniointermedio, insomniotardio, trabajo, inhibicion, agitacion, ansiedadpsiquica, ansiedadsomatica, somaticosgastrointestinales, somaticosgenerales,
                genitales, hipocondria, peso, introspeccion, estadoansioso, tension, temores, insomnio, intelectual, estadodeprimido, musculares, sensoriales, cardiovasculares, respiratorios, gastrointestinales, genitourinarios, autonomos))

        ListaPC2.append(clase_Ansiedad(humordepresivo, sentimientoculpa, suicidio, insomnioprecoz, insomniointermedio, insomniotardio, trabajo, inhibicion, agitacion, ansiedadpsiquica, ansiedadsomatica, somaticosgastrointestinales, somaticosgenerales,
                genitales, hipocondria, peso, introspeccion, estadoansioso, tension, temores, insomnio, intelectual, estadodeprimido, musculares, sensoriales, cardiovasculares, respiratorios, gastrointestinales, genitourinarios, autonomos))

        Sumatoria = ListaPC1[0] + ListaPC2[0]

        # Calculo de la Probabilidad

        Probabilidad_PC1 = ListaPC1[0]/Sumatoria

        Probabilidad_PC2 = ListaPC2[0]/Sumatoria
        
        if Probabilidad_PC1 > Probabilidad_PC2:
            Resultado_Final = "Depresion"
        else:
            Resultado_Final = "Ansiedad"

        # Se realiza la conexion.
        with mysql.connection.cursor() as cur:
            # Se executa el comando insert para guardar los nuevos datos introducidos por el usuario
            cur.execute('INSERT INTO conocimiento (Genero, Edad, Humor, Culpa, Suicidio, IPrecoz, IIntermedio, ITardio, Trabajo, Inhibicion, Agitacion, APsiquica, ASomatica, SGastrointestinales, SGenerales, SGenitales, Hipocondria, Peso, Introspeccion, AnimoAnsioso, Tension, Temores, Insomnio, Intelectual, AnimoDeprimido, SomaticosMusculares, SomaticosSensoriales, Cardiovasculares, Respiratorios, Gastrointestinales, Genitourinarios, Autonomos, Clase) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s)',
                        (genero, edad, humordepresivo, sentimientoculpa, suicidio, insomnioprecoz, insomniointermedio, insomniotardio, trabajo, inhibicion, agitacion, ansiedadpsiquica, ansiedadsomatica, somaticosgastrointestinales, somaticosgenerales, genitales, hipocondria, peso, introspeccion, estadoansioso, tension, temores, insomnio, intelectual, estadodeprimido, musculares, sensoriales, cardiovasculares, respiratorios, gastrointestinales, genitourinarios, autonomos, Resultado_Final))
            # Se ejecuta con el comando con el metodo commit
            mysql.connection.commit()
        
        return render_template('Ayuda.html', Resultado_Final = Resultado_Final)
        
    return render_template('Test.html')




@app.route('/Ayuda')
def ayuda():
    return render_template('Ayuda.html')


@app.route('/Contacto')
def contacto():
    return render_template('Contacto.html')


if __name__ == '__main__':

    app.run(port=5000, debug=True)
