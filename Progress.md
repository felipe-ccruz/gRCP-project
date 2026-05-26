# Progresso do Projeto gRPC

Checklist passo a passo para entender, implementar e aprender o projeto de gRPC com Python. Marque cada item conforme for avançando.

---

## Etapa 1 — Fundamentos Teóricos

- [ ] Ler o [Lauda.md](Lauda.md) por completo para entender o escopo do exercício.
- [ ] Pesquisar o que é **RPC (Remote Procedure Call)** e por que ele existe.
- [ ] Entender o que é **gRPC** e como ele difere de RPC tradicional.
- [ ] Estudar o que é **Protocol Buffers (protobuf)** e por que é usado como IDL.
- [ ] Comparar **gRPC vs REST** (vantagens, desvantagens e quando usar cada um).
- [ ] Compreender o papel do **HTTP/2** no gRPC (multiplexação, streaming, etc.).

---

## Etapa 2 — Preparação do Ambiente

- [ ] Verificar a versão do Python instalado (`python --version`) — precisa ser **3.7+**.
- [ ] Criar um ambiente virtual para o projeto:
  ```bash
  python -m venv venv
  ```
- [ ] Ativar o ambiente virtual:
  - Windows: `venv\Scripts\activate`
  - Linux/Mac: `source venv/bin/activate`
- [ ] Instalar as dependências necessárias:
  ```bash
  pip install grpcio grpcio-tools
  ```
- [ ] Confirmar a instalação:
  ```bash
  pip list | findstr grpc
  ```
- [ ] Criar um arquivo `requirements.txt` com as dependências do projeto:
  ```bash
  pip freeze > requirements.txt
  ```

---

## Etapa 3 — Definição do Serviço (Protocol Buffers)

- [ ] Criar o arquivo `calculator.proto` na raiz do projeto.
- [ ] Definir a sintaxe (`proto3`) e o pacote `calculator`.
- [ ] Criar a mensagem `SumRequest` com os campos `a` e `b` (int32).
- [ ] Criar a mensagem `SumResponse` com o campo `result` (int32).
- [ ] Definir o serviço `Calculator` com o método RPC `Sum`.
- [ ] Entender o significado dos **números de campo** (`= 1`, `= 2`) no protobuf.

---

## Etapa 4 — Geração dos Stubs

- [ ] Executar o comando para gerar os stubs em Python:
  ```bash
  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
  ```
- [ ] Verificar a criação dos arquivos:
  - [ ] `calculator_pb2.py` (mensagens).
  - [ ] `calculator_pb2_grpc.py` (serviço/stub).
- [ ] Abrir e ler os arquivos gerados para entender o código produzido.

---

## Etapa 5 — Implementação do Servidor

- [ ] Criar o arquivo `server.py`.
- [ ] Importar `grpc`, `concurrent.futures`, `time`, `calculator_pb2` e `calculator_pb2_grpc`.
- [ ] Criar a classe `CalculatorServicer` herdando da classe gerada.
- [ ] Implementar o método `Sum(self, request, context)`.
- [ ] Configurar o servidor com `ThreadPoolExecutor` (10 threads).
- [ ] Registrar o servicer e configurar a porta `50051`.
- [ ] Adicionar lógica para manter o servidor rodando e tratar `KeyboardInterrupt`.
- [ ] Testar a execução do servidor:
  ```bash
  python server.py
  ```

---

## Etapa 6 — Implementação do Cliente

- [ ] Criar o arquivo `client.py`.
- [ ] Importar `grpc`, `calculator_pb2` e `calculator_pb2_grpc`.
- [ ] Criar o canal (`grpc.insecure_channel`) apontando para `localhost:50051`.
- [ ] Instanciar o stub `CalculatorStub`.
- [ ] Montar a requisição `SumRequest(a=7, b=5)` e chamar `stub.Sum(...)`.
- [ ] Imprimir o resultado retornado.
- [ ] Testar a execução do cliente (com o servidor já em execução):
  ```bash
  python client.py
  ```

---

## Etapa 7 — Testes e Validação

- [ ] Confirmar que o cliente recebe o resultado correto (ex.: `7 + 5 = 12`).
- [ ] Validar que o servidor exibe a operação no console.
- [ ] Testar com diferentes valores de entrada.
- [ ] Testar valores limite (`0`, números negativos, `int32` máximo).
- [ ] Verificar o comportamento quando o servidor está desligado.

---

## Etapa 8 — Extensões e Experimentos

- [ ] Adicionar novos métodos ao serviço:
  - [ ] `Subtract` (subtração).
  - [ ] `Multiply` (multiplicação).
  - [ ] `Divide` (divisão, com tratamento de divisão por zero).
- [ ] Atualizar o `.proto` e regenerar os stubs.
- [ ] Implementar os novos métodos no servidor e cliente.
- [ ] Experimentar **streaming**:
  - [ ] *Server streaming* (servidor envia múltiplas respostas).
  - [ ] *Client streaming* (cliente envia múltiplas requisições).
  - [ ] *Bidirectional streaming* (ambos).
- [ ] Estudar e implementar **segurança SSL/TLS** entre cliente e servidor.
- [ ] Implementar **tratamento de erros** com `grpc.StatusCode`.

---

## Etapa 9 — Aprofundamento e Documentação

- [ ] Documentar o passo a passo em um `README.md` próprio.
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
