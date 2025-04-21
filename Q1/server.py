import rpyc
import time

class MyService(rpyc.Service):
    def on_connect(self, conn):
        # código que é executado quando uma conexão é iniciada
        print("Conexão iniciada")
        pass

    def on_disconnect(self, conn):
        # código que é executado quando uma conexão é finalizada
        print("Conexão finalizada")
        pass

    def exposed_get_answer(self):
        # este é um método exposto
        return 42

    exposed_the_real_answer_though = 43  # este é um atributo exposto

    def get_question(self):
        # este método não é exposto
        return "Qual é a cor do cavalo branco de Napoleão?"

    def exposed_sum_vector(self, vector):
        # método para somar os elementos de um vetor
        result = sum(vector)
        return result


# Para iniciar o servidor
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    t = ThreadedServer(MyService, port=18861)
    print("Servidor iniciado na porta 18861")
    t.start()
