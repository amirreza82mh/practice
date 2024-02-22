const url = "https://www.google.com";
document.write(url);
document.write('<br />');

try{
url = 'ali';
console.log(url);
}
catch(err){
    document.write(err.message);
    document.write('<br />');   
}

var x = 20;
{
    const x = 3;
    document.write(x);
    document.write('<br />');
}

document.write(x);
document.write('<br />');

const person = {
    firstname: 'Amir',
    lastname: 'mehrabani',
    age: 20
};

console.log(person);
person.phone = '09024649494';
person.address = 'neyshabour';
console.log(person);

person.age = 2;
console.log(person);

// person = {                 ERROR
//     firstname: 'dasfa';
// }

const names = ['Amir', 'Ali', 'gholam'];
console.log(names);
names.push('hasan');
console.log(names);