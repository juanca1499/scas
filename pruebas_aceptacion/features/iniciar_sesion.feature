Característica: Como administrador me gustaría iniciar 
                sesión en el sistema para hacer consultas 
                o administración de información.
                Como encuestador me gustaría iniciar sesión
                en el sistema para hacer consultas o administración
                de información.

    Escenario: Credenciales válidas
    Dado que accedo al sistema 
    Y capturo el usuario "juca" y la contraseña "juca123"
    Cuando presiono el botón de inicio de sesión 
    Entonces el sistema me dirige a la página donde se muestran las solicitudes de apoyos que se han realizado. 

    Escenario: Credenciales incorrectas
    Dado que accedo al sistema
    Y capturo el usuario "juca" y la contraseña "123"
    Cuando presiono el botón de inicio de sesión
    Entonces el sistema me muestra el mensaje "El usuario o la contraseña no son correctos"