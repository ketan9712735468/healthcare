//$(document).ready(function(){
function selectSearchType() {
    var x = document.getElementById("service_type").value;
//    var x = document.getElementsByClassName

    switch (x){
        case 'Doctor':{
            $('#tog').toggleClass('del');
            $('#mog').toggleClass('del');
// Disable #x
            $( "#tog" ).prop( "disabled", true );

// Enable #x
             $( "#mog" ).prop( "disabled", false );
            break;
        }
        case 'Serviciu':{
            $('#tog').toggleClass('del');
            $('#mog').toggleClass('del');
// Disable #x
            $( "#tog" ).prop( "disabled", false );

// Enable #x
             $( "#mog" ).prop( "disabled", true );
            break;
        }
    }
}
