Característica: Como administrador me gustaría editar
                un usuario para tener sus datos actualizados.

    Escenario: Datos de edición correctos
    Dado que me encuentro logueado en el sistema
    Y selecciono el botón de "Usuarios"
    Y selecciono el usuario a modificar
    Y cambio el primer apellido por "García"
    Cuando presiono el botón guardar
    Entonces el sistema me mostrará el mensaje: "Registro actualizado con éxito."

    Escenario: Datos de edición incorrectos
    Dado que me encuentro logueado en el sistema
    Y selecciono el botón de usuarios
    Y selecciono el usuario a modificar
    Y cambio el primer apellido por ""
    Cuando presiono el botón guardar
    Entonces el sistema me mostrará el mensaje: "Hay datos incorrectos en el formulario."