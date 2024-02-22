var lbl = document.getElementById('lblResult');

function add(){
    var num1 = document.getElementById("number1").value;
    var num2 = document.getElementById("number2").value;
    
    num1 = parseInt(num1);
    num2 = parseInt(num2);
    
    sum = num1 + num2;

    lbl.innerHTML = sum;
}

function zarb(){
    var num1 = document.getElementById("number1").value;
    var num2 = document.getElementById("number2").value;
    z = parseInt(num1) * parseInt(num2);
    lbl.innerHTML = z;
}

function taghsim(){
    var num1 = document.getElementById("number1").value;
    var num2 = document.getElementById("number2").value;

    lbl.innerHTML = parseInt(num1) / parseInt(num2);
}

function menha(){
    var num1 = document.getElementById("number1").value;
    var num2 = document.getElementById("number2").value;

    lbl.innerHTML = parseInt(num1) - parseInt(num2);
}

console.log(Boolean(1))
