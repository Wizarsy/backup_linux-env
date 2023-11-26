import random as rd
import time

start_time = time.time()
brute=''
key=[]

def randomP(v):
  passw=''
  for i in range(v):
    pos=rd.randint(2,100000)
    if pos % 2 != 0:
      num=rd.randint(0,9)
      passw+= str(num)
    else:
      pos=rd.randint(1,10000)
      if pos % 2 != 0:
        lupp=rd.randint(65,90)
        passw+= chr(lupp)
      else:
        llow=rd.randint(97,122)
        passw+= chr(llow)
  return passw

passw=randomP(6)

while brute != passw:
  key.append('')
  for x1 in range(48,123):
    if brute == passw:
      break
    key[0]=chr(x1)
    brute=''.join(key)
    if len(key)>1:
      for x2 in range(48,123):
        if brute == passw:
          break
        key[1]=chr(x2)
        brute=''.join(key)
        if len(key)>2:
          for x3 in range(48,123):
            if brute == passw:
              break
            key[2]= chr(x3)
            brute=''.join(key)
            if len(key)>3:
              for x4 in range(48,123):
                if brute == passw:
                  break
                key[3]= chr(x4)
                brute=''.join(key)
                if len(key)>4:
                  for x5 in range(48,123):
                    if brute == passw:
                      break
                    key[4]= chr(x5)
                    brute=''.join(key)
                    if len(key)>5:
                      for x6 in range(48,123):
                        if brute == passw:
                          break
                        key[5]= chr(x6)
                        brute=''.join(key)
print(f'{passw} == {brute}')
print("%s seconds" % (time.time() - start_time))