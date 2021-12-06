function desabilitarUsuario(url){
    Swal.fire({
        title: '¿Está seguro que desea dar de baja el usuario?',
        text: "¡No podrás revertir esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, estoy seguro',
        cancelButtonText: 'Cancelar'
    }).then(function(result) {
        if (result.isConfirmed) {
            document.getElementById('formBajaUsuario').action = url;
            document.getElementById('formBajaUsuario').submit();
        }
    })
}