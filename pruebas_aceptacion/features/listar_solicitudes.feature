Característica: Listar solicitudes
    Como usuario del sistema LEMA
    Quiero ver la lista de solicitudes
    Para mantener ver todas las solicitudes registradas.
    
    Escenario: Mostrado de todas las solicitudes
        Dado que accedo a la página de login
        Y capturo en el usuario "jozuelenuv" y en la contraseña "jozue123"
        Y inicio sesión
        Y selecciono el botón "Solicitudes"
        Entonces puedo ver una lista con todas las solicitudes capturadas en el sistema.

    Escenario: Mostrado de solicitudes propias del encuestador
        Dado que accedo a la página de login
        Y capturo en el usuario "jozuelenuv" y en la contraseña "jozue123"
        Y inicio sesión
        Y selecciono el botón "Solicitudes"
        Entonces puedo ver una lista con todas las solicitudes que he capturado.