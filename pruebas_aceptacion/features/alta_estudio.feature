Característica: Como administrador me gustaría agregar 
                un estudio socioeconómico a una solicitud 
                para valorar si se dará el apoyo al solicitante
                Como encuestador me gustaría agregar 
                un estudio socioeconómico a una solicitud 
                para valorar si se dará el apoyo al solicitante.

    Escenario: Datos de estudio socioeconómico correctos.
        Dado que accedo al login
        Y capturo usuario "juca" y contraseña "juca123"
        Y presiono ingresar
        Y me dirijo a solicitudes
        Y selecciono visualizar solicitud "1"
        Y selecciono agregar estudio socioeconomico
        Y capturo en la fecha actual "17-11-2021"
        Y subo un archivo como comprobante de domicilio "C:/Users/secre/Desktop/Pruebas/comprobante.jpg"
        Y subo un archivo como la credencial de elector "C:/Users/secre/Desktop/Pruebas/ine.jpg"
        Y capturo la edad "18"
        Y capturo el telefono "4921736547"
        Y activo la casilla en es cabeza de familia
        Y elijo en ocupación "Estudiante"
        Y elijo en escolaridad "Preparatoria"
        Y elijo en estado civil "Soltero (a)"
        Y elijo en discapacidad "Ninguna"
        Y elijo en automovil "Propio"
        Y elijo en tipo de combustible "Gasolina"
        Y capturo calle "Real de angeles"
        Y capturo en el numero exterior "43"
        Y capturo colonia "Camino Real"
        Y capturo código postal "98613"
        Y elijo en estado "Zacatecas"
        Y elijo en municipio "Guadalupe"
        Y elijo en localidad "Tacoaleche"
        Y activo la casilla en 3 plantas
        Y activo la casilla en sala/comedor
        Y activo la casilla en cocina 
        Y activo la casilla en cochera
        Y capturo el numero de recamaras "2"
        Y capturo el numero de baños "2"
        Y elijo en el piso es "Tierra"
        Y elijo en el techo es "Concreto"
        Y elijo en su casa es "Propia, pagada y escriturada"
        Y activo la casilla en energia electrica
        Y activo la casilla en drenaje
        Y activo la casilla en agua potable
        Y activo la casilla en lavadora
        Y activo la casilla en radio
        Y activo la casilla en dvd
        Y elijo en servio de salud "IMSS"
        Y activo la casilla en cancer
        Y activo la casilla en epilepsia
        Y activo la casilla en presion baja
        Cuando presiono botón "Agregar"
        Entonces el sistema me muestra "Estudio socioeconómico guardado exitosamente."

    Escenario: Datos de estudio socioeconómico incorrectos.
        Dado que accedo al login
        Y capturo usuario "juca" y contraseña "juca123"
        Y presiono ingresar
        Y me dirijo a solicitudes
        Y selecciono visualizar solicitud "2"
        Y selecciono agregar estudio socioeconomico 
        Y capturo en la fecha actual "17-11-2021"
        Y subo un archivo como comprobante de domicilio "C:/Users/secre/Desktop/Pruebas/error_1.docx"
        Y subo un archivo como la credencial de elector "C:/Users/secre/Desktop/Pruebas/error_2.docx"
        Y capturo la edad "18"
        Y capturo el telefono "4921736547"
        Y activo la casilla en es cabeza de familia
        Y elijo en ocupación "Estudiante"
        Y elijo en escolaridad "Preparatoria"
        Y elijo en estado civil "Soltero (a)"
        Y elijo en discapacidad "Ninguna"
        Y elijo en automovil "Propio"
        Y elijo en tipo de combustible "Gasolina"
        Y capturo calle "Real de angeles"
        Y capturo en el numero exterior "43"
        Y capturo colonia "Camino Real"
        Y capturo código postal "98613"
        Y elijo en estado "Zacatecas"
        Y elijo en municipio "Guadalupe"
        Y elijo en localidad "Tacoaleche"
        Y activo la casilla en 3 plantas
        Y activo la casilla en sala/comedor
        Y activo la casilla en cocina 
        Y activo la casilla en cochera
        Y capturo el numero de recamaras "1"
        Y capturo el numero de baños "2"
        Y elijo en el piso es "Tierra"
        Y elijo en el techo es "Concreto"
        Y elijo en su casa es "Propia, pagada y escriturada"
        Y activo la casilla en energia electrica
        Y activo la casilla en drenaje
        Y activo la casilla en agua potable
        Y activo la casilla en lavadora
        Y activo la casilla en radio
        Y activo la casilla en dvd
        Y elijo en servio de salud "IMSS"
        Y activo la casilla en cancer
        Y activo la casilla en epilepsia
        Y activo la casilla en presion baja
        Cuando presiono botón "Agregar"
        Entonces el sistema me muestra "Hay datos inválidos en el formulario."