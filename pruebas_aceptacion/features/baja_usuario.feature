Característica: Como administrador me gustaría 
                poder dar de baja un usuario para
                saber cuando ya no colabore en el organismo.

    Escenario: Baja de usuario correcto
    Dado que me encuentro logueado en el sistema
    Y selecciono el botón "Usuarios"
    Y selecciono el usuario a dar de baja
    Cuando confirmo la acción
    Entonces el sistema deberá mostrar el mensaje: "¡Cuenta dada de baja con éxito!"