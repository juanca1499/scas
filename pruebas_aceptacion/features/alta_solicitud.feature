Característica: Como agente me gustaría registrar
                una solicitud de apoyo para valorar 
                el caso del solicitante

    Escenario: Datos de solicitud correctos
        Dado que accedo a la página de login
        Y capturo en el usuario "jozuelenuv" y en la contraseña "jozue123"
        Y inicio sesión
        Y selecciono el botón "Solicitudes"
        Y selecciono agregar solicitud
        Y capturo "17-Nov-2021" en la fecha de la solicitud
        Y capturo "Juan Carlos" en el nombre
        Y capturo "García" en el primer apellido
        Y capturo "Murillo" en el segundo apellido
        Y capturo "Rafael Acuña" en la calle
        Y capturo "9" en el número
        Y capturo "99343" en el código postal
        Y capturo "0629" en la sección
        Y capturo "4949428829" en el teléfono
        Y capturo "GAMJ991014HZSRRN01" en la CURP
        Y elijo "Zacatecas" en el estado
        Y elijo "Jerez" en el municipio
        Y elijo "Ciénega" en la localidad
        Y elijo "En Trámite" en el estatus
        Y capturo "14-Oct-1999" en la fecha de nacimiento
        Y capturo "garciamjuancarlos14@gmail.com" en el correo
        Y capturo "El joven Juan Carlos es un estudiante universitario" en el resumen de la solicitud
        Cuando presiono el botón "Registrar" 
        Entonces el sistema me muestra el mensaje "Solicitud guardada exitosamente"

    Escenario: Datos de solicitud incorrectos
        Dado que accedo a la página de login
        Y capturo en el usuario "jozuelenuv" y en la contraseña "jozue123"
        Y inicio sesión
        Y selecciono el botón "Solicitudes"
        Y selecciono agregar solicitud
        Y capturo "17-Nov-2021" en la fecha de la solicitud
        Y capturo "Juan Carlos" en el nombre
        Y capturo "García" en el primer apellido
        Y capturo "Murillo" en el segundo apellido
        Y capturo "Rafael Acuña" en la calle
        Y capturo "9" en el número
        Y capturo "9ocho6uno3" en el código postal
        Y capturo "0629" en la sección
        Y capturo "4949428829" en el teléfono
        Y capturo "GAMJ991014HZSRRN01" en la CURP
        Y elijo "Zacatecas" en el estado
        Y elijo "Jerez" en el municipio
        Y elijo "Ciénega" en la localidad
        Y elijo "En Trámite" en el estatus
        Y capturo "14-Oct-1999" en la fecha de nacimiento
        Y capturo "garciamjuancarlos14@gmail.com" en el correo
        Y capturo "El joven Juan Carlos es un estudiante universitario" en el resumen de la solicitud
        Cuando presiono el botón "Registrar"
        Entonces el sistema me muestra el mensaje "Hay datos inválidos en el formulario"