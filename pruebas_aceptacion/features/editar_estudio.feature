Característica: Como administrador me gustaría 
                editar la información de un estudio 
                socioeconómico para corregir datos 
                que estén erróneos sobre el solicitante.

                Como encuestador me gustaría editar la 
                información de un estudio socioeconómico 
                para corregir datos que estén erróneos 
                sobre el solicitante.

    Escenario: Datos de edición de estudio socioeconómico correctos.    
        Dado que accedo al login
        Y capturo usuario "juca" y contraseña "juca123"
        Y presiono ingresar
        Y me dirijo a estudios socioeconomicos
        Y selecciono editar estudio
        Y subo un archivo como comprobante de domicilio "C:/Users/secre/Desktop/Pruebas/comprobante_correccion.jpg"
        Y subo un archivo como la credencial de elector "C:/Users/secre/Desktop/Pruebas/ine_correccion.jpg"
        Y cambio la colonia por "CTM"
        Cuando presiono botón "Guardar"
        Entonces el sistema me muestra "Estudio socioeconómico actualizado"

    Escenario: Datos de edición de estudio socioeconómico incorrectos.    
        Dado que accedo al login
        Y capturo usuario "juca" y contraseña "juca123"
        Y presiono ingresar
        Y me dirijo a estudios socioeconomicos
        Y selecciono editar estudio
        Y subo un archivo como comprobante de domicilio "C:/Users/secre/Desktop/Pruebas/error_1.docx"
        Y subo un archivo como la credencial de elector "C:/Users/secre/Desktop/Pruebas/error_2.docx"
        Y cambio la colonia por "CTM"
        Cuando presiono botón "Guardar"
        Entonces el sistema me muestra "Hay datos inválidos en el formulario"