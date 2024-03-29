Característica: Como administrador me gustaría poder registrar
                una cuenta para que pueda iniciar sesión.

    Escenario: Datos de registro correctos
    Dado que me encuentro logueado en el sistema
    Y selecciono el botón "Usuarios"
    Y presiono el botón "Agregar"
    Y capturo el nombre "Josue" 
    Y capturo el primer apellido "Gonzalez" 
    Y capturo el segundo apellido "Pinedo"
    Y capturo la calle "Real de angeles"
    Y capturo en el numero "43"
    Y capturo la colonia "Camino Real"
    Y capturo el código postal "98613"
    Y elijo el estado "Zacatecas"
    Y elijo el municipio "Guadalupe"
    Y elijo la localidad "Guadalupe"
    Y capturo el correo "jouselenuv@gmail.com"
    Y capturo el teléfono "4921736547"
    Y subo fotografía de mi INE
    Y capturo el usuario "jozuelenuv"
    Y capturar la contraseña "jozue123"
    Cuando presiono el botón "Agregar"
    Entonces puedo ver al usuario "jozuelenuv" en la lista de usuarios.  

    Escenario: Datos de registro incorrectos
    Dado que me encuentro logueado en el sistema
    Y selecciono el botón "Usuarios"
    Y presiono el botón "Agregar"
    Y capturo el nombre "Josue" 
    Y capturo el primer apellido "González"  
    Y capturo el segundo apellido "Pinedo"
    Y capturo la calle "Real de angeles"
    Y capturo en el numero "43"
    Y capturo la colonia "Camino Real"
    Y capturo el código postal "9861a"
    Y elijo el estado "Zacatecas"
    Y elijo el municipio "Guadalupe"
    Y elijo la localidad "Guadalupe"
    Y capturo el correo "jouselenuv@gmail.com"
    Y capturo el teléfono "4921736547"
    Y subo fotografía de mi INE
    Y capturo el usuario "jozuelenuv2"
    Y capturar la contraseña "jozue123"
    Cuando presiono el botón "Guardar"
    Entonces puedo ver el mensaje "Hay datos inválidos en el formulario".