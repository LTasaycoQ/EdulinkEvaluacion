
document.querySelectorAll('.btn-danger').forEach(button => {
    button.addEventListener('click', function (e) {
        e.preventDefault();  

        Swal.fire({
            title: '¿Estás seguro?',
            text: '¡Quiere eliminar a esta persona',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Sí, eliminar',
            cancelButtonText: 'Cancelar',
        }).then((result) => {
            if (result.isConfirmed) {
                this.closest('form').submit();
            }
        });
    });
});


document.querySelectorAll('.btn-success').forEach(button => {
    button.addEventListener('click', function (e) {
        e.preventDefault();  

        Swal.fire({
            title: '¿Estás seguro?',
            text: '¡Quiere Restaurar a esta persona',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Sí, Restaurar',
            cancelButtonText: 'Cancelar',
        }).then((result) => {
            if (result.isConfirmed) {
                this.closest('form').submit();
            }
        });
    });
});





