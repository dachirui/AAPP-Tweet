# AAPP-Tweet
Proyecto sobre los parámetros de la dieta mediática de los seguidores de Twitter del Ayuntamiento de Valencia

1. Título: Análisis de los parámetros de la dieta mediática de los seguidores de Twitter del Ayuntamiento de Valencia
  
2. Introducción. Se indica el objetivo del proyecto, el problema a resolver y el contexto del mismo.

El principal objetivo del proyecto, es el diseño e implementación de una herramienta, que mediante el uso de herramientas externas, permita realizar los procesos de obtención, limpieza y presentación de datos sobre la información de seguidores de una cuenta de Twitter de cualquier administración pública.

El análisis de estos seguidores, aportará una información valiosa a las administraciones para poder encauzar la toma de decisiones en políticas de comunicación y otras políticas. Se podrá llegar y satisfacer a una parte de su público, que son los ciudadanos que interactúan vía Twitter con las cuentas de las administraciones.

Este proyecto se desarrolla en el contexto actual en el que el uso de las núevas tecnologías y el acceso a las redes sociales está al alance de cualquiera. Este hecho, sumado a la importancia de la transparencia de las insitituciones y la participación ciudadana da pie a proyectos como el presente, proyectos que buscan mostrar información sobre la ciudadania que es gobernada para poder acertar a la hora de la toma de decisiones.

3. Descripción de la solución planteada.

Se propone un análisis de la dieta mediática de cada seguidor que se basará en las cuentas de periódicos seguidos

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
            - No:    
                - Desequilibro a derechas.    
                - Desequilibrio a izquierdas.
   
   Equilibrio: Consume al menos 1 medio de cada grupo.
        Respuestas:    Sí, No                    
   
   Saturación: Número de medios seguidos     
        Respuestas:    
            - monosaturada: <=5
            - saturada: >=6 y <=9 
            - polisaturada: >=10


Para obtener los seguidores se plantea desarrollar un módulo que descargue los seguidores mediante API de una cuenta de Twitter y los almacene en una base de datos. Fichero: apiToMongoDb.py

Para obtener los resultados de los parámtros del análisis de la dieta mediática, se plantea desarrollar un módulo que:
  1. Accede a los usuarios previamente almacenados
  2. Via TwitterAPI, accederá a cada uno de los ususarios para recuperar las cuentas a las que sigue y hacer conteo de periódicos a los que siguen.

4. Metodología.
aqui texto

5. Resultados.
aqui texto

6. Guía de uso.
aqui texto

7. Términos de uso.
El contenido de este repositorio está sujeto a la licencia GNU General Public License v3.0.
