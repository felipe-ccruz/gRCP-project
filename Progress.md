# Progresso do Projeto gRPC

Checklist passo a passo para entender, implementar e aprender o projeto de gRPC com Python. Marque cada item conforme for avançando.

---

## Etapa 1 — Fundamentos Teóricos

- [x] Ler o [Lauda.md](Lauda.md) por completo para entender o escopo do exercício.
- [ ] Pesquisar o que é **RPC (Remote Procedure Call)** e por que ele existe.
- [ ] Entender o que é **gRPC** e como ele difere de RPC tradicional.
- [ ] Estudar o que é **Protocol Buffers (protobuf)** e por que é usado como IDL.
- [ ] Comparar **gRPC vs REST** (vantagens, desvantagens e quando usar cada um).
- [ ] Compreender o papel do **HTTP/2** no gRPC (multiplexação, streaming, etc.).

---

## Etapa 2 — Preparação do Ambiente

- [x] Verificar a versão do Python instalado (`python --version`) — precisa ser **3.7+**.
- [x] Criar um ambiente virtual para o projeto:
  ```bash
  python -m venv venv
  ```
- [x] Ativar o ambiente virtual:
  - Windows: `venv\Scripts\activate`
  - Linux/Mac: `source venv/bin/activate`
- [x] Instalar as dependências necessárias:
  ```bash
  pip install grpcio grpcio-tools
  ```
- [x] Confirmar a instalação:
  ```bash
  pip list | findstr grpc
  ```
- [x] Criar um arquivo `requirements.txt` com as dependências do projeto:
  ```bash
  pip freeze > requirements.txt
  ```

---

## Etapa 3 — Definição do Serviço (Protocol Buffers)

- [x] Criar o arquivo `calculator.proto` na raiz do projeto.
- [x] Definir a sintaxe (`proto3`) e o pacote `calculator`.
- [x] Criar a mensagem `SumRequest` com os campos `a` e `b` (int32).
- [x] Criar a mensagem `SumResponse` com o campo `result` (int32).
- [x] Definir o serviço `Calculator` com o método RPC `Sum`.
- [x] Entender o significado dos **números de campo** (`= 1`, `= 2`) no protobuf.

---

## Etapa 4 — Geração dos Stubs

- [x] Executar o comando para gerar os stubs em Python:
  ```bash
  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
  ```
- [x] Verificar a criação dos arquivos:
  - [x] `calculator_pb2.py` (mensagens).
  - [x] `calculator_pb2_grpc.py` (serviço/stub).
- [x] Abrir e ler os arquivos gerados para entender o código produzido.

---

## Etapa 5 — Implementação do Servidor

- [x] Criar o arquivo `server.py`.
- [x] Importar `grpc`, `concurrent.futures`, `time`, `calculator_pb2` e `calculator_pb2_grpc`.
- [x] Criar a classe `CalculatorServicer` herdando da classe gerada.
- [x] Implementar o método `Sum(self, request, context)`.
- [x] Configurar o servidor com `ThreadPoolExecutor` (10 threads).
- [x] Registrar o servicer e configurar a porta `50051`.
- [x] Adicionar lógica para manter o servidor rodando e tratar `KeyboardInterrupt`.
- [x] Testar a execução do servidor:
  ```bash
  python server.py
  ```

---

## Etapa 6 — Implementação do Cliente

- [x] Criar o arquivo `client.py`.
- [x] Importar `grpc`, `calculator_pb2` e `calculator_pb2_grpc`.
- [x] Criar o canal (`grpc.insecure_channel`) apontando para `localhost:50051`.
- [x] Instanciar o stub `CalculatorStub`.
- [x] Montar a requisição `SumRequest(a=7, b=5)` e chamar `stub.Sum(...)`.
- [x] Imprimir o resultado retornado.
- [x] Testar a execução do cliente (com o servidor já em execução):
  ```bash
  python client.py
  ```

---

## Etapa 7 — Testes e Validação

- [x] Confirmar que o cliente recebe o resultado correto (ex.: `7 + 5 = 12`).
- [x] Validar que o servidor exibe a operação no console.
- [x] Testar com diferentes valores de entrada.
- [x] Testar valores limite (`0`, números negativos, `int32` máximo).
- [x] Verificar o comportamento quando o servidor está desligado. (retorna `DEADLINE_EXCEEDED`/`UNAVAILABLE`)

---

## Etapa 8 — Extensões e Experimentos

- [x] Adicionar novos métodos ao serviço:
  - [x] `Subtract` (subtração).
  - [x] `Multiply` (multiplicação).
  - [x] `Divide` (divisão, com tratamento de divisão por zero).
- [x] Atualizar o `.proto` e regenerar os stubs.
- [x] Implementar os novos métodos no servidor e cliente.
- [ ] Experimentar **streaming**:
  - [ ] *Server streaming* (servidor envia múltiplas respostas).
  - [ ] *Client streaming* (cliente envia múltiplas requisições).
  - [ ] *Bidirectional streaming* (ambos).
- [ ] Estudar e implementar **segurança SSL/TLS** entre cliente e servidor.
- [x] Implementar **tratamento de erros** com `grpc.StatusCode`.

---

## Etapa 9 — Aprofundamento e Documentação

- [x] Documentar o passo a passo em um `README.md` próprio.
- [ ] Comparar o desempenho do gRPC com uma versão REST equivalente.
- [ ] Pesquisar como aplicar gRPC em um cenário de **microsserviços**.
- [ ] Explorar **interceptors** no gRPC (logging, autenticação, etc.).
- [ ] Estudar **load balancing** e **service discovery** com gRPC.

---

## Etapa 10 — Entrega Final

- [ ] Revisar todos os arquivos do projeto.
- [ ] Garantir que o código está limpo e comentado onde necessário.
- [ ] Subir o projeto para o repositório Git com commits descritivos.
- [ ] Preparar uma demonstração funcional do servidor e cliente.
- [ ] Anotar dúvidas e aprendizados para discussão em aula.
