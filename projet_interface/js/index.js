


// xhr = new XMLHttpRequest()
// xhr.open("get", "#")
// xhr.onreadystatechange = () => {
//     if (xhr.readyState === 4 && xhr.status === 200) {
//         const rep = JSON.parse(xhr.responseText);
//     }
// }
// xhr.send()


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
(function () {
    let verif = false;
    const element = document.querySelector('.div-burger');
    const subElements = document.querySelector('.visible');

    element.addEventListener('click', (e) => {
        if (e.target === element) {
            subElements.classList.toggle("item-burger");
            e.stopPropagation();
            verif = true;
        }
    });
    document.addEventListener('click', (a) => {
        // console.log(a.target);
        if (!subElements.contains(a.target)) {      //la methode contains renvois true si subelement est parent "direct" de "e.target"
            if (verif) {
                subElements.classList.add("item-burger");
                verif = false;
            }
        }
    });
})();//fin menu deroulant

// pour les tiret-burgur
(function () {
    let verif = false;
    const element = document.querySelectorAll('.tiret-burger');
    const subElements = document.querySelector('.visible');
    // parce que c'est un array, on doit le parcourir et exploiter chacun de son item
    for (const el of element) {
        // console.log(el);
        el.addEventListener('click', (e) => {
            // console.log(e.target);
            // console.log(el);
            if (e.target === el) {
                subElements.classList.toggle("item-burger");
                e.stopPropagation();
                verif = true;
            }
        });
    }
    document.addEventListener('click', (a) => {
        // console.log(a.target);
        if (!subElements.contains(a.target)) {      //la methode contains renvois true si subelement est parent "direct" de "e.target"
            if (verif) {
                subElements.classList.add("item-burger");
                verif = false;
            }
        }
    });
})();//fin pour les tiret-burgur
// fin pour le menu deroulant





























