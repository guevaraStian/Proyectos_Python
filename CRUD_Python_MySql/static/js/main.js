const btnDelete = document.querySelectorAll('.btn-delete')

if(btnDelete){
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn)=>{
        btn.addEventListener('click', (e)=>{
            if(!confirm('Desea eliminar el dato de la base de datos?')){
                e.preventDefault();
            }
        });
    });
}