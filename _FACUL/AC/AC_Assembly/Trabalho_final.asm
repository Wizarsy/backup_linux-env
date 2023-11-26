.code
MMENOR: lda M
        jz BREAK
        not
        add #01h
        add N
        jn NMENOR

        lda M
        not
        add #01h
MLOOP:  jz BREAK
        sta M
        lda RES
        add N
        sta RES
        lda M
        add #01h
        jmp MLOOP

NMENOR: lda N
        not
        add #01h
NLOOP:  jz BREAK
        sta N
        lda RES
        add M
        sta RES
        lda N
        add #01h
        jmp NLOOP

BREAK:  hlt
.endcode



.data
M:      db #03h
N:      db #1Ah
RES:    db #00h
.enddata
