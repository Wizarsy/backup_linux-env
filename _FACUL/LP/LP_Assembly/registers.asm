%include "io.inc"
SECTION .text
GLOBAL CMAIN
CMAIN:
    MOV EAX, 30
    ADD EAX, 70
    SUB EAX, 99
    PRINT_UDEC 4, EAX
    RET