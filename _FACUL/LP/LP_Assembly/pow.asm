%include "io.inc"
section .data
X DD 5
N DD 3

section .text
global CMAIN
CMAIN:
    MOV EAX, 1
    MOV EBX, [X]
    MOV ECX, [N]
    vezes:
        IMUL EAX,EBX
    LOOP vezes
    PRINT_UDEC 4, EAX
    RET