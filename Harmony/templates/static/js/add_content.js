$(document).ready(function(){
    $('#selected').on('change', function() {
        $('#tip').toggle(false);
        $('#pic').toggle(false);
        if (this.value == "Astuce") {
            $('#tip').toggle(true)
        } else {
            $('#pic').toggle(true)
        }
    });
});