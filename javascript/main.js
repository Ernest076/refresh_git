function message() {
    alert("Hello, World!");
}
var fnumber,snumber
function add(fnumber, snumber) {
    sum = fnumber + snumber;
    return sum;
}

function changeText() {
    var button = document.getElementById("myButton");
    var span = document.getElementById("mySpan");
    button.innerHTML = "Clicked!";
    span.innerHTML = "Button was clicked!";
}
