.code
  testaA:
    lda a
    not
    add #01h
    add b
    jn aMaior

  bMaior:
    lda b
    sta maior
    lda a
    sta menor
    jmp testaC

  aMaior:
    lda a
    sta maior
    lda b
    sta menor

  testaC:
    lda c
    not
    add #01h
    add maior
    jn CmaiorMaior

  CmenorMaior:
    lda menor
    not
    add #01h
    add c
    jn CmenorMenor

  CmaiorMenor:
    lda c
    sta meio
    jmp testeMaior

  CmenorMenor:
    lda menor
    sta meio
    lda c
    sta menor
    jmp testeMaior

  CmaiorMaior:
    lda maior
    sta meio
    lda c
    sta maior

  testeMaior:
    lda maior
    not
    add #01h
    add menor
    add meio
    jn break

  testeMenor:
    lda meio
    not
    add #01h
    add maior
    not
    add #01h
    add menor
    jn break

  true:
    lda #01h
    sta res

  break:
    hlt

.endcode

.data
  a: db #0ah
  b: db #06h
  c: db #08h
  res: db #00h
  maior: db #00h
  menor: db #00h
  meio: db #00h
.enddata
