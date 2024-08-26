document.addEventListener("DOMContentLoaded", function() {
    const btnParticulier = document.getElementById('btn-particulier');
    const btnProfessionnel = document.getElementById('btn-professionnel');
    const formParticulier = document.getElementById('form-particulier');
    const formProfessionnel = document.getElementById('form-professionnel');

    btnParticulier.addEventListener('click', function() {
        formParticulier.classList.add('active');
        formProfessionnel.classList.remove('active');
        btnParticulier.classList.add('active');
        btnProfessionnel.classList.remove('active');
    });

    btnProfessionnel.addEventListener('click', function() {
        formProfessionnel.classList.add('active');
        formParticulier.classList.remove('active');
        btnProfessionnel.classList.add('active');
        btnParticulier.classList.remove('active');
    });
});
