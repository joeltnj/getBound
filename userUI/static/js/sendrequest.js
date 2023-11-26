document.addEventListener("DOMContentLoaded", function () {
    // Ajouter un écouteur d'événement au chargement du document
    var userInfoParagraph = document.getElementById("userInfo");
    if (userInfoParagraph) {
        userInfoParagraph.addEventListener("click", getUserInfo);
    }
});

function getUserInfo() {
    // Envoyer une requête vers le serveur Flask en utilisant Fetch
    fetch("/get_user_info")
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erreur HTTP! Statut: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Mettre à jour le paragraphe avec les informations de l'utilisateur
            document.getElementById("userInfo").innerText = "Nom: " + data.name + ", Âge: " + data.age;
        })
        .catch(error => {
            console.error("Erreur lors de la récupération des informations de l'utilisateur:", error);
        });
}


document.addEventListener("DOMContentLoaded", function () {
    // Ajouter un écouteur d'événement au chargement du document
    var userInfoParagraph = document.getElementById("userInfo");
    if (userInfoParagraph) {
        userInfoParagraph.addEventListener("click", getUserInfo);
    }
});

function getUserInfo() {
    // Créer une instance de XMLHttpRequest
    var xhr = new XMLHttpRequest();

    // Configurer la requête
    xhr.open("GET", "/get_user_info", true);

    // Définir la fonction de rappel lorsque la réponse est prête
    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 300) {
            // Mettre à jour le paragraphe avec les informations de l'utilisateur
            var data = JSON.parse(xhr.responseText);
            document.getElementById("userInfo").innerText = "Nom: " + data.name + ", Âge: " + data.age;
        } else {
            console.error("Erreur lors de la récupération des informations de l'utilisateur. Statut: " + xhr.status);
        }
    };

    // Gérer les erreurs réseau
    xhr.onerror = function () {
        console.error("Erreur réseau lors de la récupération des informations de l'utilisateur.");
    };

    // Envoyer la requête
    xhr.send();
}
