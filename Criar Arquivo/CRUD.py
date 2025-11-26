import os 
os.system("cls || clear ")

#CRUD usando lista.
#Create = Criar/Salvar
#Read = buscar/Selecionar
#Update = Atualizar/Modificar
#Delete = Excluir

# Criando uma lista.
lista_clientes = []

print("CREATE - Adiconar / Inserir")
nome = "Marta"
lista_clientes.append(nome)
print(f"O nome: {nome} foi inserido com seucesso!")

# READ
print("\n REad - Ler / Mostrar ")
print(lista_clientes)

# UPDATE
print("\nUptade - Atualizar / Alterar")
nome_para_atualizar = "Marta"
if nome_para_atualizar in lista_clientes:
    novo_nome = "Marta Silva"
    indice = lista_clientes.index(nome_para_atualizar)
    lista_clientes[indice] = novo_nome
    print(f"O nome {nome_para_atualizar} foi atualizado pra {novo_nome}")
else:
    print(f"O nome {nome_para_atualizar} não foi encontrado")

print(lista_clientes)

# DELETE
print("\nDelete - Excluir / Remover")
nome_para_excluir = "Maria"
if nome_para_excluir in lista_clientes:
    lista_clientes.remove(nome_para_excluir)
    print (f"{nome_para_excluir} foi excluído com sucesso!")
else:
    print(F"O nome {nome_para_excluir} não foi encontrado.")

print(lista_clientes)