.code
  main:
    lda m
    not
    add #01h
    add n
    jz true
    jn false
    sta n
    jmp main
  true:
    lda #01h
    sta res
    hlt
  false:
    hlt
.endcode

.data
  n: db #0ch
  m: db #04h
  res: db #00h
.enddata
