%include "io.inc"
section .data
F DD 300

section .text
global CMAIN
CMAIN:
    MOV EAX, [F]
    MOV ECX, 9
    MOV EDX, 0
    SUB EAX, 32
    IMUL EAX, 5
    IDIV ECX
    PRINT_UDEC 4, EAX
    RET
