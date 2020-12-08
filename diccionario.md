##################################################################

Este es un diccionario en el que ir metiendo todas las palabras claves que vayamos viendo en el curs.

La idea es actualizarlo periódicamente, e ir mejorando las definiciones.

##################################################################

### programación (1.7)
"preparar una secuencia de instrucciones para que un ordenador haga una tarea que queremos"
***
### lenguaje de programación (1.7)
"Es un lenguaje que permite a una persona dar instrucciones a un ordenador para que realice una serie de tareas"
***
### editor de codigo (1.7) 
"Un programa con el cual se puede escribir texto a la pantalla del ordenador"
***
### sublime text (1.7)
"un editor de texto"
***
### visual studio code (1.7)
"un editor de texto"
***
### algoritmo de cifrado simético
"Se utiliza para enviar mensajes encriptados, en los que sólo hay una clave que comparten el emisor y el receptor, tanto para cifrar como para descifrar el mensaje. Es menos seguro que el método asimetrico. La seguridad se reduce a que esa clave no caiga en manos equivocadas. Otro inconveniente es que por cada canal de comunicación habrá que tener una clave, mientras que en el sistema asimetrico, no. La ventaja que tiene es la velocidad."
***
### algoritmo de cifrado asimético
Cada usuario tiene una clave privada, que no comparte, y una pública que será accesible a todos los usuarios del canal de comunicación. Además de cifrar mensajes, cumple la función de verificar la identidad del emisor.
***
### funciones en programación
Las funciones son como pequeños de programas, ya que les pasas unos valores de entrada (*parámetros*), efectuan una serie de operaciones (*código de la función*), y devuelven otros valores (*valores de retorno*), los cuales entrega mediante la sentencia *return*.
***
### Ley de Moore (1.2)
Describe la tendencia empírica a que cada 2 años, se dobla el número de transistores en los circuitos integrados. Esto está directamente relacionado con el aumento de la velocidad de procesamiento, y el precio de los productos electrónicos.
***
### Transistores (1.2)
Son componentes electrónicos semiconductores que responden de una determinada forma al ser expuestos a una señal, y que combinados componen forman las puertas lógicas que controlan las operaciones dentro de los procesadores.
***
### Puertas Lógicas (1.2)
Son "puertas" que dejan pasar la corriente que les llega o no, dependiendo de los como estén configuradas. Se forman a partir de transistores, y se puede ir añadiendo complejidad hasta formar toda la lógica necesaria para que el procesador realice sus operaciones.
***
### Ada Lovelace (2.2)
Es considerada la creadora del primer programa de ordenador, y creadora del primer algoritmo, y visualizó todo el potencial de las maquinas computadoras.
***
### Bucles (2.2)
Son pedazos de código que se ejecutan repetidamente. Normalmente tienen una condición que si se cumple, finaliza el bucle. Si no, se trataría de un bucle infinito. Hay de distintos tipos (for, while), que varían en su sintaxis.
***
### Arquitectura cliente-servidor (2.5)
Se trata de un modelo de diseño de software en el que se reparten las tareas entre dos partes, la que sirve los contenidos, y la que consume esos contenidos. Este es el diseño que tiene internet.
***
### FTP (2.5)
"File Transfer Protocol". Protocolo que utilizan los ordenadores para transferir archivos. Los protocolos son una serie de normas que deben cumplir las partes para entenderse, tal y como las normas de cualquier idiomas.
***
### Protocolo TCP/IP (2.5)
En realidad son 2 protocolos, que casi siempre van unidos, y que juntos forman la columna vertebral de las comunicaciones por internet. Ocupan las capas 3 y 4 del Modelo OSI, que describe la transferencia de datos en redes
***
### DNS (2.5)
"Domain Name System". Es un sistema para asociar la dirección IP de los servidores web (poco legible para las personas) a los dominios (www.google.com), facilitando su localización en la red. Los servidores DNS se encargan de recibir las peticiones de los clientes y resolverlo buscando la IP asociada en sus tablas.
***
### IP (2.5)
Suele asociarse a la dirección IP que identifica a los dispositivos conectados a una red. Pero las siglas IP se refieren al "Internet Protocol"
***
### Servidor web (2.5)
Dentro de la arquitectura cliente-servidor que conforma internet, el servidor web es el software que cumple la función de procesar las peticiones del cliente y servir contenidos en función de éstas. Implementa el protocolo HTTP(s), que es el que se usa en cada transacción en la Web. 
***
### ETL (3.1)
Son las siglas "Extract, Transform, Load", que componen los 3 pasos que se deben dar en el preprocesado de datos. Los datos se extraen en crudo, se transforman para que tengan la forma adecuada usarlos en nuestro análisis, y se cargan al "data warehouse" o almacén de datos, siguiendo las pautas marcadas.
***
### Bases de datos (3.1)
Es dónde se almacenan los datos. Se clasifican en dos grandes tipos: relacionales y no relacionales.
***
### Data-preprocessing (3.1)
Normalmente los datos vienen no vienen "limpios", sino que antes de inyectarlos en nuestros algoritmos, deben ser preparados y limpiados para que su manejo sea más fácil.
***
### API  (3.4)
Se trata de una interfaz para comunicarse las aplicaciones entre sí, y las reglas que conforman esa interfaz. La parte cliente hace uso de las funcionalidades que le ofrece la API para no tener que "rehacer la rueda" 
***
### JSON (3.4)
*Javascript Object Notation*. Es un formato que ha ganado mucho terreno en el intercambio de DATOS a través de APIs. 
***
### XML  (3.4)
*eXtensible Markup Language* Se trata de un metalenguaje, es decir, que se puede utilizar para definir otro lenguaje, como es el caso de HTML. Se puede utilizar para intercambiar datos en APIs, aunque ese uso cada vez es más relegado por el uso de JSON.
***
### Protocólogo de Comunicación  (3.4)
Se trata de un conjunto de reglas que las partes interactuando en una comunicación tienen que cumplir. Existen protocolos que se implementan a nivel de software y de hardware.
***
### Bases de datos (3.5)
Son conjuntos de información que se almacenan y se consultan de una forma sistematizada. Para ello se utilizan herramientas de software llamadas gestores de bases de datos, que son las que permiten esa estructuración, almacenado, modificación y consulta.
***
### SQL (3.5)
Se trata de una de las 2 grandes ramas de las bases de datos. Sus siglas significan hacen referencia al lenguaje que se utiliza para hacer las consultas(también los modificaciones)
*Structured Query Language*. Son bases de datos relacionales, es decir que hay tablas que almacenan los datos y se relacionan entre ellas. Tiene una estructura definida desde el inicio, por lo que su diseño es clave desde el principio. 
***
### NoSQL (3.5)
Bases de datos no relacionales. No tienen una estructura definida, por lo que son más flexibles ante el cambio. Han proliferado en los ultimos años, ya que el entorno tan cambiante de internet, genera constantemente nuevos datos y es dificil tener una estructura definida de la base datos al empezar. Pueden ser más rápidas en proyectos a muy gran escala, pero la normalización de datos se dificulta.
***
### Dirección IP (3.7)
Es el número que identifica a a cualquier interfaz que se conecta y utiliza el protocolo de internet (IP, por sus siglas en inglés). La versión antigua, IP-v4 es un número de 32 bits, del tipo *127.12.14.19*. Actualmente exista el IP-v6, que es un número de 128 bits. Hay IPs privadas, que sólo son visibles dentro de una red, e IPs públicas, que son visibles y accesibles desde cualquier dispositivo conectado a internet.
***
### Internet (3.7)
Internet es una red de ordenadores conectados mundialmente, en el cual se comunican e intercambian información entre ellos siguiendo unas pautas o protocolos que todos entienden.
***
### WAN (3.7)
*Wide Area Network*. Se trata de una red que une ordenadores en un territorio grande. Internet es un ejemplo de una WAN.
***
### LAN (3.7)
*Local Area Network*. Los ordenadores en una oficina u otro espacio pequeño suelen estar conectados a traves de una LAN. 
***
### Máscara de Subred (3.7)
Se trata de una secuencia de bits, de la misma longitud que la dirección IP, la cual sirve para que un dispositivo sepa cuántos bits de la dirección IP que le ha sido asignada identifican a la dirección IP de la subred a la cual pertenece, y cuántos bits indican la dirección a ellos mismos (*el host*).
### Router (3.7)
Es un dispositivo hardware que sirve para que varios dispositivos se conecten entre si, y compartan una misma conexióin a internet. Opera en el nivel 3 del modelo OSI. El router se asegura de que el tráfico proviniente de internet llega al dispositivo que ha solicitado la informacion.

### Switch (3.7)
Es un dispositivo de hardware parecido al router, pero que sólo conecta dispositivos entre sí, y redirige trafico. No se conecta a internet como elk router.

### TCP-IP (3.7)
Aunque se hable de ellos conjuntamente, se trata de dos protocolos que operan en niveles diferentes del modelo OSI, pero que juntos forman el "stack" de protocolos más utilizados y que conforman la esencia de la comunicacion por internet. IP opera en la capa 3, y tiene que ver con la comunicación entre IPs, y TCP opera en la capa 4 y tiene que ver con la comunicacion entre puertos concretos.

### IP publica
Es la dirección que se utiliza para conectarse a internet

### IP privada
Su función es la de dirigir el tráfico dentro de una red local privada. No se puede enviar tráfico a ellas desde internet.