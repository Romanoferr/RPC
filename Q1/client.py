import rpyc
import sys

# Verifica se foi passado pelo menos um argumento (o endereço do servidor)
if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]  # Obtém o endereço do servidor a partir do primeiro argumento

# Estabelece uma conexão com o servidor no endereço especificado e na porta 18861
conn = rpyc.connect(server, 18861)

# Imprime o objeto raiz do serviço remoto (representação do objeto MyService no servidor)
print("O objeto raiz do servidor é:", conn.root)

print("O método get_answer() retorna:", conn.root.get_answer())

print("O atributo the_real_answer_though contém:", conn.root.the_real_answer_though)
