.code
  lda a
  main:
    not
    add #01h
    add b
    jz break
    lda a
    add #01h
    sta a
    jmp main
  break:
    hlt
.endcode

.data
  a: DB #00h
  b: db #05h
.enddata
