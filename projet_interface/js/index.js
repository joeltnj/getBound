


// // xhr = new XMLHttpRequest()
// // xhr.open("get", "#")
// // xhr.onreadystatechange = () => {
// //     if (xhr.readyState === 4 && xhr.status === 200) {
// //         const rep = JSON.parse(xhr.responseText);
// //     }
// // }
// // xhr.send()


// function deleteElementSiEcranPetit() {
//     let doc = document.querySelector(".category-list")
//     if (doc) {
//         if (window.innerWidth < 667) {
//             doc.remove();
//         }else{
//             // let parentElement = document.getElementById("parentElement"); // Remplacez "parentElement" par l'ID de l'élément parent.
//             // // parentElement.appendChild(doc);
//             if (sibling) {
//                 sibling.insertAdjacentElement("beforebegin", doc);
//             }
//         }
//     }
// }


// function handleResize() {
//     deleteElementSiEcranPetit();
// }

// window.addEventListener("resize", handleResize);

// // Appelez la fonction au chargement de la page pour gérer l'état initial
// deleteElementSiEcranPetit();







// let doc=document.querySelector(".burger")

// doc.addEventListener("click",)
//quend je clique j'affiche le menu deroulant
// --------------------------------------------------------------------------


// Pour le bouton burger
(function () {
    let verif = false;
    const element = document.querySelector('.bar-burger');
    const subElements = document.querySelector('.item-burger-visible');

    function handleClick(e) {
        if (e.target === element) {
            subElements.classList.toggle("item-burger-hidden");
            e.stopPropagation();
            verif = true;
        }
    }

    function handleDocumentClick(a) {
        if (!subElements.contains(a.target)) {
            if (verif) {
                subElements.classList.add("item-burger-hidden");
                verif = false;
            }
        }
    }

    // Fonction pour exécuter le code si la largeur est supérieure à 667px
    function executeOnLargeScreen() {
        if (window.innerWidth > 667) {
            element.addEventListener('click', handleClick);
            document.addEventListener('click', handleDocumentClick);
        } else {
            element.removeEventListener('click', handleClick);
            document.removeEventListener('click', handleDocumentClick);
        }
    }

    // Appeler la fonction de vérification initiale au chargement de la page
    executeOnLargeScreen();

    // Attacher l'événement de redimensionnement de la fenêtre pour vérifier lorsque la taille de la fenêtre change
    window.addEventListener('resize', executeOnLargeScreen);
})();

// Pour les tiret-burger
// (function () {
//     let verif = false;
//     const elements = document.querySelectorAll('.tiret-burger');
//     const subElements = document.querySelector('.visible');

//     for (const element of elements) {
//         function handleTiretBurgerClick(e) {
//             if (e.target === element) {
//                 subElements.classList.toggle("itedm-burger");
//                 e.stopPropagation();
//                 verif = true;
//             }
//         }

//         function handleDocumentClick(a) {
//             if (!subElements.contains(a.target)) {
//                 if (verif) {
//                     subElements.classList.add("item-burger");
//                     verif = false;
//                 }
//             }
//         }

//         element.addEventListener('click', handleTiretBurgerClick);
//         document.addEventListener('click', handleDocumentClick);
//     }

    // Fonction pour exécuter le code si la largeur est supérieure à 667px
//     function executeOnLargeScreen() {
//         if (window.innerWidth > 667) {
//             for (const element of elements) {
//                 element.addEventListener('click', handleTiretBurgerClick);
//             }
//             document.addEventListener('click', handleDocumentClick);
//         } else {
//             for (const element of elements) {
//                 element.removeEventListener('click', handleTiretBurgerClick);
//             }
//             document.removeEventListener('click', handleDocumentClick);
//         }
//     }

//     // Appeler la fonction de vérification initiale au chargement de la page
//     executeOnLargeScreen();

//     // Attacher l'événement de redimensionnement de la fenêtre pour vérifier lorsque la taille de la fenêtre change
//     window.addEventListener('resize', executeOnLargeScreen);
// })();

// Pour le menu déroulant de connexion
(function () {
    let verif = false;
    const element = document.querySelector('.signin');
    const subElements = document.querySelector('.item-signin-visible');

    function handleSigninClick(e) {
        if (e.target === element) {
            subElements.classList.toggle("item-signin-hidden");
            e.stopPropagation();
            verif = true;
        }
    }

    function handleDocumentClick(a) {
        if (!subElements.contains(a.target)) {
            if (verif) {
                subElements.classList.add("item-signin-hidden");
                verif = false;
            }
        }
    }

    // Fonction pour exécuter le code si la largeur est supérieure à 667px
    function executeOnLargeScreen() {
        if (window.innerWidth > 667) {
            element.addEventListener('click', handleSigninClick);
            document.addEventListener('click', handleDocumentClick);
        } else {
            element.removeEventListener('click', handleSigninClick);
            document.removeEventListener('click', handleDocumentClick);
        }
    }

    // Appeler la fonction de vérification initiale au chargement de la page
    executeOnLargeScreen();

    // Attacher l'événement de redimensionnement de la fenêtre pour vérifier lorsque la taille de la fenêtre change
    window.addEventListener('resize', executeOnLargeScreen);
})();










// ------------------------------------------------------------------------
// moins 667px
// (function () {
//     let verif = false;
//     const element = document.querySelector('.bar-burger');
//     const subElements = document.querySelector('.item-burger-visible');

//     function handleClick(e) {
//         console.log("ok");
//         if (e.target === element) {
//             console.log("jjfjfjfjf");
//             subElements.classList.toggle("item-burger-hidden");
//             e.stopPropagation();
//             verif = true;
//         }
//     }

//     function handleDocumentClick(a) {
//         if (!subElements.contains(a.target)) {
//             if (verif) {
//                 subElements.classList.add("item-burger-hidden");
//                 verif = false;
//             }
//         }
//     }

//     // Fonction pour exécuter votre code si la largeur est inférieure à 667px
//     function executeOnSmallScreen() {
//         if (window.innerWidth < 667) {
//             console.log("mmmmmmm");
//             element.addEventListener('click', handleClick);
//             document.addEventListener('click', handleDocumentClick);
//         } else {
//             element.removeEventListener('click', handleClick);
//             document.removeEventListener('click', handleDocumentClick);
//         }
//     }

//     // Appeler la fonction de vérification initiale au chargement de la page
//     executeOnSmallScreen();

//     // Attacher l'événement de redimensionnement de la fenêtre pour vérifier lorsque la taille de la fenêtre change
//     window.addEventListener('resize', executeOnSmallScreen);
// })();


// -----------------------------------


// pour les sub-item sign du button burger
(function () {
    let verif = false; //ici sous-items sont caché
    const element = document.querySelector('.item-mobile');
    const subElements = document.querySelector('.item-signin-mobile-visible');

    element.addEventListener('click', (e) => {
        if (e.target === element) {
            subElements.classList.toggle("item-signin-mobile-hidden");
            e.stopPropagation();
            verif = true; //pour dire que les sous-items sont visible
        }
    });

    document.addEventListener('click', (a) => {
        console.log(a.target);
        if (!subElements.contains(a.target)) {      //la methode contains renvois true si subelement est parent "direct" de "e.target"
            if (verif) {
                subElements.classList.add("item-signin-mobile-hidden");
                verif = false;
            }
        }
    });

    
})();//fin menu deroulant


// ------------------------


//fonction qui fonctionne et je veux remplacer par -667
// (function () {
//     let verif = false; //ici sous-items sont caché
//     const element = document.querySelector('.bar-burger');
//     const subElements = document.querySelector('.burger');

//     element.addEventListener('click', (e) => {
//         if (e.target === element) {
//             subElements.classList.toggle("item");
//             // element.classList.toggle("item")
//             e.stopPropagation();
//             verif = true; //pour dire que les sous-items sont visible
//         }
//     });
//     document.addEventListener('click', (a) => {
//         console.log(a.target);
//         if (!subElements.contains(a.target)) {      //la methode contains renvois true si subelement est parent "direct" de "e.target"
//             if (verif) {
//                 subElements.classList.remove("item");
//                 verif = false;
//             }
//         }
//     });
// })();//fin menu deroulant

(function () {
    let verif = false; // ici, les sous-éléments sont cachés
    const element = document.querySelector('.bar-burger');
    const subElements = document.querySelector('.burger');

    function handleClick(e) {
        if (e.target === element) {
            subElements.classList.toggle("item");
            e.stopPropagation();
            verif = true; // pour indiquer que les sous-éléments sont visibles
        }
    }

    function handleDocumentClick(a) {
        console.log(a.target);
        if (!subElements.contains(a.target)) {
            if (verif) {
                subElements.classList.remove("item");
                verif = false;
            }
        }
    }

    // Fonction pour exécuter le code si la largeur est supérieure à 667px
    function executeOnLargeScreen() {
        if (window.innerWidth < 667) {
            element.addEventListener('click', handleClick);
            document.addEventListener('click', handleDocumentClick);
        } else {
            element.removeEventListener('click', handleClick);
            document.removeEventListener('click', handleDocumentClick);
        }
    }

    // Appeler la fonction de vérification initiale au chargement de la page
    executeOnLargeScreen();

    // Attacher l'événement de redimensionnement de la fenêtre pour vérifier lorsque la taille de la fenêtre change
    window.addEventListener('resize', executeOnLargeScreen);
})();




//-667px avc anime
// (function () {
//     let verif = false;
//     const element = document.querySelector('.bar-burger');
//     const subElements = document.querySelector('.item-burger-visible');

//     function handleClick(e) {
//         subElements.classList.toggle("item-burger-hidden");
//         e.stopPropagation();
//         verif = true;
//     }

//     function handleDocumentClick(a) {
//         if (!subElements.contains(a.target)) {
//             if (verif) {
//                 subElements.classList.remove("item-burger-hidden");
//                 verif = false;
//             }
//         }
//     }

//     function executeOnSmallScreen() {
//         if (window.innerWidth <= 667) {
//             element.addEventListener('click', handleClick);
//             document.addEventListener('click', handleDocumentClick);
//         } else {
//             element.removeEventListener('click', handleClick);
//             document.removeEventListener('click', handleDocumentClick);
//         }
//     }

//     window.addEventListener('resize', executeOnSmallScreen);

//     executeOnSmallScreen();
// })();
