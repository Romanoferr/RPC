import rpyc          # Importa a biblioteca RPyC para fazer chamadas remotas de procedimento
import sys           # Importa o módulo sys para acessar argumentos da linha de comando

# Verifica se foi passado pelo menos um argumento (o endereço do servidor)
if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))  # Mostra mensagem de uso correto e encerra o programa

server = sys.argv[1]  # Obtém o endereço do servidor a partir do primeiro argumento

# Estabelece uma conexão com o servidor no endereço especificado e na porta 18861
conn = rpyc.connect(server, 18861)

# Imprime o objeto raiz do serviço remoto (representação do objeto MyService no servidor)
print("O objeto raiz do servidor é:", conn.root)

# Chama o método remoto 'get_answer()' e imprime o resultado (42)
print("O método get_answer() retorna:", conn.root.get_answer())

# Acessa o atributo remoto 'the_real_answer_though' e imprime seu valor (43)
print("O atributo the_real_answer_though contém:", conn.root.the_real_answer_though)
