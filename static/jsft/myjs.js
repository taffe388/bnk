$(document).ready(function() {
    // Ouvrir le popup lors du clic sur le bouton "Submit"
    $("#openPopup").click(function() {
        $("#securityPopup").show();
        startLoadingAnimation();
    });

    // Fermer le popup lors du clic sur la croix
    $("#closePopup").click(function() {
        $("#securityPopup").hide();
        stopLoadingAnimation();
    });

    // Validation du code de sécurité
    $("#submitCode").click(function() {
        var securityCode = $("#securityCode").val();
        if (securityCode.length === 8) {
            // Code de sécurité valide, continuez avec l'envoi du formulaire
            stopLoadingAnimation();
            $("#securityPopup").hide();
            // Ajoutez ici la logique pour envoyer le formulaire
        } else {
            // Code de sécurité invalide, affichez un message d'erreur
            alert("Le code de sécurité doit comporter 8 chiffres.");
        }
    });

    // Fonction pour démarrer l'animation de chargement
    function startLoadingAnimation() {
        // Ajoutez ici votre animation de chargement
    }

    // Fonction pour arrêter l'animation de chargement
    function stopLoadingAnimation() {
        // Arrêtez l'animation de chargement ici
    }
});
