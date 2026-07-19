function validate(){
    var 
    file= document.getElementId("resume").value;
    if (file==""){
        alert("upload resume");
        return false;
    
    }
    return true;
}
