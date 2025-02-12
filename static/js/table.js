$(document).ready(function () {
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



// Para mi excel

document.getElementById("exportBtn").addEventListener("click", function () {
    var wb = XLSX.utils.table_to_book(document.getElementById('tabla-responsives'), { sheet: "Sheet 1" });
    XLSX.writeFile(wb, 'contactos.xlsx');
});
