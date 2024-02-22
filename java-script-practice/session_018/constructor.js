var ali = {name: 'Ali', lastname: 'Ahmadi', age: 25};

function preson(name, lastname, age){
    this.name = name;
    this.lastname = lastname;
    this.age = age;

    this.fulname = function(){
        return this.name + ' ' + this.lastname;
    }
}

var amir = new preson('Amir', 'Mehrabani', '20');
console.log(amir);
console.log(amir.fulname());

var people = [];
people.push(new preson('Amir', 'Mehrabani', '20'));
people.push(new preson('Ali', 'Mohammadi', '25'));
people.push(new preson('Mina', 'Ahmadi', '18'));
people.push(new preson('gholam', 'Mehrabani', '30'));

var text = '';
for(i in people){
    text += people[i].name + ' '; 
    text += people[i].lastname + ' ';
    text += ' ---> ' + people[i].age + '<br/>';
}

document.getElementById('demo').innerHTML = text;