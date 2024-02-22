function myFunc(){
    alert('hi my name is amirreza');
}

var fullname = function(a, b){
    return a + ' ' + b;
}

console.log(fullname('amir', 'mehrabani'));

var my = new Function("a", "b", "return a*b");
console.log(my(3,4));

(function(){
    document.getElementById('demo').innerHTML = 'always';
})();

// function num(a, b) => a = b; 

var num = (a, b) => a + b;
console.log(num(12, 3));

var sum2 = (a, b) => {
    return a * b;
}

console.log(sum2(10, 20));