.code
  lda i
  main:
    not
    add #01h
    add n
    jz break
    lda x
    add i
    add i
    sta x
    lda i
    add #01h
    sta i
    jmp main

  break:
    hlt
.endcode


.data
  x: db #00h
  i: db #00h
  n: db #05h
.enddata
