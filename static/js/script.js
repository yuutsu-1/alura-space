document.addEventListener('htmx:beforeRequest', function(event) {
    const form = event.detail.elt.closest('form');
    if (!form) return;

    const submitButton = form.querySelector('button[type="submit"]');
    if (!submitButton) return;

    if (submitButton.classList.contains('loading')) {
        event.preventDefault();
        return;
    }

    // Adiciona o spinner
    const spinner = document.createElement('span');
    spinner.className = 'loader';
    submitButton.textContent = '';
    submitButton.appendChild(spinner);
    
    submitButton.classList.add('loading');
});

document.addEventListener('htmx:afterRequest', function(event) {
    const form = event.detail.elt.closest('form');
    if (!form) return;

    const submitButton = form.querySelector('button[type="submit"]');
    if (!submitButton) return;

    // Remove o spinner
    const spinner = submitButton.querySelector('.loader');
    if (spinner) {
        spinner.remove();
    }
    submitButton.classList.remove('loading');
});

// Para lidar com erros também
document.addEventListener('htmx:responseError', function(event) {
    const form = event.detail.elt.closest('form');
    if (!form) return;

    const submitButton = form.querySelector('button[type="submit"]');
    if (!submitButton) return;

    // Remove o spinner em caso de erro
    const spinner = submitButton.querySelector('.loader');
    if (spinner) {
        spinner.remove();
    }
    submitButton.classList.remove('loading');
});


document.addEventListener('htmx:beforeSwap', function(event) {
    if (event.detail.elt.classList.contains('login__form') && !event.detail.xhr.response) {
        location.reload()
            
    }
});


