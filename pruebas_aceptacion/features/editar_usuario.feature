Característica: Como administrador me gustaría editar
                un usuario para tener sus datos actualizados.

    Escenario: Datos de edición correctos
    Dado que me encuentro logueado en el sistema
    Y selecciono el botón "Usuarios"
    Y selecciono el usuario a modificar
    Y cambio el primer apellido por "Martínez"
    Cuando presiono el botón guardar
    Entonces el sistema me mostrará el mensaje: "¡Registro actualizado con éxito!"

    Escenario: Datos de edición incorrectos
    Dado que me encuentro logueado en el sistema
    Y selecciono el botón "Usuarios"
    Y selecciono el usuario a modificar
    Y cambio el código postal por "cod12"
    Cuando presiono el botón guardar
    Entonces el sistema me mostrará el mensaje: "Hay datos inválidos en el formulario."