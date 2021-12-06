Característica: Consultar solicitud
    Como usuario del sistema LEMA
    Quiero consultar los datos de una solicitud
    Para mantener ver la información detallada de la solicitud.
    
    Escenario: Mostrado de detalles correctamente de una solicitud
        Dado que accedo a la página de login
        Y capturo en el usuario "jozuelenuv" y en la contraseña "jozue123"
        Y inicio sesión
        Y selecciono el botón "Solicitudes"
        Y selecciono la solicitud que quiero consultar
        Cuando presiono el botón Ver detalles
        Entonces el sistema deberá mostrar los datos de la solicitud seleccionada.