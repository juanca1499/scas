$(document).ready(function() {
    if($("#id_estado").prop('selectedIndex')==""){
        $("#id_municipio").attr('disabled',true);
        $('#id_municipio').prop('selectedIndex',0);
        $("#id_localidad").attr('disabled',true);
        $('#id_localidad').prop('selectedIndex',0);
    }
    else if($("#id_municipio").prop('selectedIndex')==""){
        $("#id_localidad").attr('disabled',true);
        $('#id_localidad').prop('selectedIndex',0);
        cargarMunicipios($("#id_estado").prop('selectedIndex'));
    }
    else{
        cargarMunicipios($("#id_estado").prop('selectedIndex'));
        cargarLocalidades($("#id_municipio").prop('selectedIndex'));
    }
    
    $("#id_estado").on('change', function(){
        if($("#id_estado").prop('selectedIndex')==""){
            $("#id_municipio").attr('disabled',true);
            $('#id_municipio').prop('selectedIndex',0);
            $("#id_localidad").attr('disabled',true);
            $('#id_localidad').prop('selectedIndex',-1);
        }
    });

    $("#id_estado").on('change', function(){ 
        var token = $('[name="csrfmiddlewaretoken"]').val();  
        $.ajax({
            type: "post",
            url: `/solicitudes/municipios/`,
            data: {'id':this.value, 'csrfmiddlewaretoken': token},
            success: function (response) {
                var html = "";
                if (response[0].hasOwnProperty('error')){
                    html+=`<option value="0">${response[0].error}</option>`;
                }
                else{
                    $.each(response, function (llave, valor) { 
                        html+=`<option value="${valor.id}">${valor.nombre}</option>`;
                    });
                }
                $("#id_municipio").html(html);
                $("#id_municipio").attr('disabled',false);
                $('#id_localidad').prop('selectedIndex',0);
                $("#id_localidad").attr('disabled',true);
            },
            error: function (param) { 
                console.log('Error en la petición')
            }
        });
    });

    $("#id_municipio").on('change', function(){ 
        var token = $('[name="csrfmiddlewaretoken"]').val();  
        $.ajax({
            type: "post",
            url: `/solicitudes/localidades/`,
            data: {'id':this.value, 'csrfmiddlewaretoken': token},
            success: function (response) {
                var html = "";
                if (response[0].hasOwnProperty('error')){
                    html+=`<option value="0">${response[0].error}</option>`;
                }
                else{
                    $.each(response, function (llave, valor) { 
                        html+=`<option value="${valor.id}">${valor.nombre}</option>`;
                    });
                }
                $("#id_localidad").html(html);
                $("#id_localidad").attr('disabled',false);
            },
            error: function (param) { 
                console.log('Error en la petición')
            }
        });
    });

    function cargarMunicipios(id){ 
        var token = $('[name="csrfmiddlewaretoken"]').val();  
        $.ajax({
            type: "post",
            url: `/solicitudes/municipios/`,
            data: {'id':id, 'csrfmiddlewaretoken': token},
            success: function (response) {
                var html = "";
                if (response[0].hasOwnProperty('error')){
                    html+=`<option value="0">${response[0].error}</option>`;
                }
                else{
                    $.each(response, function (llave, valor) { 
                        html+=`<option value="${valor.id}">${valor.nombre}</option>`;
                    });
                }
                var idMunicipio = $("#id_municipio").prop('selectedIndex');
                $("#id_municipio").html(html);
                
                if(idMunicipio != ""){
                    $('#id_municipio').val(idMunicipio);
                }
            },
            error: function (param) { 
                console.log('Error en la petición')
            }
        });
    }

    function cargarLocalidades(id){ 
        var token = $('[name="csrfmiddlewaretoken"]').val();  
        $.ajax({
            type: "post",
            url: `/solicitudes/localidades/`,
            data: {'id':id, 'csrfmiddlewaretoken': token},
            success: function (response) {
                var html = "";
                if (response[0].hasOwnProperty('error')){
                    html+=`<option value="0">${response[0].error}</option>`;
                }
                else{
                    $.each(response, function (llave, valor) { 
                        html+=`<option value="${valor.id}">${valor.nombre}</option>`;
                    });
                }
                var idLocalidad = $("#id_localidad").prop('selectedIndex');               
                $("#id_localidad").html(html);
                
                if(idLocalidad != ""){
                    $('#id_localidad').val(idLocalidad);
                }
            },
            error: function (param) { 
                console.log('Error en la petición')
            }
        });
    }
});