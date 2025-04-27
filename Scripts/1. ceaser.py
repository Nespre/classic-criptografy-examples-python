"""
CIFRA DE CÉSAR - Criptografia e Descriptografia

Este script implementa a cifra de César, um método de criptografia simples e simétrico que 
desloca as letras do alfabeto por um número fixo de posições. A cifra pode ser usada tanto 
para criptografar quanto para descriptografar uma mensagem.

:Program Flow:
1. O usuário escolhe entre criptografar ou descriptografar um texto.
2. O usuário insere a mensagem que deseja criptografar/descriptografar.
3. O usuário fornece uma chave de segurança (um número inteiro entre 0 e 25).
4. A função converte o texto em unicode e aplica a cifra de César com a chave fornecida.
5. O programa retorna a representação do texto original em unicode e o texto criptografado/descriptografado.

:Functions:
- text_to_unicode(text: str) -> list
    Converte o texto para uma lista de valores Unicode, mantendo caracteres não alfabéticos inalterados.
- ceaser_cipher(text_to: str, key: int) -> list
    Aplica a cifra de César ao texto fornecido, usando a chave para criptografar ou descriptografar.

:Practical Examples:
1. Criptografar mensagem:
   - Mensagem: "HELLO"
   - Chave: 3
   - Resultado: "KHOOR"

2. Descriptografar mensagem:
   - Mensagem: "KHOOR"
   - Chave: 3
   - Resultado: "HELLO"

:Note: A chave deve ser um número inteiro entre 0 e 25.
"""

def text_to_unicode(text: str) -> list:
    """
    Converte o texto fornecido para uma lista de valores Unicode.

    :param text: Texto a ser convertido.
    :type text: str
    :return: Lista contendo os valores Unicode de cada caractere alfabético e os caracteres não alfabéticos.
    :rtype: list

    :Example:
        >>> text_to_unicode("HELLO")
        [72, 69, 76, 76, 79]
    """
    list_cha_unicode = []
    for cha in text:
        if cha.isalpha():
            list_cha_unicode.append(ord(cha))
        else:
            list_cha_unicode.append(cha)

    return list_cha_unicode

def ceaser_cipher(text_to: str, key: int) -> list:
    """
    Aplica a cifra de César para criptografar ou descriptografar o texto com a chave fornecida.

    :param text_to: Texto a ser criptografado ou descriptografado.
    :type text_to: str
    :param key: Chave para deslocar as letras do texto (inteiro).
    :type key: int
    :return: Uma lista com a representação do texto em Unicode e o texto criptografado/descriptografado.
    :rtype: list

    :Example:
        >>> ceaser_cipher("HELLO", 3)
        ([72, 69, 76, 76, 79], "KHOOR")
    """
    uni_text = text_to_unicode(text_to)
    result_text = ''

    for value in uni_text:
        if isinstance(value, int):
            letter = ((value-65) + key)%26 +65
            result_text += chr(letter)
        else:
            result_text += value

    return [uni_text, result_text]
    
if __name__ == '__main__':
    """
    Executa o sistema de cifragem, permitindo que o usuário escolha entre criptografar ou descriptografar uma mensagem.

    O programa oferece as seguintes opções ao usuário:
    1. Criptografar mensagem
    2. Descriptografar mensagem
    3. Sair

    O programa solicita uma chave (número inteiro entre 0 e 25) e a mensagem a ser cifrada ou decifrada.
    """
    while True:
        print('\nBEM VINDO AO SISTEMA QUE UTILIZA: CIFRA DE CÉSAR')
        print('\t1. Criptografar mensagem')
        print('\t2. Descriptografar mensagem')
        print('\t3. Sair')
        choice = input('O que deseja fazer? ')
        print()

        if choice in '12':
            print('CRIPTOGRAFAR' if choice == '1' else 'DESCRIPTOGRAFAR')
            print('Introduza a mensagem e a chave de segurança (número inteiro, 0-25)')
            orig_text = input('\tMensagem: ').upper()
            while True:
                key = input('\tChave: ')
                try:
                    key = int(key)
                    break
                except ValueError:
                    print('⚠️  Chave inválida. Certefique-se que é um número inteiro (0-25)⚠️')

            uni_text, result_text = ceaser_cipher(orig_text, key if choice == '1' else -key)
            print(f"""
Mensagem Inicial: \t\t{orig_text}
Representação em unicode: \t{uni_text}
Chave Usada: \t\t\t{key % 26}
Resultado: \t\t\t{result_text}""")
            
        else:
            break