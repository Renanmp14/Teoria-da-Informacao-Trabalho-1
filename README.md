# Teoria da Informação — TP1 + TP2

Ferramenta completa de codificação, detecção e correção de erros, implementando os principais algoritmos estudados em Teoria da Informação. Possui interface gráfica (Tkinter) e interface de linha de comando (CLI).

---

## Sumário

- [Algoritmos implementados](#algoritmos-implementados)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Executar a interface gráfica](#executar-a-interface-gráfica)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como usar a interface gráfica](#como-usar-a-interface-gráfica)
  - [Aba 1 — Codificação / Decodificação (TP1)](#aba-1--tp1-codificação--decodificação)
  - [Aba 2 — Detecção e Correção de Erro (TP2)](#aba-2--tp2-detecção-e-correção-de-erro)
  - [Aba 3 — Comunicação Socket (TP2)](#aba-3--tp2-comunicação-socket)
  - [Resumo rápido de entradas válidas](#resumo-rápido-de-entradas-válidas)
- [Como usar a CLI](#como-usar-a-cli)
  - [encode](#encode)
  - [decode](#decode)
  - [bit-flip](#bit-flip)
  - [Referência rápida](#referência-rápida)
- [Executar testes](#executar-testes)

---

## Algoritmos implementados

### TP1 — Codificação de Fonte

| Algoritmo | Codificação | Decodificação | Observação |
|---|---|---|---|
| Golomb | ✅ | ✅ | Requer parâmetro `M` ≥ 1 |
| Elias-Gamma | ✅ | ✅ | Apenas inteiros positivos (≥ 1) |
| Fibonacci / Zeckendorf | ✅ | ✅ | Representação com stop-bit ao final |
| Huffman | ✅ | ✅ | Aceita texto e números; saída em JSON |
| Bit-flip (inserção de erro) | ✅ | — | Suporta semente para reprodutibilidade |

### TP2 — Detecção e Correção de Erros

| Algoritmo | Codificação | Verificação / Correção | Observação |
|---|---|---|---|
| CRC-4 | ✅ | ✅ | Polinômio G(x) = x⁴ + x + 1 → `10011` |
| Hamming (7,4) | ✅ | ✅ | Detecta e corrige 1 bit de erro |
| Repetição Ri | ✅ | ✅ | Votação majoritária; R deve ser ímpar |
| Socket TCP | ✅ | ✅ | Servidor/cliente em localhost:65432 |

---

## Requisitos

- **Python 3.9 ou superior**
- Apenas bibliotecas da **stdlib** (`tkinter`, `socket`, `threading`, `json`, `heapq`, `collections`) — nenhum pacote externo necessário para a GUI

---

## Instalação

### Somente para a GUI (sem instalação de pacote)

Nenhuma instalação é necessária. Basta ter Python 3.9+ e executar:

```bash
python main.py
```

### Para usar também a CLI (`cripto-da-galera`)

#### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

#### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

Após instalar, o comando `cripto-da-galera` fica disponível no ambiente virtual:

```bash
cripto-da-galera --help
```

> Se a instalação falhar em ambiente sem internet, tente:
> ```bash
> pip install -e . --no-build-isolation
> ```

---

## Executar a interface gráfica

```bash
python main.py
```

A janela abre com três abas: **TP1 — Codificação/Decodificação**, **TP2 — Detecção e Correção de Erro** e **TP2 — Comunicação Socket**.

---

## Estrutura do projeto

```
.
├── main.py                  # Ponto de entrada — abre a GUI
├── gui.py                   # Interface gráfica Tkinter (3 abas)
├── utils.py                 # Utilitários: flip_bit, text_to_ascii, validate_binary
│
├── encoding/                # Módulos de codificação (TP1)
│   ├── __init__.py
│   ├── golomb.py
│   ├── elias_gamma.py
│   ├── fibonacci.py
│   └── huffman.py           # Suporta texto e números
│
├── error/                   # Módulos de detecção/correção de erro (TP2)
│   ├── __init__.py
│   ├── crc.py               # CRC-4 com G(x) = x⁴+x+1
│   ├── hamming.py           # Hamming (7,4)
│   └── repetition.py        # Código de repetição Ri
│
├── socket_comm/             # Comunicação TCP (TP2)
│   ├── __init__.py
│   ├── server.py            # Servidor TCP (localhost:65432)
│   └── client.py            # Cliente TCP
│
├── src/                     # Código original da CLI (preservado)
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── cli.py
│   ├── encoders/
│   │   └── encoders.py
│   └── decoders/
│       └── decoders.py
│
├── tests/
│   ├── conftest.py
│   ├── test_algoritmos.py
│   ├── test_carga.py
│   └── test_cli.py
│
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## Como usar a interface gráfica

Execute `python main.py` para abrir a janela. Ela possui três abas.

---

### Aba 1 — TP1: Codificação / Decodificação

#### Campo "Texto / Número(s)"

É a entrada principal. O que você digitar aqui define o que será codificado.

| O que digitar | Interpretação |
|---|---|
| `hello` | Texto — cada letra é um símbolo |
| `abracadabra` | Texto — cada letra é um símbolo |
| `65 66 67` | Números separados por espaço — cada número é um símbolo |
| `3,5,7,3` | Números separados por vírgula — cada número é um símbolo |
| `104` | Número único — tratado como texto (cada dígito é símbolo) |

> Para Golomb, Elias-Gamma e Fibonacci: se você digitar **texto**, ele é convertido automaticamente para ASCII antes de codificar. Se digitar **números**, eles são usados diretamente.

---

#### Método: Golomb

Requer o **parâmetro M** (inteiro positivo ≥ 1). Um campo extra aparece ao selecionar este método.

| Campo "Texto / Número(s)" | M | Codeword gerado |
|---|---|---|
| `13` | `4` | `111001` |
| `0` | `4` | `0` |
| `7` | `2` | `11100` |
| `A` | `4` | Converte `A` → ASCII 65, codifica 65 |
| `hi` | `3` | Converte `h`→104, `i`→105, codifica cada um |

**Para decodificar:** cole o codeword no campo **"Codeword atual"** e clique em **Decodificar**. Se houver vários, separe por espaço: `111001 0 11100`.

---

#### Método: Elias-Gamma

Aceita inteiros positivos (≥ 1). Texto é convertido para ASCII automaticamente.

| Campo "Texto / Número(s)" | Codeword gerado |
|---|---|
| `1` | `1` |
| `2` | `010` |
| `10` | `0001010` |
| `A` | Converte `A` → 65 → `000000001000001` |
| `hi` | Converte `h`→104 e `i`→105, exibe ambos |

**Para decodificar:** cole os bits no campo **"Codeword atual"**. Se houver múltiplos, separe por espaço.

---

#### Método: Fibonacci / Zeckendorf

Aceita inteiros positivos (≥ 1). Texto vira ASCII automaticamente.

| Campo "Texto / Número(s)" | Codeword gerado |
|---|---|
| `1` | `11` |
| `4` | `1011` |
| `13` | `0000011` |
| `66` | `0010100011` |
| `hi` | Converte `h`→104 e `i`→105 |

**Para decodificar:** cole os bits (com stop-bit `1` ao final) no campo **"Codeword atual"**.

---

#### Método: Huffman

Aceita **texto** (cada caractere é símbolo) ou **números separados por espaço/vírgula** (cada número é símbolo).

| Campo "Texto / Número(s)" | Modo detectado | O que acontece |
|---|---|---|
| `hello` | Texto | Codifica h, e, l, o como símbolos |
| `abracadabra` | Texto | Frequências: a=5, b=2, r=2, c=1, d=1 |
| `65 66 67 65` | Numérico | Símbolos são "65", "66", "67" |
| `3,5,7,3` | Numérico | Símbolos são "3", "5", "7" |
| `aabc` | Texto | Frequências: a=2, b=1, c=1 |

> Huffman exige **ao menos 2 símbolos distintos** na entrada. `aaaa` retornará erro.

**Para decodificar:** cole o **JSON completo** gerado pelo codificador no campo **"Codeword atual"**:

```json
{"codes": {"l": "0", "h": "100", "e": "101", "o": "11"}, "data": "100101000011", "mode": "text"}
```

---

#### Inserção de Erro — Aba 1 (Bit Flip)

Após codificar, o codeword aparece automaticamente no campo **"Codeword atual"**.

1. Digite uma posição no campo **"Posição do bit (0-based)"**
2. Clique **"Inserir Erro"** — o bit naquela posição é invertido (0→1 ou 1→0)
3. Clique **"Decodificar"** para ver o efeito do erro na saída

| Codeword | Posição | Resultado |
|---|---|---|
| `111001` | `0` | `011001` (1º bit invertido) |
| `111001` | `5` | `111000` (último bit invertido) |
| `0001010` | `3` | `0000010` |

---

### Aba 2 — TP2: Detecção e Correção de Erro

#### Método: CRC-4

Polinômio gerador fixo: **G(x) = x⁴ + x + 1 → `10011`**

O campo **"Bits"** aceita qualquer sequência de `0`s e `1`s.

| Entrada | Bits de CRC | Codeword final |
|---|---|---|
| `1101` | `0100` | `11010100` |
| `1010` | `1110` | `10101110` |
| `11001010` | `0110` | `110010100110` |

**Para verificar:** cole o codeword completo (dados + CRC) no campo **"Codeword"** e clique **"Verificar / Decodificar"**.

- Resto = `0000` → sem erros
- Resto ≠ `0000` → erro detectado

> CRC-4 detecta erros mas **não os corrige**. Para correção, use Hamming.

---

#### Método: Hamming (7,4)

**Para codificar:** exatamente **4 bits** no campo "Bits".

| Entrada (4 bits) | Codeword (7 bits) | Layout |
|---|---|---|
| `1011` | `0110011` | p1 p2 d1 p4 d2 d3 d4 |
| `0000` | `0000000` | |
| `1111` | `1111111` | |
| `1010` | `1110100` | |
| `0101` | `0001101` | |

**Para decodificar/corrigir:** cole os **7 bits** no campo **"Codeword"** e clique **"Verificar / Decodificar"**.
- Exibe a posição do erro (1–7, base 1) se houver
- Mostra o codeword corrigido e os 4 bits de dados recuperados

---

#### Método: Repetição Ri

**Campo "R":** inteiro ímpar ≥ 1 (ex: `3`, `5`, `7`). R par é rejeitado pois impossibilita a votação majoritária.

| Entrada | R | Codeword gerado |
|---|---|---|
| `101` | `3` | `111000111` |
| `10` | `5` | `1111100000` |
| `1101` | `3` | `111111000111` |
| `0` | `3` | `000` |

**Para decodificar:** cole o codeword no campo **"Codeword"** com o mesmo valor de R e clique **"Verificar / Decodificar"**.
- Aplica votação majoritária em cada grupo de R bits
- Informa os índices (0-based) dos grupos com votos discordantes

---

#### Inserção de Erro Manual — Aba 2

1. Codifique uma mensagem — o codeword é copiado automaticamente para o campo **"Codeword"**
2. Digite a posição do bit a inverter em **"Posição (0-based)"**
3. Clique **"Inserir Erro"**
4. Clique **"Verificar / Decodificar"** para ver a detecção/correção em ação

**Exemplo prático com Hamming:**

```
Dados originais : 1011
Codeword gerado : 0110011   →   p1 p2 d1 p4 d2 d3 d4
Erro na posição 4: 0110111
Decodificar → detecta erro na posição 5, corrige para 0110011, dados = 1011
```

---

### Aba 3 — TP2: Comunicação Socket

#### Passo a passo

1. **Clique em "Iniciar Servidor"**
   - O status muda para `● Rodando` (verde)
   - O servidor TCP fica escutando em `localhost:65432`
   - Pode ser iniciado e parado quantas vezes quiser

2. **Preencha o campo "Mensagem (bits)"** — apenas `0` e `1`

3. **Selecione o método:** Hamming, CRC-4 ou Repetição

4. **Opcional — marque "Sim, posição:"** para inserir um erro antes de enviar
   - O bit na posição informada é invertido antes da transmissão

5. **Clique em "Enviar (Cliente)"**
   - O cliente codifica, opcionalmente corrompe e envia ao servidor via TCP
   - O servidor verifica/corrige e responde com o resultado
   - Tudo aparece no log em tempo real

---

#### Exemplos por método

**Hamming (7,4)**

| Campo "Mensagem" | O que acontece |
|---|---|
| `1011` | Codifica → `0110011`, envia, servidor decodifica → `1011` |
| `0000` | Codifica → `0000000`, servidor confirma sem erros |
| `1111` | Codifica → `1111111`, servidor decodifica → `1111` |

> Hamming exige **exatamente 4 bits**. `10` ou `10110` retornarão erro.

**CRC-4**

| Campo "Mensagem" | O que acontece |
|---|---|
| `1101` | Calcula CRC → `11010100`, servidor verifica resto = `0000` |
| `10101010` | Qualquer tamanho funciona |

**Repetição (R=3)**

| Campo "Mensagem" | O que acontece |
|---|---|
| `101` | Codifica → `111000111`, servidor vota e decodifica → `101` |
| `11` | Codifica → `111111`, servidor decodifica → `11` |

---

#### Exemplo com erro deliberado

**Cenário:** verificar se o Hamming detecta e corrige 1 bit errado na transmissão.

1. Mensagem: `1011`
2. Método: Hamming
3. Marcar "Sim, posição: `4`"
4. Clicar **"Enviar (Cliente)"**

**Log esperado:**

```
[Cliente] Dados originais : 1011
[Cliente] Método          : hamming
[Cliente] Codeword enviado: 0110011
[Cliente] ⚠ Erro inserido na posição 4: 0110111
[Servidor] Recebido   : 0110111
[Servidor] Erro?       : Sim
[Servidor] Corrigido  : 0110011
[Servidor] Decodificado: 1011
[Servidor] Mensagem    : Erro corrigido na posição 5
```

---

### Resumo rápido de entradas válidas

| Método | Campo | Exemplo válido | Exemplo inválido |
|---|---|---|---|
| Golomb | Texto/Nº | `13` ou `hello` | número negativo |
| Elias-Gamma | Texto/Nº | `10` ou `AB` | `0` ou negativo |
| Fibonacci | Texto/Nº | `13` ou `hi` | `0` ou negativo |
| Huffman | Texto/Nº | `hello` ou `3 5 7` | único símbolo (`aaaa`) |
| CRC-4 | Bits | `1101` | `abc` ou `1 0 1` (com espaço) |
| Hamming — codificar | Bits | `1011` (4 bits) | 3 ou 5 bits |
| Hamming — decodificar | Bits | `0110011` (7 bits) | 6 ou 8 bits |
| Repetição | Bits + R ímpar | `101` com R=`3` | R=`2` ou R=`4` |
| Socket — Hamming | Bits | `1011` (4 bits) | qualquer outro tamanho |
| Socket — CRC | Bits | `11001010` | letras ou espaços |
| Socket — Repetição | Bits + R ímpar | `1011` com R=`3` | R par |

---

## Como usar a CLI

A CLI é organizada em dois comandos principais — `encode` e `decode` — cada um com subcomandos para cada algoritmo.

```
cripto-da-galera <comando> <subcomando> [argumentos]
```

---

### encode

#### Golomb

Codifica um inteiro não-negativo com o parâmetro `m`.

```bash
cripto-da-galera encode golomb <m> <n>
```

```bash
cripto-da-galera encode golomb 4 13
# Saída: 111001
```

---

#### Elias-Gamma

Codifica um inteiro positivo.

```bash
cripto-da-galera encode elias-gamma <n>
```

```bash
cripto-da-galera encode elias-gamma 10
# Saída: 0001010
```

---

#### Fibonacci / Zeckendorf

Codifica um inteiro positivo na representação de Zeckendorf com stop-bit.

```bash
cripto-da-galera encode fibonacci <n>
```

```bash
cripto-da-galera encode fibonacci 66
# Saída: 0010100011
```

---

#### Huffman

Codifica um texto. A saída é um JSON com o mapa de códigos (`codes`), os bits resultantes (`data`) e o modo (`mode`). Guarde essa saída para decodificar depois.

```bash
cripto-da-galera encode huffman "<texto>"
```

```bash
cripto-da-galera encode huffman "hello"
# Saída: {"codes": {"h": "00", "e": "01", "o": "10", "l": "11"}, "data": "0001111110", "mode": "text"}
```

---

#### Bit-flip (inserção de erro)

Aplica inversões aleatórias de bits com uma dada probabilidade.

```bash
cripto-da-galera encode bit-flip <bits> <probabilidade> [--seed <N>]
```

| Argumento | Tipo | Descrição |
|---|---|---|
| `bits` | string binária | Ex: `10110011` |
| `probabilidade` | float 0.0–1.0 | Chance de cada bit ser invertido |
| `--seed` | inteiro (opcional) | Semente para resultado reproduzível |

```bash
cripto-da-galera encode bit-flip 10101010 0.5 --seed 42
# Saída: 11011011
```

---

### decode

#### Golomb

```bash
cripto-da-galera decode golomb <m> <bits>
```

```bash
cripto-da-galera decode golomb 4 111001
# Saída: 13
```

---

#### Elias-Gamma

```bash
cripto-da-galera decode elias-gamma <bits>
```

```bash
cripto-da-galera decode elias-gamma 0001010
# Saída: 10
```

---

#### Fibonacci / Zeckendorf

```bash
cripto-da-galera decode fibonacci <bits>
```

```bash
cripto-da-galera decode fibonacci 0010100011
# Saída: 66
```

---

#### Huffman

A entrada deve ser o JSON completo gerado pelo encoder.

```bash
# Linux / macOS
cripto-da-galera decode huffman '{"codes": {"h": "00", "e": "01", "o": "10", "l": "11"}, "data": "0001111110", "mode": "text"}'
# Saída: hello

# PowerShell (aspas escapadas)
cripto-da-galera decode huffman '{\"codes\": {\"h\": \"00\", \"e\": \"01\", \"o\": \"10\", \"l\": \"11\"}, \"data\": \"0001111110\", \"mode\": \"text\"}'
```

> **Dica:** Encadeando encode e decode num script bash:
> ```bash
> encoded=$(cripto-da-galera encode huffman "minha mensagem")
> cripto-da-galera decode huffman "$encoded"
> ```

---

### Referência rápida

```bash
# Encode
cripto-da-galera encode golomb      <m> <n>
cripto-da-galera encode elias-gamma <n>
cripto-da-galera encode fibonacci   <n>
cripto-da-galera encode huffman     "<texto>"
cripto-da-galera encode bit-flip    <bits> <prob> [--seed N]

# Decode
cripto-da-galera decode golomb      <m> <bits>
cripto-da-galera decode elias-gamma <bits>
cripto-da-galera decode fibonacci   <bits>
cripto-da-galera decode huffman     '<json>'

# Utilitários
cripto-da-galera hello
cripto-da-galera legend
cripto-da-galera --version
cripto-da-galera --help
```

---

## Executar testes

Instale as dependências de desenvolvimento:

```bash
pip install -r requirements.txt
```

```bash
# Rodar toda a suíte
pytest

# Apenas testes da CLI
pytest tests/test_cli.py -v

# Apenas testes dos algoritmos
pytest tests/test_algoritmos.py -v

# Com cobertura
pip install pytest-cov
pytest --cov=src
```
