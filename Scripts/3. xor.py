"""
Operação XOR - Exemplo Simples

Este script demonstra como funciona a operação XOR em Python, utilizando o operador `^` para 
realizar a operação bit a bit entre dois valores inteiros.

:Program Flow:
1. A mensagem e a chave são convertidas para seus valores Unicode.
2. A operação XOR é aplicada entre a mensagem e a chave.
3. O script exibe o resultado da operação XOR.
4. A operação XOR pode ser revertida aplicando a operação novamente com a mesma chave.

:Functions:
- Não há funções específicas, o script realiza a operação XOR diretamente.

:Practical Examples:
1. Operação XOR:
   - Mensagem: "A" (Unicode: 65)
   - Chave: "B" (Unicode: 66)
   - Resultado da operação `message ^ key`: 3

2. Reverter a operação XOR:
   - Operação: `result ^ key`
   - Resultado: "A" (Reversão da operação original)

:Note: A operação XOR é simétrica, ou seja, aplicar a operação duas vezes com a mesma chave retorna o valor original.

"""

message = ord('A')
key = ord('B')
print('message =', message, '\nkey =', key)

result = message ^ key
print('\tmessage ^ key =',result) 
#retorna um resultado através de 2 números

back = result ^ key
print('\tresult ^ key =', back)
#é possível reverter esse resultado através da chave correta