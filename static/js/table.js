$(document).ready(function() {
    $('#tabla-responsives').DataTable({
        responsive: true, 
        pageLength: 10,    
        lengthMenu: [10, 25, 50, 100],  
        language: {
            lengthMenu: "Mostrar _MENU_ registros por página",  
            info: "",  
            infoEmpty: "",  
            zeroRecords: "No se encontraron resultados",
        },
        autoWidth: false,
        pagingType: "full_numbers", 
        dom: '<"top"f>rt<"bottom"ilp><"clear">',
    });
});