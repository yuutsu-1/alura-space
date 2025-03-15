function abrirModal(type = 'login') {
    document.getElementById('DiagModal').showModal();
}

document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('DiagModal');
    const modalOverlay = document.getElementById('authModal');

    // Fecha o modal se clicar fora do conteúdo
    modalOverlay.addEventListener('click', function(e) {
        if (e.target === modalOverlay) {
            modal.close();
        }
    });

    // Fecha o modal com a tecla ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.open) {
            modal.close();
        }
    });
});