function myFunction(){
    var x = document.forms["first-form"]["fname"].value;
    if(x==''){
        alert('field can not be empty');
        return false;
    }
}