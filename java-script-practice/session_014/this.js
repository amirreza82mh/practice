var firstname = 'ali';
var lastname = 'ghadam';

var person = {
    firstname: "Amirreza",
    lastname: "Mehrabani",
    Fullname: function() {
        return this.firstname + " " + this.lastname;      
    }
};

document.getElementById('result').innerHTML = person.Fullname();

// alert(this);  object window

// function myfunc(){
//     return this;
// }

// alert(myfunc());

function myfunc(){
    alert(this);
}

var x = 15;
{
    var x = 20;
}

document.getElementById('p01').innerHTML = x;


var y = 15;
{
    let y = 143;
    alert(y);
}

document.getElementById('p02').innerHTML = y;

var i = 5;
for (let i = 0; i < 3; i++) {
    alert(i);    
}

document.getElementById('p03').innerHTML = i;
