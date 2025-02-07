
def tratarPrecoSkinReal(precoString):
     
    precoTratado = precoString.replace(" ","") 
    
    precoTratado = precoTratado.replace(",","") 
    
    precoTratado = precoTratado.replace("R$","")

    precoTratado = int(precoTratado)
    
    return precoTratado

def tratarPrecoSkinDollar(precoString):
     
    precoTratado = precoString.replace(" ","") 
    
    precoTratado = precoTratado.replace(".","") 

    precoTratado = precoTratado.replace("$","")

    precoTratado = precoTratado.replace("USD","")

    precoTratado = int(precoTratado)
    
    return precoTratado