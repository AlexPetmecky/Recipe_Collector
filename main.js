document.addEventListener('DOMContentLoaded', function () {
    //document.querySelectorAll('.gen_form')[0].addEventListener('click', checkoutForm);
    document.getElementById('submit-button').addEventListener('click', checkoutForm);

});


function checkoutForm(){
    console.log("PRESSED");
    //xhttp.open("GET", "http://localhost:8888/recipe_callback/endpoint.php");
    chrome.tabs.query({
        active: true,
        lastFocusedWindow: true
    }, function(tabs) {
    // and use that tab to fill in out title and url
        var tab = tabs[0];
        //console.log(tab.url);
        //alert(tab.url);

        var http = new XMLHttpRequest();
        var url = 'http://localhost:8888/recipe_callback/endpoint.php';
        var params = 'activeTabId='+tab.url;
        http.open('POST', url, true);

        //Send the proper header information along with the request
        http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

        http.onreadystatechange = function() {//Call a function when the state changes.
            if(http.readyState == 4 && http.status == 200) {
                //alert(http.responseText);
                //console.log(http.responseText);
                chrome.downloads.download({
                    url: http.responseText,
                    //filename: "suggested/filename/with/relative.path" // Optional
                    });
            }
        }
        http.send(params);
    });

    






    //location.href ='http://localhost:8888/recipe_callback/endpoint.php';
    //console.out(data);
/*
    $.ajax({

    url : 'http://localhost/8888/recipe_callback/endpoint.php',
    type : 'GET',
    data : {
        'numberOfWords' : 10
    },
    dataType:'json',
    success : function(data) {
        console.log(data);
        alert('Data: '+data);
    },
    error : function(request,error)
    {
        alert("Request: "+JSON.stringify(request));
        console.log(JSON.stringify(request))
    }
});

*/
}