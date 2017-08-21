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

function feedback(form){
    var data = form.serialize(),
        f = form[0];
    console.log(data);
    $.ajax({
        type:"POST",
        url:"/api/feedback/",
        data: data,
        success: function(response){
            var obj = response['responce'];
            f.reset();
            $(obj).show();
            function stop(){
                $(obj).hide();
                clearInterval(timer);
            }
            var timer = setTimeout(stop, 5000); 
        },
        error: function(jqXHR, exception){
            console.log(exception);
        },
    });
}
