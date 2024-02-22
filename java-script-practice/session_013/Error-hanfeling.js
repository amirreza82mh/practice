// try{
//     add_func('Amirreza');
// }
// catch(err){
//     document.getElementById('result').innerHTML = err.message;
// }
// finally{
//     alert('finally');
// }

// throw 'haaaaaaaaaaaaah';

function my_function(){
    var message, input;
    message = document.getElementById("p01");
    input = document.getElementById("demo").value;

    try{
        if(input == '') throw 'empty';

        if(isNaN(input)) throw 'not a number';

        input = Number(input);

        if(input < 5)
            throw 'smaller than 5';
        else if(input > 10)
            throw 'bigger than 10';
        else
            throw 'fine';
    }
    catch(err){
        message.innerHTML = 'input is ' + err;
    }
    finally{
        document.getElementById("demo").value = ''
    }
}