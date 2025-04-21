import rpyc
import sys
import time

if len(sys.argv) < 3:
    exit("Usage {} SERVER VECTOR_SIZE".format(sys.argv[0]))

server = sys.argv[1]
n = int(sys.argv[2])

# Conectar ao servidor
print(f"Conectando ao servidor {server}...")
conn = rpyc.connect(server, 18861)

# Para as questões 1 e 2
print("Resultado de root:", conn.root)
print("Resultado de get_answer():", conn.root.get_answer())
print("Valor de the_real_answer_though:", conn.root.the_real_answer_though)

# Para a questão 3 - chamando o método get_question -> Comentado pois da erro
# print(conn.get_question())
# print(conn.root.get_question)

# Para a questão 4 - criando um vetor de n posições e somando
vector = list(range(n))
print(f"\nSomando vetor com {n} elementos...")

start = time.time()
result = conn.root.sum_vector(vector)
end = time.time()

print(f"Resultado da soma: {result}")
print(f"Tempo total de execução no cliente: {end - start}")