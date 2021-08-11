from io import TextIOWrapper

import string

def lexico(palavra):
    
    reservada = ['if', 'else', 'def', 'print', 'for', 'while', 'int']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    if (''.join(palavra) in reservada):
        
        return print(''.join(palavra) + ' = palavra reservada \n')
    
    elif(''.join(palavra[0]) in numeros):
        
        return print(''.join(palavra) + ' = número \n')
    
    else:
        
        return print(''.join(palavra) + ' = texto \n')
    
    
def compara(tipo):
    
    reservada = ['int ', 'float ', 'char ']
    simbolos = [',', ' ']
    a = list(string.ascii_lowercase)
    
    if(''.join(tipo) in reservada):
        
        return True
    
    elif(''.join(tipo) in a):
        
        return True
    
    elif(''.join(tipo) in simbolos):
        
        return True
    
    else:
        
        return False
    
    
def sintatico(palavra):
    
    aux = list()
    aux2 = list()
    
    final = len(palavra)
    cont = 0
    flag = True
    
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    bloqueado = ['.', '!', '%', '*', '+', '-', '/', '<', '>', '(', ')']
    bloqueado_ini = ['.', '!', '%', '*', '+', '-', '/', '<', '>', ')', '=', ' ']
    reservada = ['int', 'float', 'char']
    
    if(palavra[0] == 'd' and palavra[1] == 'e' and palavra[2] == 'f' and palavra[3] == ' ' and palavra[final-1] == ')'):
        
        palavra.pop(0)
        palavra.pop(0)
        palavra.pop(0)
        palavra.pop(0)
        
        if(palavra[0] in numeros):
            
            flag = False
            print('Sintaxe incorreta!')
            return flag
            
        else:
        
            for item in palavra:
                
                if(item == '('):
                    
                    cont += 1
                    break
                
                elif(item == ')' or item in bloqueado_ini):
                    
                    flag = False
                    print('Sintaxe incorreta!')
                    return flag
                    
                else:
                                        
                    cont += 1
                
            for item in range(len(palavra[cont:final])):
                
                if (palavra[cont] != ')'):
                    
                    if(palavra[cont] not in bloqueado):
                        
                        cont += 1
                        
                    else:
                        
                        flag = False
                        print('Sintaxe incorreta!')
                        return flag
                    
                else:
                    
                    break
                
                
    if(palavra[0] == 'i' or palavra[0] == 'f' or palavra[0] == 'c'):
        
        for valor in range(len(palavra)):
            
            if(palavra[valor] == ' '):
                
                cont += 1
                break
            
            else:
                
                cont += 1
                
                aux.append(palavra[valor])
                
       
        if(''.join(aux) not in reservada):
            
            flag = False
            print('Sintaxe incorreta!')
            return flag
            
        for valor in range(cont):
            
            palavra.pop(0)
        
        
        if(palavra[0] in numeros):
            
            flag = False
            print('Sintaxe incorreta!')
            return flag
            
        else:
            
            cont = 0
            
            for item in palavra:
                
                if(item == '('):
                    
                    cont += 1
                    break
                
                elif(item == ')' or item in bloqueado_ini):
                    
                    flag = False
                    print('Sintaxe incorreta!')
                    return flag
            
                else:
                    
                    cont += 1
            
            # print(palavra)
            
            for item in range(len(palavra[cont:final])):
                
                if (palavra[cont] != ')'):
                           
                    if(palavra[cont] == ' '):
                        
                        aux2.append(palavra[cont])
                        validado = compara(aux2)
                        aux2.clear()
                        
                        if(validado == False):
                            
                            flag = False
                            print('Sintaxe incorreta!')
                            return flag
                    
                    elif(palavra[cont] == ","):
                        
                        validado = compara(aux2)
                        aux2.clear()
                        
                        print(validado)
                        
                        if(validado == False):
                            
                            flag = False
                            print('Sintaxe incorreta!')
                            return flag
                        
                    else:
                        
                        aux2.append(palavra[cont])
                        
                    if(palavra[cont] not in bloqueado):
                        
                        cont += 1          
                        
                    else:
                        
                        flag = False
                        print('Sintaxe incorreta!')
                        return flag
                    
                elif(palavra[cont] == ')'):
                    
                    validado = compara(aux2)
                    aux2.clear()
                        
                    if(validado == False):
                        
                        flag = False
                        print('Sintaxe incorreta!')
                        return flag
                    
                
    return flag
                

texto = open('arquivo.txt', 'r')

lista = texto.readlines()

aux = list()
lista_simb = list()
lista_palavra = list()
clone = list()

simbolos = ['.', ',', '=', '!', '(', ')', '%', '*', '+', '-', '/', '<', '>', ' ']
   

for linha in lista:
    
    for item in linha:
    
        aux.append(item)

for linha in lista:
    
    for item in linha:
    
        clone.append(item)

validado = sintatico(clone)
        
if(validado == True):
    
    for palavra in aux:
        
        if(palavra in simbolos):
            
            if(len(lista_palavra) != 0):
                
                lexico(lista_palavra)
            
                lista_palavra.clear()
                
            
            print(''.join(palavra) + ' = simbolo \n')
            
        else:
            
            lista_palavra.append(palavra)
            
else:
    pass

    
texto.close()