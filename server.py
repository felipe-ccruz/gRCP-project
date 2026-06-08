import grpc
from concurrent import futures
import time

import calculator_pb2
import calculator_pb2_grpc


# Implementacao do servico Calculator
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    # Metodo original do exercicio (mantem a assinatura SumRequest/SumResponse).
    def Sum(self, request, context):
        result = request.a + request.b
        print(f"[Sum]      {request.a} + {request.b} = {result}")
        return calculator_pb2.SumResponse(result=result)

    def Add(self, request, context):
        result = request.a + request.b
        print(f"[Add]      {request.a} + {request.b} = {result}")
        return calculator_pb2.OperationResponse(result=result)

    def Subtract(self, request, context):
        result = request.a - request.b
        print(f"[Subtract] {request.a} - {request.b} = {result}")
        return calculator_pb2.OperationResponse(result=result)

    def Multiply(self, request, context):
        result = request.a * request.b
        print(f"[Multiply] {request.a} * {request.b} = {result}")
        return calculator_pb2.OperationResponse(result=result)

    def Divide(self, request, context):
        # Tratamento de divisao por zero usando os codigos de status do gRPC.
        if request.b == 0:
            message = "Divisao por zero nao e permitida."
            print(f"[Divide]   {request.a} / {request.b} -> ERRO: {message}")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(message)
            return calculator_pb2.OperationResponse(error=message)

        result = request.a / request.b
        print(f"[Divide]   {request.a} / {request.b} = {result}")
        return calculator_pb2.OperationResponse(result=result)


def serve():
    # Cria um servidor gRPC com um pool de 10 threads.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

    # Define a porta para escutar as requisicoes.
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC iniciado na porta 50051.")

    try:
        while True:
            time.sleep(86400)  # mantem o servidor ativo por 1 dia
    except KeyboardInterrupt:
        server.stop(0)
        print("Servidor interrompido.")


if __name__ == '__main__':
    serve()
