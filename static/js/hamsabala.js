function toggleMenu(){
    document.getElementById("menu").classList.toggle("active");
    document.getElementById("mobile-menu-button").classList.toggle("active");
}

function getInsta(){
    var data = {};
    $.ajax({
        url:"https://www.instagram.com/hamsabala.pro/media/",
        jsonp: "callback",
        dataType: "json",
        data: data,
        success: function(response){
            console.log(responce["items"]);
            }
    });

}

