from graphics import *
import random as rd

win=GraphWin("Forca",700,400)
def word():
  doc=open(r'lib\forca_word.csv','r')
  dados=doc.read().split(';')
  doc.close()
  escolhida=rd.choice(dados).upper()
  posX=150
  posX1=160
  pontos=[]
  for letra in escolhida:
    line=Line(Point(posX,180),Point(posX1,180)).draw(win)
    pontos.append((posX+posX1)/2)
    posX=posX1+10
    posX1=posX+10
  return pontos, escolhida

def head():
  head=Circle(Point(100,101),10)
  return head.draw(win)
def body():
  body=Line(Point(100,110),Point(100,150))
  return body.draw(win)
def l_arm():
  l_arm=Line(Point(100,120),Point(70,130))
  return l_arm.draw(win)
def r_arm():
  r_arm=Line(Point(100,120),Point(130,130))
  return r_arm.draw(win)
def l_leg():
  l_leg=Line(Point(100,150),Point(70,170))
  return l_leg.draw(win)
def r_leg():
  r_leg=Line(Point(100,150),Point(130,170))
  return r_leg.draw(win)
def forca():
  Line(Point(50,70),Point(50,180)).draw(win)
  Line(Point(30,180),Point(70,180)).draw(win)
  Line(Point(50,70),Point(100,70)).draw(win)
  Line(Point(100,70),Point(100,90)).draw(win)
  Line(Point(90,90),Point(110,90)).draw(win)

def game():
  forca()
  tentativas=0
  acertos=0
  comboX=0
  usadas=[]
  erros=Text(Point(350,100),f'Erros: {tentativas}').draw(win)
  combo=Text(Point(450,100),f'Combo: {comboX}X').draw(win)
  combo.setStyle('bold')
  pontos,palavra=word()
  key=win.checkKey()
  while key != 'Escape':
    # resposta=input('Digite uma letra: ').upper()
    resposta=win.getKey().upper()
    if resposta in usadas:
      print(f'Letra {resposta} já foi usada!')
      continue
    for index in range(len(palavra)):
      if resposta == palavra[index]:
        Text(Point(pontos[index],173),palavra[index]).draw(win)
        acertos+=1
        comboX+=1
        combo.setText(f'Combo: {comboX}X')
    usadas.append(resposta)
    if acertos == len(palavra):
      Rectangle(Point(260,130),Point(440,270)).draw(win).setFill('green1')
      Text(Point(350,200),'WIN!').draw(win).setStyle('bold')
      win.getMouse()
      win.close()
    if resposta not in palavra:
      tentativas+=1
      comboX=0
      erros.setText(f'Erros: {tentativas}')
      combo.setText(f'Combo: {comboX}X')
    if tentativas == 1:
      head()
    if tentativas == 2:
      body()
    if tentativas == 3:
      l_arm()
    if tentativas == 4:
      r_arm()
    if tentativas == 5:
      l_leg()
    if tentativas == 6:
      r_leg()
      Rectangle(Point(260,130),Point(440,270)).draw(win).setFill('red1')
      Text(Point(350,200),'GAME OVER!').draw(win).setStyle('bold')
      win.getMouse()
      win.close()
  key=win.checkKey()
  win.getMouse()
  win.close()

game()