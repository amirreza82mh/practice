var lbl = document.getElementById('lblResult');

function fullname(name1, name2){
    return name1 + ' ' + name2;    
}

function myAge(){
    return 10 + 10;
}

lbl.innerHTML = fullname('Amir', 'mehrabani');

var age = document.getElementById('result');
age.innerHTML = myAge()