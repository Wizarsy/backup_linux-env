html = open('_FACUL/AED_I/AED_I_-_3_Bi_prova/2/teste.html','r')
read_html = html.readlines()
html.close()
init = 0
fim = 0
print(read_html)
for elem in read_html:
    for char in elem:
        if char == '>':
            init = elem.index(char)
        if char == '/' or char == ' ':
            fim = elem.index(char)
    print(elem[init + 1:fim - 1])