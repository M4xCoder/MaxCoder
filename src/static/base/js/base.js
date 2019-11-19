/* Scroll button*/
window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}

let timeOut;

function topFunction() {
    let top = Math.max(document.body.scrollTop, document.documentElement.scrollTop);
    if (top > 0) {
        window.scrollBy(0, -100);
        timeOut = setTimeout('topFunction()', 20);
    } else clearTimeout(timeOut);
}

btnMenu.onclick = function responsiv_menu() {
    let x = document.getElementById("myMenu");
    let y = document.getElementById("btnMenuImg");

    if( x.className === "myMenu") {
        x.className += "_responsiv";
        y.className = "fa  fa-angle-double-up";
    }
    else {
        x.className = "myMenu";
        y.className = "fa  fa-angle-double-down";
    }
}