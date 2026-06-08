import grpc
import calculator_pb2
import calculator_pb2_grpc


def run():
    # Conecta-se ao servidor na porta 50051.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)

        # 1) Metodo original do exercicio: Sum.
        request = calculator_pb2.SumRequest(a=7, b=5)
        response = stub.Sum(request)
        print(f"O resultado da soma e: {response.result}")

        print("\n--- Demonstracao das demais operacoes ---")

        # 2) Add / Subtract / Multiply usando OperationRequest.
        a, b = 12, 4
        op = calculator_pb2.OperationRequest(a=a, b=b)
        print(f"Add({a}, {b})      = {stub.Add(op).result}")
        print(f"Subtract({a}, {b}) = {stub.Subtract(op).result}")
        print(f"Multiply({a}, {b}) = {stub.Multiply(op).result}")
        print(f"Divide({a}, {b})   = {stub.Divide(op).result}")

        # 3) Tratamento de erro: divisao por zero.
        print("\n--- Tratamento de erro (divisao por zero) ---")
        try:
            stub.Divide(calculator_pb2.OperationRequest(a=10, b=0))
        except grpc.RpcError as e:
            print(f"Erro recebido do servidor: {e.code().name} - {e.details()}")


if __name__ == '__main__':
    run()
