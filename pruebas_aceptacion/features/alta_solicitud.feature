Característica: Como agente me gustaría registrar
                una solicitud de apoyo para valorar 
                el caso del solicitante

    Escenario: Datos de solicitud correctos
    Dado que accedo a la página de login
    Y capturo en el usuario "juca" y en la contraseña "juca123"
    Y inicio sesión
    Y me dirijo al dashboard 
    Y selecciono agregar solicitud
    Y capturo "17-11-2021" en la fecha de la solicitud
    Y capturo "Juan Carlos" en el nombre
    Y capturo "García" en el primer apellido
    Y capturo "Murillo" el segundo apellido
    Y capturo "Rafael acuña" en la calle
    Y capturo "9" en el número
    Y capturo "99343" en el código postal
    Y capturo "0629" en la sección
    Y capturo "4949428829" en el teléfono
    Y capturo "GAMJ991014HZSRRN01" en la CURP
    Y capturo "Jerez, Zacatecas" en el lugar de nacimiento
    Y capturo "14-10-1999" en la fecha de nacimiento
    Y elijo la opción "Soltero(a)" en estado civil
    Y elijo la opción "Secundaria" en el último grado de estudios
    Y elijo la opción "Estudiante" en la ocupación
    Y capturo "garciamjuancarlos14@gmail.com" en el correo
    Y capturo "El joven Juan Carlos es un estudiante universitario" en el resumen de la solicitud
    Cuando presiono el botón "Registrar"
    Entonces el sistema me reedirecciona a la lista de solicitudes

    Escenario: Datos de solicitud incorrectos
    Dado que accedo a la página de login
    Y capturo en el usuario "juca" y en la contraseña "juca123"
    Y inicio sesión
    Y me dirijo al dashboard 
    Y selecciono agregar solicitud
    Y capturo "17-11-2021" en la fecha de la solicitud
    Y capturo "Juan Carlos" en el nombre
    Y capturo "García" en el primer apellido
    Y capturo "Murillo" el segundo apellido
    Y capturo "Rafael acuña" en la calle
    Y capturo "9" en el número
    Y capturo "9ocho6uno3" en el código postal
    Y capturo "0629" en la sección
    Y capturo "4949428829" en el teléfono
    Y capturo "GAMJ991014HZSRRN01" en la CURP
    Y capturo "Jerez, Zacatecas" en el lugar de nacimiento
    Y capturo "14-10-1999" en la fecha de nacimiento
    Y elijo la opción "Soltero(a)" en estado civil
    Y elijo la opción "Secundaria" en el último grado de estudios
    Y elijo la opción "Estudiante" en la ocupación
    Y capturo "garciamjuancarlos14@gmail.com" en el correo
    Y capturo "El joven Juan Carlos es un estudiante universitario" en el resumen de la solicitud
    Cuando presiono el botón "Registrar"
    Entonces el sistema me muestra el mensaje "Hay datos inválidos en el formulario."