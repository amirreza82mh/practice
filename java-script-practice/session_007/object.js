var person = {
    Name : 'Amirreaza',
    LastName : 'mehrabani',
    age : 20,
    fullname(){
        return this.Name + ' ' + this.LastName;
    }
};

document.getElementById('lblResult1').innerHTML = person.fullname()
document.getElementById('lblResult2').innerHTML = person.age