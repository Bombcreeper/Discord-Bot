// Récupération des éléments du DOM
const addVignetteBtn = document.getElementById('add-vignette-btn');
const popup = document.getElementById('popup');
const validateBtn = document.getElementById('validate-btn');
const closePopupBtn = document.getElementById('close-popup-btn');
const vignetteText = document.getElementById('vignette-text');
const vignetteValue = document.getElementById('vignette-value');
const vignetteImage = document.getElementById('vignette-image');
const vignetteContainer = document.getElementById('vignette-container');

// Afficher le pop-up lorsque le bouton est cliqué
addVignetteBtn.addEventListener('click', function() {
    popup.style.display = 'flex';
});

// Fermer le pop-up sans ajouter de vignette
closePopupBtn.addEventListener('click', function() {
    popup.style.display = 'none';
});

// Ajouter une vignette lorsque le bouton de validation est cliqué
validateBtn.addEventListener('click', function() {
    const text = vignetteText.value;
    const value = vignetteValue.value;
    const imageFile = vignetteImage.files[0]; // Récupérer le fichier image

    if (imageFile) {
        const reader = new FileReader();

        reader.onload = function(event) {
            // Créer une nouvelle vignette
            const vignette = document.createElement('div');
            vignette.className = 'vignette';

            // Ajouter l'image à la vignette
            const image = document.createElement('img');
            image.src = event.target.result; // Utiliser l'image lue
            vignette.appendChild(image);

            // Ajouter le texte à la vignette
            const textElement = document.createElement('p');
            textElement.textContent = text;
            textElement.className = 'vignette-text'; // Ajouter une classe pour le texte
            vignette.appendChild(textElement);

            // Ajouter la valeur (prix) à la vignette
            const valueElement = document.createElement('div');
            valueElement.textContent = `${value} €`;
            valueElement.className = 'vignette-value'; // Ajouter une classe pour la valeur (prix)
            vignette.appendChild(valueElement);

            // Ajouter la vignette au conteneur
            vignetteContainer.appendChild(vignette);

            // Scroller vers le bas pour voir la nouvelle vignette si nécessaire
            vignette.scrollIntoView({ behavior: 'smooth', block: 'end' });

            // Fermer le pop-up
            popup.style.display = 'none';

            // Réinitialiser les champs du formulaire
            vignetteText.value = '';
            vignetteValue.value = '';
            vignetteImage.value = '';
        };

        // Lire le fichier image
        reader.readAsDataURL(imageFile);
    } else {
        alert('Veuillez sélectionner une image.');
    }
});
