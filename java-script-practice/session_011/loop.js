var names = ['iman', 'amir', 'reza', 'gholam'];
var text = String();
for(var i = 0 ; i < names.length ; i++){
    text += names[i] + "<br !>";
}

document.getElementById('result').innerHTML = text;

text = '';
for(i in names){
    text += names[i] + '<br>';
}

document.getElementById('result2').innerHTML = text;

for(var i = 0 ; i < 3 ; i++){
    alert(i);
}