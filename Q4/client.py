import rpyc
import sys
import time

# Para a questão 4 em diante

if len(sys.argv) < 3:
    exit("Usage {} SERVER VECTOR_SIZE".format(sys.argv[0]))

server = sys.argv[1]
n = int(sys.argv[2])

# Conectar ao servidor
print(f"Conectando ao servidor {server}...")
conn = rpyc.connect(server, 18861)

# criando um vetor de n posições e chamando soma do servidor
# elementos em [0,n-1]

vector = list(range(n))
print(f"\nSomando vetor com {n} elementos...")

start = time.time()
result = conn.root.sum_vector(vector)
end = time.time()

print(f"Resultado da soma: {result}")
print(f"Tempo total de execução no cliente: {end - start}")
