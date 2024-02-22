function myFunction(){
    var x, text;

    x = document.getElementById('num').value;

    if(isNaN(x) || x > 10 || x < 1){
        text = 'input is not vaild';
        document.getElementById('show').innerHTML = text;
        document.getElementById('show').style.color="red";
    }
    else{
        text = 'input is valid';
        document.getElementById('show').innerHTML = text;
        document.getElementById('show').style.color="green";
    }
}