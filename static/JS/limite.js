
document.getElementById('tipoProdutos').addEventListener('change', function() {
    var categoria = this.value;

    // Ocultar todos os setores
    document.querySelectorAll('.ingrediente').forEach(function(element) {
        element.style.display = 'none';
    });

    // Mostrar o setor correspondente à categoria selecionada
    if (categoria === 'Artesanal') {
        document.getElementById('hamburguer-artesanal').style.display = 'block';
    } else if (categoria === 'Tradicional') {
        document.getElementById('hamburguer-tradicional').style.display = 'block';
    } else if (categoria === 'Porcao') {
        document.getElementById('porcao').style.display = 'block';
    } else if (categoria === 'Sobremesa') {
        document.getElementById('sobremesa').style.display = 'block';
    }
});
function permitirApenasUmCheckbox(checkbox) {
    const checkboxes = document.getElementsByName(checkbox.name);
    checkboxes.forEach((cb) => {
        if (cb !== checkbox) {
            cb.checked = false;
        }
    });
}

const form = document.getElementById('form-hamburguer');
form.addEventListener('submit', function() {
    const checkboxes = document.getElementsByName('tamanho');
    let selected = false;
    checkboxes.forEach((checkbox) => {
        if (checkbox.checked) {
            selected = true;
        }
    });
    if (!selected) {
        alert('Selecione um tamanho para o hambúrguer.');
        event.preventDefault();
    }
});
