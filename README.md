# AAPP-Tweet
Proyecto sobre los parámetros de la dieta mediática de los seguidores de Twitter del Ayuntamiento de Valencia

1. Título: Análisis de los parámetros de la dieta mediática de los seguidores de Twitter del Ayuntamiento de Valencia

2. Introducción. Se indica el objetivo del proyecto, el problema a resolver y el contexto del mismo.

    El principal objetivo del proyecto, es el diseño e implementación de una herramienta, que mediante el uso de herramientas externas, permita realizar los procesos de obtención, limpieza y presentación de datos sobre la información de seguidores de una cuenta de Twitter de cualquier administración pública.

    El análisis de estos seguidores, aportará una información valiosa a las administraciones para poder encauzar la toma de decisiones en políticas de comunicación y otras políticas. Se podrá llegar y satisfacer a una parte de su público, que son los ciudadanos que interactúan vía Twitter con las cuentas de las administraciones.

    Este proyecto se desarrolla en el contexto actual en el que el uso de las núevas tecnologías y el acceso a las redes sociales está al alance de cualquiera. Este hecho, sumado a la importancia de la transparencia de las insitituciones y la participación ciudadana da pie a proyectos como el presente, proyectos que buscan mostrar información sobre la ciudadania que es gobernada para poder acertar a la hora de la toma de decisiones.

3. Descripción de la solución planteada.

    Se propone un análisis de la dieta mediática de cada seguidor que se basará en las cuentas de periódicos seguidas

    Esta es la clasificación de los periódicos

    - Derecha: Expansión, ABC, El Confidencial
    - Centro derecha: El Imparcial, El Economista, La Gaceta
    - Centro: El mundo, 20 Minutos, El Español
    - Centro izquierda: El Pais, El Huffington Post, El Plural
    - Izquierda: Público, infolibre, eldiario.es

    Se ha realizado a partir de este estudio: https://smreputationmetrics.wordpress.com/2015/12/09/el-perfil-ideologico-de-los-lectores-de-prensa-analisis-encuestas-7deldebatedecisivo/

    Los parámetros de la dieta mediática son los siguientes:

    Dieta mediática                    
    Análisis individual:                                 
       Balance: Consume el mismo número de medios de un sentido que de otro.           
            Respuestas:    
                - Sí
                - No: - Balanceo a derechas.    
                      - Balanceo a izquierdas.

      Equilibrio: Consume al menos 1 medio de cada grupo.
            Respuestas:    Sí, No                    

      Saturación: Número de medios seguidos     
            Respuestas:    
                - monosaturada: <=5
                - saturada: >=6 y <=9
                - polisaturada: >=10


    Para obtener los seguidores se plantea desarrollar un módulo que descargue los seguidores mediante API de una cuenta de Twitter y los almacene en una base de datos. Fichero: apiToMongoDb.py

    Para obtener los resultados de los parámetros del análisis de la dieta mediática, se plantea desarrollar un módulo que:
    1. Accede a los usuarios previamente almacenados
    2. Via TwitterAPI, accederá a cada uno de los ususarios para recuperar las cuentas a las que sigue y establecer el valor de los parámetros de saturación, equilibrio y balanceo. Fichero: dataProcess.py
    3. Se toma el fichero CSV genearado por dataProcess.py como fuente de datos para proceder al montaje de la visualización utilizando Tableau.
    4. Se analizan los resultados y se extraen conclusiones.


4. Metodología.
    1. Análisis y definición: definición del proyecto (DEFINE), Caracterización del público objetivo; estudio de la estructura del objeto JSON que contiene datos del usuario (FIND); estudio del rate-limit y predicción de coste de computo.
    2. Diseño: diseño de los módulos de tratamiento de datos; configuración cuenta consumidora TwitterAPI; Diseño visualizaciones; clasificación ideológica de los periódicos.
    3. Implementación: implementación de la base de datos; implementación apiToMongoDb.py; implementación dataProcess.py;
    4. GET: creación de los conjuntos de datos (usuarios y dieta)
    5. Analyse: análisis para la consecución del proyecto
    6. Present: presentación de los resultados obtenidos

5. Resultados.
    Tras la recogida de datos, se ha pasado a la implementación del módulo de presentación. Para la realización de este módulo, que se encargargará de la visualización de estos datos recogidos, se utilizará la herramienta de visualización Tableau. Este módulo consiste en una historia que contiene dos cuadros de mandos. A continuación, se entra en detalle sobre los gráficos qué se incorporan en cada uno de los cuadros de mando.

    Historia
        Título: Visualización de los parámetros de la dieta mediática de los seguidores de la cuenta de Twitter del Ayuntamiento de Valencia
        
      Cuadro de mando 1
      
            Título: Resultados generales
            Gráfico 1
                Se muestra el número de individuos de la muestra, población y fecha del análisis.
            Gráfico 2
                Se muestra en un diagrama de barras el número de seguidores del ayuntamiento que sigue a cada periódico.
            Gráfico 3
                Se muestran los parámetros de balanceo, saturación y equilibrio en todas las posibles combinaciones de la dieta mediática. Con este gráfico, se puede ver a simple golpe de vista cuál es el patrón de dieta mediática que más se repite en la muestra.
   
   Resultados
        -En nuestro caso, el público se caracteriza por tener una dieta no equilibrada, monosaturada y balanceada a la izquierda. Con 420 registros, representa un 34,65% de la muestra.
        - Le sigue de cerca, el perfil de seguidor que no sigue a ninguna cuenta de periódico y que por lo tanto, no tiene dieta mediática. Con 411 registros, representa un 33,91% de la muestra.
        - En tercera posición, se encuentra el perfil de dieta no equilibrada, saturada y con balanceo a la izquerda. Con 112 registros, representa un 9,24%
        - Si nos fijamos solo en el balanceo, quedaría de la siguiente forma:
        
            Balanceada: 121 registros, representan el 9,98% de la muestra.
            Balanceo a la izquierda: 573 registros, representan el 47,27% de la muestra.
            Balanceo a la derecha: 94 registros, representan el 7,76% de la muestra.
       
      Se observa una clara tendencia hacia la izquierda.
                
      Cuadro de mando 2
      
            Título: Comparación entre consumo de periódicos y parámetros de balanceo y saturación
            Gráfico 1: Saturación y consumo de periódicos
                Se muestra para cada uno de los distintos valores que puede tomar el parámetro saturación, el
                número de seguidores que siguen a cada cuenta de periódico. Este gráfico, nos permite visualizar la
                densidad de seguidores que tiene cada periódico para cada valor del parámetro saturación.
            Gráfico 2: Balanceo y consumo de periódicos
                Se muestra para cada uno de los distintos valores que puede tomar el parámetro balanceo, el
                número de seguidores que siguen a cada cuenta de periódico. Este gráfico, nos permite visualizar la
                distribución de los seguidores a lo largo de los distintos periódicos en función del balanceo que aparezca.
        
    Resultados
        - Fijándonos en 'Saturación y consumo de periódicos', se puede observar que tanto en dietas monostauradas, como dietas saturadas, los medios de izquierdas y centroizquierda, cuentan con más seguidores. Sin embargo en dietas polisaturadas, no hay ningún grupo de destaque.
        - Si pasamos a la visualización 'Balance y consumo de periódicos', se puede observar que entre los seguidores que balancean a la izquierda, sí que hay mayor tendencia a seguir periódicos de derechas, en menor grado que periódicos de izquierdas, pero hay tendencia. Sin embargo, entre los seguidores que balancean a la derecha no se observa ningún interés sobre los medios de izquierdas.
        - Entre los usuarios con dieta balanceada, los periódicos más populares son el País y el Mundo.
        

6. Guía de uso bajo entorno linux.
    1. Crear una cuenta de Twitter en https://twitter.com/
    2. Dar de alta aplicación para obtener credenciales en https://apps.twitter.com/
    3. Sustituir los tokens de acceso en los campos indicados con 'xxxxxxxxxxxxxxxxx' en los ficheros apiToMongoDb.py y dataProcess.py
    4. Instalar python: sudo apt-get install python
    5. Instalar pip: sudo python get-pip.py
    6. Instalar pymongo: sudo python -m pip install pymongo
    7. Instalar librería Twitter: sudo pip install python-twitter
    8. Instalar unicodecsv: sudo apt-get install python-unicodecsv
    9. Instalar librería tweepy: sudo pip install tweepy
    10. En el mismo directorio debe estar los siguientes archivos: apiToMongoDb.py, funciones.py, dataProcess.py
    11. En la línea 76 de apiToMongoDb.py indicar nombre de la cuenta de la que se quieren extraer los seguidores. Por defecto: AjuntamentVLC
    12. En el mismo directorio que apiToMongoDb.py ejecutar en consola: python apiToMongoDb.py 
    Con esto obtenemos los seguidores e información asociada.
    13(Opcional). En el mismo directorio que funciones.py ejecutar en consola: python funciones.py
    Este paso se realiza si no se dispone de tiempo para hacer un análisis de toda la población, ya que se creará una muestra.
    14. En el mismo directorio que dataProcess.py ejecutar en consola: python dataProcess.py
    Con esto obtenemos los valores de los parámetros de la dieta de cada seguidor de la muestra. Indicar el la línea 235 el el nombre del fichero CSV de la población o la muestra, por defecto está el nombre del fichero que se genera tras la muestra.
    15. Abrir el CSV generado por dataProcess.py con un software de hojas de cálculo(Calc, Excel, ...) y guardarlo como archivo con extensión .xls o .xlsx
    16. Seleccionar en Tableau el .xls generado y confeccionar las visualizaciones.
    17. La visualización de este estudio se encuentra en https://public.tableau.com/profile/david3308#!/vizhome/Anlisisparmetrosdietameditica/Historia1

7. Términos de uso.
El contenido de este repositorio está sujeto a la licencia GNU General Public License v3.0.
