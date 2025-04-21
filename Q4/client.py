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

# Para a questão 4 - criando um vetor de n posições e chamando soma do servidor (elementos em [0,n-1])
vector = list(range(n))
print(vector)
print(f"\nSomando vetor com {n} elementos...")

result = conn.root.sum_vector(vector)

print(f"Resultado da soma: {result}")