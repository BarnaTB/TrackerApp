function opentable(evt, approve){
    var i, tabcontent, tablinks;
    // get all contents with "tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i=0; i < tabcontent.length; i++){
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    // remove class active from tablinks
    for (i=0; i < tablinks.length; i++){
        tablinks[i].className = tablinks[i].className.replace("active", "");
    }
    document.getElementById(approve).style.display = "block";
    evt.currentTarget.className += "active";
}