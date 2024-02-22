var names = ['iman', 'Amir', 'reza', 'gholam'];
var i = 0;

while(names[i]){
    document.write(names[i] + '<br />');
    i++;
}

document.write("<br />");

var i = 1;
do{
    document.write(i);
    i++;
}while(i > 20)

document.write('<br />');
document.write('<br />');

var i = 0;

while(true){
    
    if(i % 2 == 0){
        i++;
        continue;
    }

    if(i >= 30){
        break;
    }

    document.write(i + '   ');
    i++;
}