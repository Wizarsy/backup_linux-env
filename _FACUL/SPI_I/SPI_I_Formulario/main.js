 function validate (){
  let n = document.getElementById("nome").value;
  let e = document.getElementById("endereço").value;
  let c = document.getElementById("cep").value;
  let t = document.getElementById("telefone").value;
  let m = document.getElementById("e-mail").value;
  let va =/^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;

  if (n == ""){
    alert( "Por favor informe um nome" );
    return false;
  }

  if (e == ""){
    alert( "Por favor informe um endereço" );
    return false;
  }

  if (isNaN(c) || c == ""){
    alert( "Por favor informe um CEP válido" );
    return false;
  }

  if (isNaN(t) || t == "" || t.length < 10 || t.length > 11){
    alert( "Por favor informe um número de telefone válido" );
    return false;
  }

  if (!m.match(va) || m == ""){
    alert( "Por favor informe  um endereço de e-mail válido" );
    return false;
  }

  alert("Registrado e enviado com sucesso")

  return(true);
 }