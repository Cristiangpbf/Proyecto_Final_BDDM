# Proyecto_Final_BDDM
FECHA: 21 de septiembre 2020

Se realiza el proceso de cosecha de datos, su transformación, mapeo, creación de índices, entre otros procesos para el análisis de datos de fuentes de Internet como twitter, tiktok y además archivos estáticos de INEC.

Se tiene como objetivo obtener y analizar datos de diversas fuentes con el uso de varias herramientas usadas en clase, diseñar una arquitectura de Data Lake en la cual tenga el insumo de datos, recopilar información con geolocalización o con filtro de palabras, realizar varias visualizaciones de datos para el análisis de los mismos.
Y así poner en practica todos los temas y herramientas aprendidas en clase durante el semestre en la materia de bases de datos multidimensionales.

EQUIPO DE TRABAJO 

El equipo de trabajo está integrado por: Xavier Calle, Samanta Gómez, Cristian Guamba y David Pisuña.

Entre las actividades realizadas se organizó el equipo de la siguiente manera:

Xavier: Recolección de datos para el caso de estudio:  juegos en línea. 
Fuente de datos: Twitter.
Motor de base de datos: MySQL.

Samanta: Recolección de datos para el caso de estudio: Condiciones de vida-vivienda en el Ecuador 
Fuente de datos: INEC.
Motor de base de datos: PostgreSQL.

Cristian: Recolección de datos para el caso de estudio:  Pulso político en 20 ciudades principales de Ecuador, listas y candidatos, presidenciales y diputados. Pulso político por provincias en Ecuador, listas y candidatos, presidenciales y diputados.
Fuente de datos: Twitter.
Motor de base de datos: CouchDB.

David: Recolección de datos para el caso de estudio:  Tendencia actual – Red Social
Fuente de datos: Tik Tok.
Motor de base de datos: MongoDB.

Recursos y herramientas utilizadas durante el desarrollo del proyecto

MYSQL

MySQL es un sistema de gestión de bases de datos relacionales de código abierto (RDBMS, por sus siglas en inglés) con un modelo cliente-servidor. RDBMS es un software o servicio utilizado para crear y administrar bases de datos basadas en un modelo relacional. 

POSTGRESQL

PostgreSQL es una de las opciones más interesantes en bases de datos relacionales open-source. Michael Stonebraker inició el proyecto bajo el nombre Post Ingres a mediados de los 80’s con la idea de solucionar problemas existentes en las bases de datos en esa época. MySQL fue por mucho tiempo el motor más popular; pero hoy es propiedad de Oracle y esto limita su evolución, una característica interesante de PostgreSQL es el control de concurrencias multiversión; o MVCC por sus siglas en inglés. Este método agrega una imagen del estado de la base de datos a cada transacción. Esto nos permite hacer transacciones eventualmente consistentes, ofreciéndonos grandes ventajas en el rendimiento. 

COUCHDB

Es una base de datos NoSQL capaz de replicarse en una amplia gama de entornos cliente y servidor. Por sus respectivas características, el Cloud Computing es el ambiente de funcionamiento más natural de CouchDB, otra de las aplicaciones Open Source que podemos instalar y desplegar sobre los Servidores Cloud de Arsys en sólo unos minutos. 

MONGODB

Es una base de datos orientada a documentos. Esto quiere decir que, en lugar de guardar los datos en registros, guarda los datos en documentos. Estos documentos son almacenados en BSON, que es una representación binaria de JSON.

ELASTICSEARC

Se trata de un motor de búsqueda y análisis. Es distribuible y fácilmente escalable, enfocado sobre todo al mundo empresarial y científico. Es accesible a través de una extensa y elaborada API. Con esta herramienta podemos impulsar búsquedas extremadamente rápidas que respalden nuestras aplicaciones de descubrimientos de datos. 

Sus características:
	Es orientado a documentos: Utiliza JSON
	No utiliza esquemas, aunque si son necesarios se pueden llegar a definir
	Distribuido: Realiza escalado de manera dinámica, implementa alta disponibilidad (HA)
	Utiliza una potente API: expone prácticamente todas sus funcionalidades utiliza una API REST
	Permite búsquedas tanto estructuras como no estructuradas 
  
KIBANA

Kibana es una herramienta open-source perteneciente a Elastic, que nos permite visualizar y explorar datos que se encuentran indexados en ElasticSearch, es decir, un plugin de ElasticSearch. Kibana también es conocido por el stack ELK.
  
CEREBRO

Cerebro es un entorno de trabajo colaborativo adecuado para proyectos de complejidad ilimitada. Esta es una herramienta para la planificación, distribución de tareas y seguimiento de la ejecución. Ofrece características únicas en términos de almacenamiento e intercambio de datos, así como anotaciones visuales para cualquier material de trabajo. 

LOAGSTASH

Es una herramienta Open Source que nos permite centralizar la recogida de información, normalizarla y redistribuirla. 
Aunque es una herramienta que puede funcionar de forma independiente, como parte del Stack vemos que Logstash tiene total integración con éste. Su integración con Beats, Elasticsearch y Kibana es nativa, ofreciendo así gran valor para la transformación avanzada de nuestra información. 

TWITTER

Esta plataforma social, es un servicio de comunicación bidireccional con el que puedes compartir información de diverso tipo de una forma rápida, sencilla y gratuita, se trata de una de las redes de microblogging más populares que existen en la actualidad y su éxito reside en el envío de mensajes cortos llamados “tweets”. 

INEC

Instituto Nacional de Estadística y Censos fue creado mediante la Ley No. 7839 del Sistema Estadístico Nacional (SEN), como Institución Autónoma de derecho público, con personería jurídica y patrimonio propios, gozando de autonomía funcional y administrativa consagrada en el artículo No 188 de la Constitución Política. 

TIK TOK

Hablamos de una red social asiática basada en compartir vídeos musicales, y que está consiguiendo unos increíbles resultados en los últimos meses. De hecho, este pasado mes de octubre ha conseguido superar a Facebook, Instagram, YouTube y Snapchat en número de descargas confirmándose como una de las sorpresas del año. 

PROCESO DE EXTRACCIÓN DE DATOS

Caso de estudio: Pulso político en Ecuador
La extracción de datos se realizó desde Twitter mediante dos scripts de Python.
El primero utilizó como criterio de búsqueda los nombres de los precandidatos a presidencia y vicepresidencia, y sus respectivos partidos políticos. Además, se añadieron los hashtags y nombres de usuario en Twitter.
El segundo script incluyó las coordenadas del territorio ecuatoriano extraídas del sitio web; https://boundingbox.klokantech.com/
Los datos fueron almacenados en CouchDB, y mediante Logstash, se enviaron en tiempo real a Elastic cloud.
Los datos enviados desde CouchDB hasta Elastic cloud, se unifican en mismo índice de nombre map_twitter.

Caso de estudio: Juegos en linea
La extracción de datos se dio desde la fuente: Twitter
La extracción de datos se realizó desde Twitter utilizando un script de Python y un archivo de configuración.
Primeramente, se realizó la recolección de datos con el script de Python.

Caso de estudio: Condiciones de vida-vivienda en el Ecuador
La extracción de datos se dio desde la fuente: INEC
Obteniendo un archivo .csv con la información.

Caso de estudio: Tendencia actual – Red Social
La extracción de datos se dio desde la fuente: Tik Tok
Obteniendo un archivo .csv con la información.

ANALISIS DE DATOS Y DESARROLLO

Caso de estudio: Pulso político en Ecuador
Para el análisis de datos se usó la herramienta Elasticsearch en la nube.
Para un correcto formato de los datos, se realizó el mapeo de los atributos de tipo fecha y geolocalización en las propiedades del índice para los datos de Twitter.
De la totalidad de datos que se consiguieron solo el 44,21% tuvo la geolocalización activa.
Para filtrar los datos se crearon varias consultas para clasificar los datos por localidades y por partidos políticos.
Las subconsultas se realizaron en la herramienta Kibana de Elastic clud.

Caso de estudio: Juegos en línea
Los datos recolectados fueron: identificador de twitter, nombre de usuario, texto del tweet y localización como se indica en la figura 4 donde definimos que campos se van a guardar en la base de datos y el tipo de datos.
Se utilizó la herramienta cerebro para visualizar los datos recolectados en elastic search.
 
Caso de estudio: Condiciones de vida-vivienda en el Ecuador
El instituto nacional de estadísticas y censos realizó una encuesta nacional de condiciones de vida en todas las provincias del país dando un aproximado de 1040000 millones de datos.
Se realiza la población de la base de datos, ésta puede realizarse de dos maneras ya sea por el método de importación de un archivo csv 
Figura11: Importación de archivo .csv Ó a su vez por medio de fórmula se puede realizar las líneas de insertar en el documento .csv para luego copiar en un script y al correr ingresan los datos, después de haber creado la base de datos se procede a crear una tabla la misma que va a hacer llenada de inmediato.
Al finalizar la población de la base de datos se puede verificar por medio de una consulta como se muestra en la siguiente figura.
 
VISUALIZACION DE INFORMACIÓN

Caso de estudio: Pulso político en Ecuador
Para la visualización de información y la creación de consultas se usó kibana.
Mediante la opción Discover, se analizarón resultados previos basados en grupos pequeños de datos. Estas consultas trabajan con datos limitados (500) para mostrar resultados de tendencias.

Estos resultados se usaron para definir los atributos críticos de los tweets recabados, para poder generar las visualizaciones.
 
Caso de estudio: Condiciones de vida-vivienda en el Ecuador
Se requiere configurar un archivo para ejecutar con logstash, previamente ya iniciado cerebro, elasticsearch y kibana para ingresar el archivo json y poder ver algunas tablas como visualizaciones, se inicia el proceso de carga del archivo .json y podemos observar varias vistas con diferente orden de tatos para interpretar de una forma mas práctica y facil la información.

Caso de estudio: Tendencia actual Red Social Tik-Tok, es una de las plataformas de redes sociales que más rápido ha crecido en el mundo y que presenta una versión alternativa de compartir e interactuar online, ya que permite a los usuarios crear vídeos cortos con música, filtros y otras características.

Desde el paso de obtención de datos, se estuvieron descargando los archivos desde Python y luego enviando las consultas desde CouchDB hasta Elastc cloud. Razón por la que los datos ya se encontraron en el punto de unificación de los resultados obtenidos, desde un principio

RESULTADOS OBTENIDOS UNIFICADOS

Desde el paso de obtención de datos, se estuvieron enviando las consultas desde los diferentes motores de bases de datos MongoDB, CouchDB, PostgreSQL y MySQL hasta Elastc cloud. Razón por la que los datos ya se encontraron en el punto de unificación de los resultados obtenidos, desde un principio.

Elastic Cloud:
hosts: "https://9ba19c6e50304a85956a1c80d0323876.eastus2.azure.elastic-cloud.com:9243"
user: "elastic"
password: "59w55DqTdnJW8D1Sli7LRLrq"

Se creó de 3 nodos, 16 índices para la carga de datos en conjunto de los distintos casos de estudio, recopilando mas de 4 millones de datos.
Se debe tomar en cuentta que el mapeo de los datos es primordial para el análisis de resultados, puesto que si no se cuentan con datos mapeados no se puede realizar un análisis correcto de los datos recopiados.

DESAFÍOS ENCONTRADOS Y RESULETOS

	La carga de información estática puede registrar un significativo aumento de tiempo empleado que los datos en tiempo real, al subir los archivos .json a la nube        llevo un tiempo prolongado por la cantidad de datos.
	Los datos no mapeados generan conflictos en el análisis de las gráficas pero fueron resueltos y coordinados grupalmente para continuar con el proceso sin dificultad.

