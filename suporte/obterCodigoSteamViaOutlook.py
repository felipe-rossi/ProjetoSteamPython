import win32com.client
import re
import gc
import time

class CodigoSteam:
  
    def obterCodigoViaEmail():
        time.sleep(60)

        # Conectando no aplicativo do Outlook Via COM(Component Object Model)(Lembrando que tem que estar aberto)
        outlook = win32com.client.Dispatch("Outlook.Application") 
            
        # Acessa o namespace MAPI(Messaging Application Programming Interface), que é a interface padrão do Outlook para manipular mensagens(como Caixa de Entrada, Itens Enviados, etc.)
        namespace = outlook.GetNamespace("MAPI") 
            
        # Retorna a caixa de entrada do cliente
        inbox = namespace.GetDefaultFolder(6)
            
        # Filtrando por emails não lidos
        emails_recebidos = inbox.Items.Restrict("[UnRead] = True") 
            
        # Ordena por data de recebimento dos emails
        emails_recebidos.Sort("[ReceivedTime]", True) 
          

        if emails_recebidos.Count > 0:
            # Captura o primeiro e-mail da lista baseado nas configurações que setamos ali em cima
            ultimo_email_nao_lido = emails_recebidos.GetFirst() 

            # Padrão para capturar o código enviado via email
            pattern = r'Brazil\s*([A-Za-z0-9]{5})' 
    
            # Procurar o código no corpo da mensagem, re.search vai procurar o pad~rao definido no corpo do último email recebido, re.DOTALL garente que ele vá procurar no corpo todo do email
            match = re.search(pattern, ultimo_email_nao_lido.Body, re.DOTALL)
                
            # Verificar se o código foi encontrado
            if match:
                    
                # Captura o conteúdo do primeiro grupo da expressão regular, que no caso é o código de verificação alfanumérico com 5 caracteres. O número 1 se refere ao grupo capturado entre parênteses na expressão regular ([A-Za-z0-9]{5}).
                verification_code = match.group(1) 

                listaCodigo = list(verification_code)

                #preenhcerCodigo = True
                print(f"Código encontrado: {verification_code}")

                # Marcar o e-mail como lido
                ultimo_email_nao_lido.UnRead = False
                ultimo_email_nao_lido.Save()  # Salvar a alteração
                ultimo_email_nao_lido.Delete()
                
                return listaCodigo     
            else:
                print("Código não encontrado no corpo da mensagem.")
        else:
            time.sleep(120) # 
            print("Nenhum email não lido encontrado.")
            return ""

        # Encerrando a sessão com o Outlook
        del outlook
        del namespace
        del inbox
        gc.collect()