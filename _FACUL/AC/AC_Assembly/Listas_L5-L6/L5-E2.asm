.code
  lda n1
  not
  add #01h
  add n2
  jn maximo
  minimo:
    lda n1
    sta min
    lda n2
    sta max
    jmp break
  maximo:
    lda n1
    sta max
    lda n2
    sta min
    jmp break
  break:
    hlt
.endcode



.data
  n1: db #03h
  n2: db #01h
  max: db #00h
  min: db #00h
.enddata
