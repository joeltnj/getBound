


// // xhr = new XMLHttpRequest()
// // xhr.open("get", "#")
// // xhr.onreadystatechange = () => {
// //     if (xhr.readyState === 4 && xhr.status === 200) {
// //         const rep = JSON.parse(xhr.responseText);
// //     }
// // }
// // xhr.send()


// // function deleteElementSiEcranPetit() {
// //     let doc = document.querySelector(".category-list")
// //     if (doc) {
// //         if (window.innerWidth < 667) {
// //             doc.remove();
// //         }else{
// //             // let parentElement = document.getElementById("parentElement"); // Remplacez "parentElement" par l'ID de l'élément parent.
// //             // // parentElement.appendChild(doc);
// //             if (sibling) {
// //                 sibling.insertAdjacentElement("beforebegin", doc);
// //             }
// //         }
// //     }
// // }


// // function handleResize() {
// //     deleteElementSiEcranPetit();
// // }

// // window.addEventListener("resize", handleResize);

// // // Appelez la fonction au chargement de la page pour gérer l'état initial
// // deleteElementSiEcranPetit();







// // let doc=document.querySelector(".burger")

// // doc.addEventListener("click",)
// //quend je clique j'affiche le menu deroulant









// // pour le button burger
// (function () {
//     let verif = false;
//     const element = document.querySelector('.bar-burger');
//     const subElements = document.querySelector('.item-burger-visible');

//     element.addEventListener('click', (e) => {
//         if (e.target === element) {
//             subElements.classList.toggle("item-burger-hidden");
//             e.stopPropagation();
//             verif = true;
//         }
//     });
//     document.addEventListener('click', (a) => {
//         // console.log(a.target);
//         if (!subElements.contains(a.target)) {      //la methode contains renvois true si subelement est parent "direct" de "e.target"
//             if (verif) {
//                 subElements.classList.add("item-burger-hidden");
//                 verif = false;
//             }
//         }
//     });
// })();//fin menu deroulant

// // pour les tiret-burgur
// (function () {
//     let verif = false;
//     const element = document.querySelectorAll('.tiret-burger');
//     const subElements = document.querySelector('.visible');
//     // parce que c'est un array, on doit le parcourir et exploiter chacun de son item
//     for (const el of element) {
//         // console.log(el);
//         el.addEventListener('click', (e) => {
//             // console.log(e.target);
//             // console.log(el);
//             if (e.target === el) {
//                 subElements.classList.toggle("itedm-burger");
//                 e.stopPropagation();
//                 verif = true;
//             }
//         });
//     }
//     document.addEventListener('click', (a) => {
//         // console.log(a.target);
//         if (!subElements.contains(a.target)) {      //la methode contains renvois true si subelement est parent "direct" de "e.target"
//             if (verif) {
//                 subElements.classList.add("item-burger");
//                 verif = false;
//             }
//         }
//     });
// })();//fin pour les tiret-burgur
// // fin pour le menu deroulant



// // dropdown menu for signin
// (function () {
//     let verif = false; //ici sous-items sont caché
//     const element = document.querySelector('.signin');
//     const subElements = document.querySelector('.item-signin-visible');

//     element.addEventListener('click', (e) => {
//         if (e.target === element) {
//             subElements.classList.toggle("item-signin-hidden");
//             e.stopPropagation();
//             verif = true; //pour dire que les sous-items sont visible
//         }
//     });
//     document.addEventListener('click', (a) => {
//         console.log(a.target);
//         if (!subElements.contains(a.target)) {      //la methode contains renvois true si subelement est parent "direct" de "e.target"
//             if (verif) {
//                 subElements.classList.add("item-signin-hidden");
//                 verif = false;
//             }
//         }
//     });
// })();//fin menu deroulant

// // pour les sub-item sign du button burger
// (function () {
//     let verif = false; //ici sous-items sont caché
//     const element = document.querySelector('.item-mobile');
//     const subElements = document.querySelector('.item-signin-mobile-visible');

//     element.addEventListener('click', (e) => {
//         if (e.target === element) {
//             subElements.classList.toggle("item-signin-mobile-hidden");
//             e.stopPropagation();
//             verif = true; //pour dire que les sous-items sont visible
//         }
//     });

//     document.addEventListener('click', (a) => {
//         console.log(a.target);
//         if (!subElements.contains(a.target)) {      //la methode contains renvois true si subelement est parent "direct" de "e.target"
//             if (verif) {
//                 subElements.classList.add("item-signin-mobile-hidden");
//                 verif = false;
//             }
//         }
//     });

    
// })();//fin menu deroulant
























(function () {
    let verif = false;
    const element = document.querySelector('.item-mobile');
    const subElements = document.querySelector('.item-signin-mobile-visible');

    function handleClick(e) {
        if (e.target === element) {
            subElements.classList.toggle("item-signin-mobile-hidden");
            e.stopPropagation();
            verif = true;
        }
    }

    function handleDocumentClick(a) {
        if (!subElements.contains(a.target)) {
            if (verif) {
                subElements.classList.add("item-signin-mobile-hidden");
                verif = false;
            }
        }
    }

    // Fonction pour exécuter votre code si la largeur est inférieure à 667px
    function executeOnSmallScreen() {
        if (window.innerWidth < 667) {
            element.addEventListener('click', handleClick);
            document.addEventListener('click', handleDocumentClick);
        } else {
            element.removeEventListener('click', handleClick);
            document.removeEventListener('click', handleDocumentClick);
        }
    }

    // Appeler la fonction de vérification initiale au chargement de la page
    executeOnSmallScreen();

    // Attacher l'événement de redimensionnement de la fenêtre pour vérifier lorsque la taille de la fenêtre change
    window.addEventListener('resize', executeOnSmallScreen);
})();

