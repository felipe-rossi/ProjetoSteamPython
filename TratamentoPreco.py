import time


def tratarPrecoSkin(precoString):
     
    precoTratado = precoString.replace(" ","") 
    
    precoTratado = precoTratado.replace(".","") 
    
    precoTratado = precoTratado.replace("$","")
    
    precoTratado = precoTratado.replace("USD","")

    precoTratado = int(precoTratado)
    
    return precoTratado