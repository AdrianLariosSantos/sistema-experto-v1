#Importación de los modulos
from flask import Flask, redirect, url_for, render_template, request, make_response
from flask_mysqldb import MySQL
from flask.templating import render_template_string
from AlgoritmoBayes import *
#import matplotlib.pyplot as plt

string_connection = 'mysql+pymysql://root@localhost:3306/escalahamilton'
connection = create_engine(string_connection)
sql = 'SELECT * FROM conocimiento'
datos = pd.read_sql_query(sql, connection)
df = pd.DataFrame(datos)
print(df)

app = Flask(__name__)

# Estableciendo la conexion con la base de datos.
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'escalahamilton'

mysql = MySQL(app)

Resultado_Final = ""

#Página principal
@app.route('/')
def home():
    return render_template('Index.html')


@app.route('/Test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        # Primero dos datos.
        genero = request.form.getlist('Genero')
        edad = request.form.getlist('Edad')

        # Cuestionario de los Sintomas de la Depresion.
        humordepresivo = str(request.form.getlist('Humordepresivo')[0])
        sentimientoculpa = str(request.form.getlist('Sentimientoculpa')[0])
        suicidio = str(request.form.getlist('Suicidio')[0])
        insomnioprecoz = str(request.form.getlist('Insomnioprecoz')[0])
        insomniointermedio = str(request.form.getlist('Insomniointermedio')[0])
        insomniotardio = str(request.form.getlist('Insomniotardio')[0])
        trabajo = str(request.form.getlist('Trabajoactividades')[0])
        inhibicion = str(request.form.getlist('Inhibicionpsicomotora')[0])
        agitacion = str(request.form.getlist('Agitacionpsicomotora')[0])
        ansiedadpsiquica = str(request.form.getlist('Ansiedadpsiquica')[0])
        ansiedadsomatica = str(request.form.getlist('Ansiedadsomatica')[0])
        somaticosgastrointestinales = str(request.form.getlist('Somaticosgastrointestinales')[0])
        somaticosgenerales = str(request.form.getlist('Somaticosgenerales')[0])
        genitales = str(request.form.getlist('Genitales')[0])
        hipocondria = str(request.form.getlist('Hipocondria')[0])
        peso = str(request.form.getlist('Peso')[0])
        introspeccion = str(request.form.getlist('Introspeccion')[0])

        # Cuestionario de los Sintomas de la Ansiedad
        estadoansioso = str(request.form.getlist('Estadoansioso')[0])
        tension = str(request.form.getlist('Tension')[0])
        temores = str(request.form.getlist('Temores')[0])
        insomnio = str(request.form.getlist('Insomnio')[0])
        intelectual = str(request.form.getlist('Intelectual')[0])
        estadodeprimido = str(request.form.getlist('Estadodeprimido')[0])
        musculares = str(request.form.getlist('Musculares')[0])
        sensoriales = str(request.form.getlist('Sensoriales')[0])
        cardiovasculares = str(request.form.getlist('Cardiovasculares')[0])
        respiratorios = str(request.form.getlist('Respiratorios')[0])
        gastrointestinales = str(request.form.getlist('Gastrointestinales')[0])
        genitourinarios = str(request.form.getlist('Genitourinarios')[0])
        autonomos = str(request.form.getlist('Autonomos')[0])

        # Algoritmo de Bayes Ingenuo
        ListaPC1 = []
        ListaPC2 = []

        clase_Depresion(humordepresivo, sentimientoculpa, suicidio, insomnioprecoz, insomniointermedio, insomniotardio, trabajo, inhibicion, agitacion, ansiedadpsiquica, ansiedadsomatica, somaticosgastrointestinales, somaticosgenerales,
                        genitales, hipocondria, peso, introspeccion, estadoansioso, tension, temores, insomnio, intelectual, estadodeprimido, musculares, sensoriales, cardiovasculares, respiratorios, gastrointestinales, genitourinarios, autonomos)
        ListaPC1.append(clase_Depresion(humordepresivo, sentimientoculpa, suicidio, insomnioprecoz, insomniointermedio, insomniotardio, trabajo, inhibicion, agitacion, ansiedadpsiquica, ansiedadsomatica, somaticosgastrointestinales, somaticosgenerales,
                        genitales, hipocondria, peso, introspeccion, estadoansioso, tension, temores, insomnio, intelectual, estadodeprimido, musculares, sensoriales, cardiovasculares, respiratorios, gastrointestinales, genitourinarios, autonomos))

        clase_Ansiedad(humordepresivo, sentimientoculpa, suicidio, insomnioprecoz, insomniointermedio, insomniotardio, trabajo, inhibicion, agitacion, ansiedadpsiquica, ansiedadsomatica, somaticosgastrointestinales, somaticosgenerales,
                       genitales, hipocondria, peso, introspeccion, estadoansioso, tension, temores, insomnio, intelectual, estadodeprimido, musculares, sensoriales, cardiovasculares, respiratorios, gastrointestinales, genitourinarios, autonomos)
        ListaPC2.append(clase_Ansiedad(humordepresivo, sentimientoculpa, suicidio, insomnioprecoz, insomniointermedio, insomniotardio, trabajo, inhibicion, agitacion, ansiedadpsiquica, ansiedadsomatica, somaticosgastrointestinales, somaticosgenerales,
                        genitales, hipocondria, peso, introspeccion, estadoansioso, tension, temores, insomnio, intelectual, estadodeprimido, musculares, sensoriales, cardiovasculares, respiratorios, gastrointestinales, genitourinarios, autonomos))

        print("\n\nEl valor de P(C1) es: {}".format(ListaPC1),
              "\n\nEl valor del P(C2) es: {}".format(ListaPC2))

        Sumatoria = ListaPC1[0] + ListaPC2[0]

        print("\nLa sumatoria de P(C1) + P(C2) es: {}".format(Sumatoria))

        # Calculo de la Probabilidad

        Probabilidad_PC1 = ListaPC1[0]/Sumatoria

        Probabilidad_PC2 = ListaPC2[0]/Sumatoria
        
        Pro_PC1 = ""
        Pro_PC2 = ""

        print("\nEl calculo para la probabilidad de P(C1) es de: {}".format(Probabilidad_PC1),
              "\nEl calculo para la probabilidad de P(C2) es de: {}".format(Probabilidad_PC2))

        if Probabilidad_PC1 > Probabilidad_PC2:
            print("\nLa probabilidad de P(C1) es de: {:.2f}".format(Probabilidad_PC1 * 100), "%", " por lo tanto padece de Depresion.")
            Resultado_Final = "Depresion"
        else:
            print("\nLa probabilidad de P(C2) es de: {:.2f}".format(Probabilidad_PC2 * 100), "%", " por lo tanto padece de Ansiedad.")
            Resultado_Final = "Ansiedad"

        # Se realiza la conexion.
        cur = mysql.connection.cursor()
        # Se executa el comando insert para guardar los nuevos datos introducidos por el usuario
        cur.execute('INSERT INTO conocimiento (Genero, Edad, Humor, Culpa, Suicidio, IPrecoz, IIntermedio, ITardio, Trabajo, Inhibicion, Agitacion, APsiquica, ASomatica, SGastrointestinales, SGenerales, SGenitales, Hipocondria, Peso, Introspeccion, AnimoAnsioso, Tension, Temores, Insomnio, Intelectual, AnimoDeprimido, SomaticosMusculares, SomaticosSensoriales, Cardiovasculares, Respiratorios, Gastrointestinales, Genitourinarios, Autonomos, Clase) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s)',
                    (genero, edad, humordepresivo, sentimientoculpa, suicidio, insomnioprecoz, insomniointermedio, insomniotardio, trabajo, inhibicion, agitacion, ansiedadpsiquica, ansiedadsomatica, somaticosgastrointestinales, somaticosgenerales, genitales, hipocondria, peso, introspeccion, estadoansioso, tension, temores, insomnio, intelectual, estadodeprimido, musculares, sensoriales, cardiovasculares, respiratorios, gastrointestinales, genitourinarios, autonomos, Resultado_Final))

        # Se ejecuta con el comando con el metodo commit
        mysql.connection.commit()
        
        return render_template('Ayuda.html', Resultado_Final = Resultado_Final)
        
    return render_template('Test.html')




@app.route('/Ayuda')
def ayuda(Resultado_Final):
    return render_template('Ayuda.html')


@app.route('/Contacto')
def contacto():
    return render_template('Contacto.html')


if __name__ == '__main__':

    app.run(port=5000, debug=True)
