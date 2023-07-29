#BIBLIOTECAS
import sqlite3
#CREAT
#CRIANDO E ACESSANDO O BANCO
banco=sqlite3.connect('bdgeo.sqbpro')
cursor=banco.cursor()
#CRIANDO TABELA
cursor.execute("CREATE TABLE projeto(local,cidade,lati,longi,bairro,ocorrido,status,dia)")

#ADMINISTRANDO 
print('escolha uma ação para ser executada no seu banco de dados.')
acao=input("adicionar(add),ver(see),autualizar(up) ou deletar(del):")

#FORMULARIO
if acao == 'add':
    print('preencha o formulário!')        
    print()
    def formulario(acao):
        return
    local=input('insira o nome do lugar:')
    cidade=input('digite o nome de seu municipio:')
    lati=input('digite a latitude do ponto:')
    longi=input('digite a longitude do ponto:')
    bairro=input('digite o nome do bairro:')
    ocorrido=input('relate o corrido:')
    atual=input('digite o status entre ativo e não ativo:')
    dia=input('Qual a data desse registro?formato dia-mês-ano:')
    cursor.execute("INSERT INTO projeto VALUES('"+local+"','"+cidade+"','"+lati+"','"+longi+"','"+bairro+"','"+ocorrido+"','"+atual+"','"+dia+"');")
    banco.commit()#Adicionando dados
    print('dados adicionados ao banco de dados!')

#READ
elif acao == 'see':
    print("veja seu banco de dados:")
    leitura=f'SELECT * FROM projeto'
    cursor.execute(leitura)
    ver=cursor.fetchall()
    print(ver)

#UPDATE
elif acao == 'up':
        print("atualização do status!")
        atual=input('qual o status:')
        area=input('qual a cidade:')
        cursor.execute(f"UPDATE projeto SET status='{atual}' WHERE cidade='{area}'")
        banco.commit()
        print("atulização concluída com sucesso!")

#DELETE
elif acao == 'del':
    print("escolha os parametros para deletar!")
    linha=input('qual linha vai deletar:')
    cursor.execute(f"DELETE FROM projeto WHERE local='{linha}'")
    banco.commit()
    print("valor deletado com sucesso!")
    print()
else:
    print('tente novamente')


            
            

        



        
        
        