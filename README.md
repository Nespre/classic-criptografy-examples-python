# Exemplo-de-Cifra-de-Vernam-XOR---Python
Este é um exemplo prático de como a cifra de Vernam funciona, utilizando a operação XOR em Python. O script recebe um texto e uma chave, e gera o texto cifrado nos formatos Unicode, binário e hexadecimal.

<br>

## Como funciona?

1. O script converte o texto e a chave para representações Unicode.
2. Aplica a operação XOR entre os caracteres do texto e da chave.
3. Gera a cifra nos seguintes formatos:
   - Unicode
   - Binário
   - Hexadecimal


## Como usar?

1. Clone o repositório:<br>
   git clone https://github.com/SEU_USUARIO/EXEMPLO_CIFRA_VERNAM.git
2. Navegue até o diretório do projeto:<br>
   cd EXEMPLO_CIFRA_VERNAM
3. Execute o script Python:<br>
   python cifra_vernan.py
   

## Parâmetros:

text: O texto a ser cifrado.<br>
key: A chave utilizada na cifra.


## Exemplo de Resultado:
Se você usar o texto ESTAMOS NA AULA DE CRIPTOGRAFIA e uma chave aleatória, o script gerará a cifra nos três formatos mencionados.<br>
+ Unicode: [123, 104, 110, ...]<br>
+ Representação oficial: ['\x7b', '\x68', '\x6e', ...]<br>
+ Binário: ['01111011', '01101000', '01101110', ...]<br>
+ Hexadecimal: ['0x7b', '0x68', '0x6e', ...]
   

## Contribuição
Sinta-se à vontade para contribuir! Abra um pull request ou crie um issue para discutir melhorias.


## Licença
Este projeto está licenciado sob a MIT License. Veja LICENSE para mais detalhes.
