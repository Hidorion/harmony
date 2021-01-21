$(document).ready(function(){
    if (document.getElementById("add-content") !== null) {
        let checked = document.getElementById("selected");
        if(checked.value = "Astuce"){         
            document.getElementById("tip").setAttribute("style","display:table")
            document.getElementById("pic").setAttribute("style","display:none");
        }
        else if(checked.value = "Image"){
            document.getElementById("tip").setAttribute("style","display:none")
            document.getElementById("pic").setAttribute("style","display:table");
        }
        else{ 
            document.getElementById("tip").setAttribute("style","display:none")
            document.getElementById("pic").setAttribute("style","display:none");
        }
    }
});