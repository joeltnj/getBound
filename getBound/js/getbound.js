

/**
 * la fonction make est la fonction auto appeler(on paouarait faire aussi autrement)
 */

function make() {
    let v1 = document.querySelector(".barre");
    v1.addEventListener("click", make);
    /**les instruction que je vais donner à ma fonction */

    let verif = false;
    function make(b) {
        document.querySelector(".asideOne").classList.add("asideCreate");
        verif = true;
        //document.querySelector(".un").classList.remove(".asideCreate");
        b.stopPropagation(); //stop la propagation qui aurait la 2 fonction (desous), ainsi cela annulerait(suprimerait) les "class"  ajouter
        //b.preventDefault();
    }

    document.querySelector("body").addEventListener("click", function () {
        if (verif) {
            document.querySelector(".asideOne").classList.remove("asideCreate");
        }
    })



}

make();