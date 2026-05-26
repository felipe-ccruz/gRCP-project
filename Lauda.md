# Exercício: Introdução ao gRPC com Python

## 1. Introdução ao gRPC

O **gRPC** é um framework de chamada de procedimento remoto (RPC) de alto desempenho desenvolvido pelo Google. Ele permite definir serviços e mensagens usando o **Protocol Buffers** como linguagem de definição de interface (IDL).

Algumas vantagens do gRPC são:

- **Comunicação eficiente:** utiliza HTTP/2 para comunicação, permitindo streaming, multiplexação e melhor gerenciamento de conexões.
- **Linguagem independente:** permite gerar código para diversos idiomas (Python, Java, Go, etc.) a partir de um mesmo arquivo `.proto`.
- **Interface fortemente tipada:** a definição das mensagens e serviços garante consistência e validação dos dados trocados.

---

## 2. Objetivo do Exercício

Você aprenderá a:

- Definir um serviço gRPC usando um arquivo `.proto`;
- Gerar os *stubs* (código base) para o servidor e cliente;
- Implementar um servidor gRPC que realiza uma operação de soma;
- Criar um cliente gRPC que consome esse serviço.

---

## 3. Pré-requisitos

- Conhecimentos básicos de Python.
- Python instalado na sua máquina (recomenda-se a versão 3.7 ou superior).
- Instalação dos pacotes:
  - `grpcio`
  - `grpcio-tools`

Você pode instalá-los utilizando o `pip`:

```bash
pip install grpcio grpcio-tools
```

- O compilador `protoc` (geralmente instalado junto com o pacote `grpcio-tools` ou disponível separadamente).

---

## 4. Definindo o Serviço: Arquivo `.proto`

Crie um arquivo chamado `calculator.proto` com o seguinte conteúdo:

```proto
syntax = "proto3";

package calculator;

// Mensagem para a requisição de soma
message SumRequest {
    int32 a = 1;
    int32 b = 2;
}

// Mensagem para a resposta da soma
message SumResponse {
    int32 result = 1;
}

// Definição do serviço
service Calculator {
    // Método para somar dois números
    rpc Sum(SumRequest) returns (SumResponse);
}
```

**Explicação:**

- Declaramos o pacote `calculator` para organizar nosso código.
- Definimos duas mensagens: `SumRequest` (com os números `a` e `b`) e `SumResponse` (com o resultado da soma).
- Criamos o serviço `Calculator` com o método `Sum`.

---

## 5. Gerando os Stubs com o `protoc`

Utilize o comando abaixo para gerar os arquivos Python a partir do arquivo `.proto`:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
```

Esse comando criará dois arquivos:

- `calculator_pb2.py` – contém as classes geradas para as mensagens.
- `calculator_pb2_grpc.py` – contém as classes para o serviço, incluindo a definição do *servicer*.

---

## 6. Implementando o Servidor gRPC

Crie um arquivo chamado `server.py` com o seguinte conteúdo:

```python
import grpc
from concurrent import futures
import time

import calculator_pb2
import calculator_pb2_grpc


# Implementação do serviço Calculator
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    def Sum(self, request, context):
        # Soma os valores recebidos na requisição
        result = request.a + request.b
        print(f"Recebido: {request.a} + {request.b} = {result}")
        return calculator_pb2.SumResponse(result=result)


def serve():
    # Cria um servidor gRPC com um pool de 10 threads
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

    # Define a porta para escutar as requisições
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC iniciado na porta 50051.")

    try:
        while True:
            time.sleep(86400)  # mantém o servidor ativo por 1 dia
    except KeyboardInterrupt:
        server.stop(0)
        print("Servidor interrompido.")


if __name__ == '__main__':
    serve()
```

**Explicação:**

- A classe `CalculatorServicer` herda de `CalculatorServicer` gerado e implementa o método `Sum`.
- O servidor é configurado para escutar na porta `50051` e utiliza múltiplas threads para atender requisições.

---

## 7. Implementando o Cliente gRPC

Crie um arquivo chamado `client.py` com o seguinte conteúdo:

```python
import grpc
import calculator_pb2
import calculator_pb2_grpc


def run():
    # Conecta-se ao servidor na porta 50051
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    # Cria uma requisição com os números a serem somados
    request = calculator_pb2.SumRequest(a=7, b=5)
    response = stub.Sum(request)

    print(f"O resultado da soma é: {response.result}")


if __name__ == '__main__':
    run()
```

**Explicação:**

- O cliente cria um canal para se conectar ao servidor.
- Utiliza o *stub* `CalculatorStub` para chamar o método `Sum` com uma requisição contendo os valores.
- Exibe o resultado recebido na resposta.

---

## 8. Executando o Exercício

### 1. Inicie o Servidor

No terminal, execute:

```bash
python server.py
```

Você verá a mensagem indicando que o servidor foi iniciado na porta `50051`.

### 2. Execute o Cliente

Em outro terminal, execute:

```bash
python client.py
```

O cliente deverá imprimir o resultado da soma (por exemplo, *"O resultado da soma é: 12"*) e o servidor também mostrará no console a operação realizada.

---

## 9. Extensões e Discussões

- **Novos Métodos:**
  Você pode adicionar outros métodos à definição do serviço, como subtração, multiplicação ou divisão, atualizando o arquivo `.proto`, gerando novamente os *stubs* e implementando os métodos correspondentes no servidor.

- **Streaming:**
  Explore as capacidades de *streaming* do gRPC. Por exemplo, crie métodos que enviem múltiplas respostas (*server streaming*) ou que recebam múltiplas requisições (*client streaming*) ou ambos (*bidirectional streaming*).

- **Segurança:**
  Investigue como implementar segurança (SSL/TLS) em comunicações gRPC.

- **Comparação com REST:**
  Discuta as vantagens e desvantagens do gRPC em comparação com APIs RESTful, especialmente em termos de desempenho, tipagem e suporte a múltiplas linguagens.