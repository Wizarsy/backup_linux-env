def teste(**kwargs):
  print(kwargs)
  x = kwargs["b"]
  print(x)
  
  
  
  
teste(a = [1], b = 'string')