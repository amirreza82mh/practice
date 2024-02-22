var number1 = 20;
var number2 = 22;

if(number1 > number2){
    document.write('numer1 is bigger than number2');
}else{
    document.write('number1 is smaller than number2');
}

document.write("<br !>");

function conditional(){
    number3 = document.getElementById('time').value;
    if (number3 <= 10){
        document.getElementById('number').innerHTML = 'good morning';
    }else if(number3 <= 16){
        document.getElementById('number').innerHTML = 'good day';      
    }else if(number3 <= 20){
        document.getElementById('number').innerHTML = 'good evening';
    }else{
        document.getElementById('number').innerHTML = 'good night';
    }
}