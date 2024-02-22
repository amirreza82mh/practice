switch(new Date().getDay()){
    case 0: {
        alert('today is sunday');
        break;
    }
    case 1: {
        alert('today is monday');
        break;
    }
    case 2: {
        alert('today is tuesday');
        break;
    }
    case 3: {
        alert('today is wednesday');
        break;
    }
    case 4: {
        alert('today is thursday');
        break;
    }
    case 5: {
        alert('today is friday');
        break;
    }
    case 6: {
        alert('today is saturday');
        break;
    }

    default: {
        alert('invalid');
        break;
    }
}

var Name = 'Amir';

switch(Name){
    case 'ali':{
        alert('hello ali');
        break;
    }

    case 'Amir':{
        alert('hello amir');
    }
    case 'taha': {
        alert('hello taha');
    }
}