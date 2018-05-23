# Solemne 1
## descripción 
Se pide implementar una solución en django que permita gestionar las nominas a un partido de baloncesto, para ello debe considerar las siguientes entidades:

- Equipo
- Jugadores
- Entrenador

La relación entre las entidades establece que un Equipo se compone por varios jugadores y cada jugador solo puede pertencer a un solo equipo, además el equipo posee un único entrenador y cada entrenador solo puede entrenar a un único equipo. 

Cada entidad debe considerar los siguientes campos:

* El Equipo debe tener los siguientes campos
    - Nombre del equipo
    - Descripción del equipo
    - Logo del equipo

* Un jugador  debe contener los siguientes campos
    - Nombre jugador
    - Apodo
    - Fecha de nacimiento
    - Edad
    - Rut
    - Email
    - Estatura
    - Peso
    - Fotografía
    - Posición de juego (opciones: Base, Escolta, Alero, Ala-pivot, Pivot)

* El Entrenado debe contener los siguientes campos:
    - Nombre entrenador
    - Edad
    - Email
    - Rut
    - Apodo

La aplicación deberá tener un administrador que será encargado de crear los equipos, jugadores y entrenador. además de asignar las credenciales al entrenador para que pueda hacer login.

Además, debe permitir que el entrenador se autentique y pueda crear una nomina para un partido. Cada nómina debe contener el nombre del partido, fecha y hora y los jugadores que participaran, además cada nomina no puede superar los 12 jugador y ser inferior a los 5 jugadores. 

Finalmente, al momento de generar la nomina, esta debe ser publica para que los jugadores puedan revisarla.

## Consideraciones
La aplicación debe considerar las siguientes características:
- CRUD para la entidades Jugador, Equipo y Entrenador (no aplica el uso del admin)
- En el listar jugadores, equipos debe considerar la paginación de resultados
- Solo el administrador podrá crear, editar y eliminar equipos, jugadores y entrenadores
- El entrenador solo podrá ver su equipo y las nominas creadas. Además de crear nuevas nominas.


## Condiciones de entrega
* El proyecto debe estar versionado con GIT y gestionado a través de GITHUB
* Debe enviar el link del proyecto al email miguel [at] ewok [dot] cl 
* Asunto: DW2018-SOLEMNE-1
* Fecha de entrega: 01 Junio 2018

## Consideraciones
* Se evaluará el uso de GIT y GITHUB
* Se evaluará el uso de models en django
* Se evaluará el uso de views, urls y templates
* Manejo de login

## Hints
* Utilice los HTML entregados en el proyecto https://github.com/mcantillana/dw2018-views-html
* Para el login puede utilizar bootstrap con su ejemplo login http://getbootstrap.com/docs/4.1/examples/floating-labels/ 
