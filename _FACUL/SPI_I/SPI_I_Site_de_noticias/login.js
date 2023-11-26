let usuario = document.querySelector('#usuario')
let labelusuario = document.querySelector('#labelusuario')
let valideusuario = false

let senha = document.querySelector('#senha')
let labelsenha = document.querySelector('#labelsenha')
let validesenha = false

let msgErro = document.querySelector('#msgErro')
let msgSucesso = document.querySelector('#msgSucesso')

usuario.addEventListener('keyup', () =>{
  if(usuario.value.length <= 5){
    labelusuario.setAttribute('style', 'color:red')
    labelusuario.innerHTML = 'Usuário *Insira no mínimo 6 caracteres'
    usuario.setAttribute('style', 'color:red')
    valideusuario = false
  }
  else{
    labelusuario.setAttribute('style', 'color:green')
    labelusuario.innerHTML = 'Usuário'
    usuario.setAttribute('style', 'color:green')
    valideusuario = true
  }
})
senha.addEventListener('keyup', () =>{
  if(senha.value.length <= 7){
    labelsenha.setAttribute('style', 'color:red')
    labelsenha.innerHTML = 'Senha *Insira no mínimo 8 caracteres'
    senha.setAttribute('style', 'color:red')
    validesenha = false
  }
  else{
    labelsenha.setAttribute('style', 'color:green')
    labelsenha.innerHTML = 'Senha'
    senha.setAttribute('style', 'color:green')
    validesenha = true
  }
})

function cadastrar(){
  if(valideusuario && validesenha){
    let listausuario = JSON.parse(localStorage.getItem('listausuario') || '[]')

    msgSucesso.setAttribute('style', 'display: block')
    msgSucesso.innerHTML = '<strong>Cadastrando Usuário...</strong>'
    msgErro.setAttribute('style', 'display: none')
    msgErro.innerHTML = ''

    listausuario.push(
    {
      cadastrousuario: usuario.value,
      cadastrosenha: senha.value
    }
    )
    localStorage.setItem('listausuario', JSON.stringify(listausuario))

    setTimeout(() =>{
      window.location.href = 'login.html'
    }, 3000)

  }
  else{
    msgErro.setAttribute('style', 'display: block')
    msgErro.innerHTML = '<strong>Preencha todos os dados corretamente!</strong>'
    msgSucesso.setAttribute('style', 'display: none')
    msgSucesso.innerHTML = ''
  }
}

function entrar(){
  let usuario = document.querySelector('#usuario')
  let labelusuario = document.querySelector('#labelusuario')

  let senha = document.querySelector('#senha')
  let labelsenha = document.querySelector('#labelsenha')

  let listausuario = []

  let uservalid = {
    usuario: '',
    senha: ''
  }

  listausuario = JSON.parse(localStorage.getItem('listausuario'))

  listausuario.forEach((item) => {
    if(usuario.value == item.cadastrousuario && senha.value == item.cadastrosenha){
      uservalid = {
        usuario: item.cadastrousuario,
        senha: item.cadastrosenha
      }
       }
  })
  if(usuario.value == uservalid.usuario && senha.value == uservalid.senha){
    window.location.href = 'index.html'
  }else{
    labelusuario.setAttribute('style', 'color:red')
    usuario.setAttribute('style', 'color:red')
    labelsenha.setAttribute('style', 'color:red')
    senha.setAttribute('style', 'color:red')
    msgErro.setAttribute('style', 'display: block')
    msgErro.innerHTML = 'Usuário e/ou senha incorretos!'
  }
}