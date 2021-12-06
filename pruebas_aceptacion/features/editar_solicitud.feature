Característica: Editar solicitud
    Como usuario del sistema LEMA
    Quiero editar los datos de una solicitud
    Para mantener actualizada la información de las solicitudes.
    
    Escenario: Datos de edición correctos
        Dado que accedo a la página de login
        Y capturo en el usuario "jozuelenuv" y en la contraseña "jozue123"
        Y inicio sesión
        Y selecciono el botón "Solicitudes"
        Y selecciono la solicitud a editar
        Y corrijo el valor del campo "telefono": "4949428829"
        Cuando presiono el botón "Guardar"
        Entonces el sistema me muestra el mensaje "Solicitud actualizada"

    Escenario: Datos de edición incorrectos
        Dado que accedo a la página de login
        Y capturo en el usuario "jozuelenuv" y en la contraseña "jozue123"
        Y inicio sesión
        Y selecciono el botón "Solicitudes"
        Y selecciono la solicitud a editar
        Y corrijo el valor del campo "telefono": "494"
        Cuando presiono el botón "Guardar"
        Entonces el sistema me muestra el mensaje "Hay datos inválidos en el formulario"