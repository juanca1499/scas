Característica: Como administrador me gustaría consultar 
                la información de un estudio socioeconómico 
                para visualizar todos los datos que se capturaron.
                
                Como agente me gustaría consultar la información de 
                un estudio socioeconómico para visualizar todos los 
                datos que se capturaron.

    Escenario: Consulta de estudio correcto.
        Dado que accedo al login
        Y capturo usuario "juca" y contraseña "juca123"
        Y presiono ingresar
        Y me dirijo a solicitudes
        Y selecciono visualizar solicitud
        Y selecciono ver estudio socioeconomico
        Entonces el sistema deberá mostrar el estudio socioeconomico.