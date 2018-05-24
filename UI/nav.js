window.onscroll = function() {navFucntion()}

let navbar = document.getElementById("navbar");

let sticky = navbar.offsetTop;

function navFunction(){
    if (window.pageYOffset >= sticky){
        navbar.classList.add("sticky")
    }else{
        navbar.classList.remove("sticky");
    }
}
