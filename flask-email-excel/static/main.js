function myFunction(id) {
    idi= 'id:'+id
    email= document.getElementById('email'+id).value
    temat=document.getElementById('temat'+id).value
    tresc= document.getElementById('tresc'+id).value
    var forms = document.getElementById("form_send");
    document.getElementById("email").value = email;
    document.getElementById("tytul").value = temat;
    document.getElementById("message").value = tresc
    forms.action = "/wyslij/"+id;
    openForm()

}
function openForm() {
  
  var x = document.getElementById("hide");
  var y = document.getElementById("hide_send");
  var c = document.getElementById("wszystko_btn");

  if (x.style.display === "none") {
    
    x.style.display = "block";
  } else {
    x.style.display = "none";
    y.style.display = "block"
    c.style.display = "none"
  }
}


  

  