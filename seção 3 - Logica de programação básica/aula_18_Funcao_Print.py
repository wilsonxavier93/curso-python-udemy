# FUNÇÃO PRINT:

print(12, 34) #argumentos não nomeados. a virgula é usada para dar separar os valores, mostrando um espaço entre os nummeros.
print(56, 78, sep="-") #sep="" é um argumento nomeado, neste caso sep é um separador, mas os arqumentos serão com o que estiver dentro das aspas.
print(910, 1112, sep='#') #exemplo do sep que separou os valores com a #


# QUEBRA DE LINHAS
print("Olá", end='\n') #end é um argumento nomeado, que faz a quebra da linha.
# \r\n -> CRFL
#  \n -> LF
print("Mundo")

print("Python") #aqui não é necessário o end='\n' pois a função print já quebra a linha por padrão.
