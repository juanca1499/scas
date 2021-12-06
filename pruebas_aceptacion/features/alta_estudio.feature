Característica: Como administrador me gustaría agregar 
                un estudio socioeconómico a una solicitud para valorar 
                si se dará el apoyo al solicitante.

    Escenario: Datos de estudio socioeconómico correctos.
    Dado que me encuentro logueado en el sistema
    Y accedo a la url "http://192.168.33.10:8000/estudio-socieconomico/nuevo"
    # Y selecciono el botón "Solicitudes"
    # Y selecciono una solicitud
    # Y selecciono agregar estudio socioeconómico
    Y capturo la fecha de hoy
    Y subo un archivo como comprobante de domicilio
    Y subo un archivo como la credencial de elector
    Y elijo en ocupación "Estudiante"
    Y elijo en escolaridad "Preparatoria"
    Y elijo en estado civil "Soltero (a)"
    Y elijo en discapacidad "Ninguna"
    Y capturo la calle "Real de angeles"
    Y capturo en el numero exterior "43"
    Y capturo la colonia "Camino Real"
    Y capturo el código postal "98613"
    Y capturo en es cabeza de familia "si"
    Y capturo en estado civil "soltero"
    Y capturo en sufre de discapacidad "ninguna"
    Y capturo en su casa es "propia, pagada y escriturada"
    Y capturo en ¿cuenta con los siguientes servicios de equipamiento? "Energía eléctrica"
    Y capturo en ¿cuenta con los siguientes servicios de equipamiento? "Drenaje"
    Y capturo en ¿cuenta con los siguientes servicios de equipamiento? "Agua potable"
    Y capturo en ¿cuenta con los siguientes servicios de equipamiento? "instalación gas"
    Y capturo en ¿cuenta con los siguientes servicios de equipamiento? "Tel celular"
    Y capturo en ¿cuenta con los siguientes servicios de equipamiento? "Horno de micro"
    Y capturo en ¿cuenta con los siguientes servicios de equipamiento? "computadora"
    Y capturo en ¿cuenta con los siguientes servicios de equipamiento? "laptop"
    Y capturo en características de la casa "2 plantas"
    Y capturo en características de la casa  "sala/comedor"
    Y capturo en características de la casa "cocina"
    Y capturo en características de la casa "3 recámaras"
    Y capturo en características de la casa "1 baño"
    Y capturo en características de la casa "patio"
    Y capturo en características de la casa "cochera"
    Y capturo en el piso es "cemento"
    Y capturo en el techo es "ladrillo"
    Y capturo en automóvil "propio"
    Y capturo en tipo de combustible "gas" 
    Y capturo en ocupación "estudiante"
    Y capturo en cuenta con servicio de "IMSS"
    Y capturo en que enfermedades existen la familia "Alergias"
    Cuando presiono el botón "Registrar"
    Entonces el sistema me muestra el mensaje "El registro se realizó correctamente."
