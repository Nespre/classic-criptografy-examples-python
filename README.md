# Exemplos de Criptografia em Python
Este repositório contém vários exemplos de implementações de técnicas de criptografia em Python. Cada script mostra como funcionam diferentes algoritmos de criptografia, como a Cifra de Vernam, Cifra de César, Vigenère, entre outros.
<br>

## Índice
- [Scripts Disponíveis](#scripts-disponíveis)
- [Como Funciona?](#como-funciona)
- [Como usar?](#como-usar)
- [Parâmetros Comuns](#parâmetros-comuns)
- [Contribuição](#contribuição)
- [Licença](#licença)
<br>

## Scripts Disponíveis

- **Cifra de César**  
  Implementação da clássica cifra de deslocamento.  
  **Exemplo:**  
  Entrada: "ABC" com chave 2 → Resultado: "CDE"

- **Cifra de Vigenère**  
  Utiliza uma chave repetitiva para criptografar texto.  
  **Exemplo:**  
  Entrada: "ATAQUE" com chave "LEMON" → Resultado: "LXFOPV"

- **Operação XOR - Exemplo Simples**  
  Demonstra a operação XOR entre dois valores inteiros.  
  **Exemplo:**  
  'A' (Unicode 65) ^ 'B' (Unicode 66) = 3

- **One-Time Pad**  
  Cifra simétrica usando uma chave aleatória do mesmo tamanho da mensagem.  
  **Exemplo:**  
  Entrada: "HELLO" + Chave Aleatória → Resultado cifrado em Unicode, Binário e Hexadecimal.

- **Cifra de Vernam (XOR)**  
  Exemplo de criptografia utilizando XOR entre a mensagem e a chave.  
  **Exemplo:**  
  Entrada: "ESTAMOS NA AULA DE CRIPTOGRAFIA" + Chave Aleatória → Resultado cifrado em Unicode, Binário e Hexadecimal.
<br>

## Como Funciona?
1. Cada script implementa uma técnica de criptografia diferente.
2. O texto é criptografado com a chave fornecida e os resultados são exibidos nos formatos Unicode, binário e hexadecimal.
3. Cada script pode ser executado individualmente, como demonstrado abaixo.
<br>

## Como usar?
1. Clone o repositório:
`git clone https://github.com/SEU_USUARIO/cryptography-examples-python.git`

2. Navegue até o diretório do projeto:
	`cd cryptography-examples-python/scripts`

3. Execute o script Python desejado. Exemplo:
   `python scripts/cifra_vernam.py`
<br>

## Parâmetros Comuns
**text:** O texto a ser cifrado. <br>
**key:** A chave utilizada na cifra.
<br>

## Contribuição
Sinta-se à vontade para contribuir! Abra um pull request ou crie um issue para discutir melhorias.
<br>

## Licença
Este projeto está licenciado sob a MIT License. Veja LICENSE para mais detalhes.
