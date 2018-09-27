// var SERVER_URL = "http://172.20.10.7:8888/"
var SERVER_URL = "http://192.168.201.35:8888/"


setInterval(getButton, 200)

function setLed(num, onoff) {
    callApi(
        SERVER_URL + "setLed",
        {
            "num": num,
            "onoff": onoff
        },
        function (o) {
        });
}

function getButton() {
    callApi(
        SERVER_URL + "getButton",
        {"dummy":"dummy"},
        function (o) {
            console.log(o.responseText);
            var retJson = eval('new Object(' + o.responseText + ')');
            document.getElementById("checkbox-button-0").checked = retJson.btn_0 == "1";
            document.getElementById("checkbox-button-1").checked = retJson.btn_1 == "1";
        });
}

function callApi(url, jsonObj, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('Accept', 'application/json');

    xhr.onreadystatechange = (function(myxhr) {
        return function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                callback(myxhr);
            }
        }
    })(xhr);

    xhr.send(JSON.stringify(jsonObj));
}




var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "My First dataset",
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [50, 10, 5, 2, 20, 30, 45],
        }]
    },

    // Configuration options go here
    options: {}
});
