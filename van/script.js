
const addVignetteBtn = document.getElementById('add-vignette-btn');
const popup = document.getElementById('popup');
const validateBtn = document.getElementById('validate-btn');
const closePopupBtn = document.getElementById('close-popup-btn');
const vignetteText = document.getElementById('vignette-text');
const vignetteValue = document.getElementById('vignette-value');
const vignetteImage = document.getElementById('vignette-image');
const vignetteContainer = document.getElementById('vignette-container');


addVignetteBtn.addEventListener('click', function() {
    popup.style.display = 'flex';
});

closePopupBtn.addEventListener('click', function() {
    popup.style.display = 'none';
    vignetteText.value = '';
    vignetteValue.value = '';
    vignetteImage.value = '';
});

validateBtn.addEventListener('click', function() {
    const text = vignetteText.value;
    const value = vignetteValue.value;
    const imageFile = vignetteImage.files[0]; 
    
    if (imageFile) {
        const reader = new FileReader();

        reader.onload = function(event) {
            const vignette = document.createElement('div');
            vignette.className = 'vignette';

           
            const image = document.createElement('img');
            image.src = event.target.result; 
            vignette.appendChild(image);

            
            const textElement = document.createElement('p');
            textElement.textContent = `${text} - ${value}`;
            vignette.appendChild(textElement);

            
            vignetteContainer.appendChild(vignette);

           
            vignette.scrollIntoView({ behavior: 'smooth', block: 'end' });

           
            popup.style.display = 'none';

           
            vignetteText.value = '';
            vignetteValue.value = '';
            vignetteImage.value = '';

            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'delete-btn';
            deleteBtn.innerHTML = '✖'; 
            vignette.appendChild(deleteBtn);

            deleteBtn.addEventListener('click', function() {
                if (confirm('Êtes-vous sûr de vouloir supprimer cette vignette ?')) {
                    vignette.remove();}
                });
        };

        reader.readAsDataURL(imageFile);
    } else {
        alert('Veuillez sélectionner une image.');
    }
});

