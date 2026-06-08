# gRPC Calculator — Python

Exercício de introdução ao **gRPC** com Python: uma calculadora cliente/servidor
definida via **Protocol Buffers**. Implementa o método `Sum` original do exercício
e as extensões `Add`, `Subtract`, `Multiply` e `Divide` (com tratamento de divisão
por zero usando `grpc.StatusCode`).

## Estrutura

| Arquivo | Descrição |
|---|---|
| `calculator.proto` | Definição do serviço e das mensagens (IDL). |
| `calculator_pb2.py` | Classes das mensagens (gerado). |
| `calculator_pb2_grpc.py` | Stub e servicer do serviço (gerado). |
| `server.py` | Servidor gRPC que implementa as operações. |
| `client.py` | Cliente que consome o serviço e demonstra as operações. |

## Pré-requisitos

- Python 3.7+ (testado com 3.13).
- Dependências em `requirements.txt`.

## Instalação

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/Mac
pip install -r requirements.txt
```

## Gerar os stubs (caso altere o `.proto`)

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
```

## Executar

Terminal 1 — servidor:

```bash
python server.py
```

Terminal 2 — cliente:

```bash
python client.py
```

### Saída esperada do cliente

```
O resultado da soma e: 12

--- Demonstracao das demais operacoes ---
Add(12, 4)      = 16.0
Subtract(12, 4) = 8.0
Multiply(12, 4) = 48.0
Divide(12, 4)   = 3.0

--- Tratamento de erro (divisao por zero) ---
Erro recebido do servidor: INVALID_ARGUMENT - Divisao por zero nao e permitida.
```

## Serviço (`calculator.proto`)

- `Sum(SumRequest) -> SumResponse` — método original do exercício.
- `Add / Subtract / Multiply / Divide (OperationRequest) -> OperationResponse` —
  extensões. `Divide` retorna `INVALID_ARGUMENT` quando o divisor é zero.
