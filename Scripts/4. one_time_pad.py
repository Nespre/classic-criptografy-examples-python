"""
ONE TIME PAD - Criptografia e Descriptografia

Este programa implementa a criptografia de "One-Time Pad", uma cifra de chave única, 
onde a chave é gerada aleatoriamente e tem o mesmo comprimento do texto a ser criptografado.

:Program Flow:
1. O usuário insere a mensagem a ser criptografada.
2. Uma chave aleatória binária é gerada com o mesmo comprimento da mensagem.
3. O texto é convertido para bits.
4. A operação XOR é aplicada entre a mensagem e a chave, gerando o texto cifrado.
5. O texto cifrado é revertido (decifrado) aplicando novamente a operação XOR com a mesma chave.
6. O texto decifrado é convertido novamente para texto legível.

:Practical Examples:
1. Criptografar mensagem:
   - Mensagem: "HELLO"
   - Chave gerada: Uma chave aleatória com o mesmo comprimento da mensagem.
   - Resultado da operação XOR (texto criptografado): [10010111, 10010100, 00000010, 11010001, 10000001]

2. Descriptografar mensagem:
   - Texto criptografado: [10010111, 10010100, 00000010, 11010001, 10000001]
   - Chave usada: A mesma chave aleatória gerada para criptografar.
   - Resultado da operação XOR (texto original): "HELLO"

:Note: A chave gerada é única e tem o mesmo comprimento da mensagem. Qualquer valor não alfabético 
é preservado na criptografia e descriptografia.
"""

from random import randint

def random_key(lengh_text: int) -> list:
    """
    A função gera uma chave aleatória binária apartir do comprimento da mensagem. 
    Retorna uma lista com todos os valores binários gerados (08b), com o mesmo número de caractéres da mensagem.

    :param lengh_text: lengh do texto, o qual a chave vai ter o mesmo comprimento
    :type lengh_text: int
    :return: list off all binarie numbers
    :rtype: list

    :Example:
        #len('hello') = 5
    >>> random_key(len('hello'))
    [11111111, 11110001, 01101110, 10111101, 11101110]
        #len(random_key('hello')) = 5
    """
    bin_per_cha = ''
    list_bin_key = []
    for cha in range(lengh_text):
        for bit in range(8):
            bin_per_cha += str(randint(0,1))
        list_bin_key.append(bin_per_cha)
        bin_per_cha = ''
    return list_bin_key
        
def text_to_bits(text: str) -> list:
    """
    A função converte o texto para uma lista com valores binarios. Cada valor da lista corresponde a um caracter do texto.
    
    :param text: texto a ser convertido
    :type text: str
    :return: list of all caracters in binarie
    :rtype: list
    
    :Example:
    >>> test_to_bin('hello')
    ['01101000', '01100101', '01101100', '01101100', '01101111']
    """
    list_cha_bin = []
    for char in text:
        char = format(ord(char), '08b')
        list_cha_bin.append(char)
    return list_cha_bin 

def bits_to_text(bin_list: list) -> str:
    """
    A função converte uma lista de valores binarios para uma string. Cada letra da string corresponde a um valor binário da lista

    :param bin_list: lista a ser desconvertida
    :type bin_list: list
    :return: string of all binarie numbers in list
    :rtype: str

    :Example:
    >>> bits_to_text(['01101000', '01100101', '01101100', '01101100', '01101111'])
    'hello'
    """
    text = ''
    for bin in bin_list:
        cha = chr(int(bin, 2))
        text += cha
    return text

def xor_bin_list(bin_msg: list, bin_key: list) -> list:
    """
    A função usa o operador XOR para misturar um caracter do texto com um valor da chave, até se obter uma nova lista com novos valores
    para cada caracter. Através da função também é possível obter a messagem original, através do texto encriptado e da chave.

    :param bin_msg: mensagem a ser encriptografada, uma lista com os caracteres em binário
    :type bin_msg: list
    :param bin_key: chave da encriptação, uam lista com o mesmo nº de valores que a mensagem
    :type bin_key: list
    :return: list off all mixed values, by order
    :rtype: list

    :Example:
        #message = 'hello'
    >>> bits_message = [01101000, 01100101, 01101100, 01101100, 01101111]
    >>> bits_key = [11111111, 11110001, 01101110, 10111101, 11101110]
    >>> cipher_text = xor_bin_list(bits_message, bits_key)
    >>> print(cipher_text)
    [10010111, 10010100, 00000010, 11010001, 10000001]
    """
    result = 0
    result_bin = 0
    list_result_bin = []

    for b1, b2 in zip(bin_msg, bin_key):
        result = int(b1, 2) ^ int(b2, 2)
        result_bin = format(result, '08b')
        list_result_bin.append(result_bin)
    return list_result_bin


if __name__ == '__main__':
    """
    Executa a cifra One-Time Pad (OTP). O programa solicita ao usuário uma mensagem secreta, 
    gera uma chave aleatória, criptografa e depois descriptografa a mensagem.

    :Program Flow:
    1. Solicita a mensagem secreta.
    2. Converte a mensagem para bits.
    3. Gera uma chave aleatória.
    4. Criptografa a mensagem usando XOR.
    5. Descriptografa a mensagem.
    6. Converte os bits de volta para texto e exibe a mensagem original.

    :Exemple:
        >>> python one_time_pad.py
        Insert your secret message:
            Hello
        Mensagem Original:    Hello
        Texto encriptado:     10011101 11011111 10111000 11111011 10100100
        Texto decifrado:      Hello
    """
    plain_text = input('Insert your secret message: \n\t')
    print(f'\n  Mensagem Original: \t{plain_text}')

    #convert to bits
    bits_key = random_key(len(plain_text))
    bits_text = text_to_bits(plain_text)
    print(f'  Bits da mensagem: \t{' '.join(bits_text)}')
    print(f'  Chave gerada: \t{' '.join(bits_key)}')

    #encriptar
    cipher_text = xor_bin_list(bits_text, bits_key)
    print(f'  Texto encriptado: \t{' '.join(cipher_text)}\n')

    #desencriptar
    decipher_text = xor_bin_list(cipher_text, bits_key)
    print(f'  Texto decifrado: \t{' '.join(decipher_text)}')

    #converter para texto
    message = bits_to_text(decipher_text)
    print(f'  Mensagem original: \t{message}')