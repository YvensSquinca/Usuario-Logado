from subprocess import check_output
import re

output = check_output(r"pstools\psloggedon.exe  -l -x \\IPdamaquina") #Com base no PSEXEC pega informações de Logon na maquina Indicada.

#O comando de saida retorna uma lista, e precisa ser filtrada com base no indice.

logado = str(output.splitlines()[7]) #Posição que confirma se tem usuario logado.
usuario = str(output.splitlines()[8]) #Posição que confirma qual usuario logado.

#A saida do usuario é muito poluida, usamos o comando replace para limpar as sujeiras.

usuario1 = usuario.replace("b'","")
usuario2 = usuario1.replace(" ","")
usuario3 = usuario2.replace("tALMAVIVA","")
usuario4 = usuario3.replace("\\","")
usuariof = usuario4.replace("'","")

print (usuariof) #Variavel com o usuario que esta logado. Saida limpa pelos comandos replace.

if re.search('one', logado, re.IGNORECASE): #Baseado na variavel LOGADO, confirma se tem ou não usuario logado.
    print("Não tem logado")
else:
    print("Tem logado")
