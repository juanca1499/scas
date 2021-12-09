function desabilitarUsuario(url){
    Swal.fire({
        title: '¿Está seguro que desea dar de baja el usuario?',
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

function habilitarUsuario(url){
    Swal.fire({
        title: '¿Está seguro que desea dar de alta el usuario?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, estoy seguro',
        cancelButtonText: 'Cancelar'
    }).then(function(result) {
        if (result.isConfirmed) {
            document.getElementById('formAltaUsuario').action = url;
            document.getElementById('formAltaUsuario').submit();
        }
    })
}