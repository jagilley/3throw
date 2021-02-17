$(window).on('keypress', function(e) {
    var key = e.key;
    // $.ajax({
    //     data :{
    //         keyboard : key
    //     },
    //     type : 'POST',
    //     url: '/postmethod'
    // }

    // );
    if(key == "k"){
        var pBar = document.getElementById("progressBar");
        var val = parseInt(pBar.style.width);
        if(val < 100){
            pBar.style.width = (val + 1).toString() + '%';
        }
        
    }
    if(key == "a" || key == "s" || key == "d" || key == "w" || key == "k"){
        $.post("/postmethod", {
            keyboard : key
        });
    }
});

$(document).on('keyup', function(e) {
    if(e.key == "k"){
        document.getElementById("progressBar").style.width = "0%";
        $.post("/postmethod", {
            keyboard : "r"
        });
    }
});