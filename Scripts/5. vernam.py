"""
Cifra de Vernam - Criptografia com XOR

Este programa implementa a cifra de Vernam utilizando a operação XOR. Ele recebe um texto e uma chave, realizando a criptografia e retornando os resultados em três formatos: Unicode, Binário e Hexadecimal.

:Program Flow:
1. O usuário fornece o texto e a chave.
2. O texto e a chave são convertidos para representações Unicode.
3. A operação XOR é aplicada entre os caracteres do texto e da chave, gerando o texto cifrado.
4. O texto cifrado é formatado em três representações: Unicode, Binário e Hexadecimal.
5. Os resultados são exibidos ao usuário.

:Practical Examples:
1. Criptografar a mensagem:
    - Texto: "ESTAMOS NA AULA DE CRIPTOGRAFIA"
    - Chave: "ESTOU A UTILIZAR UMA CHAVE ALEATÓRIA PARA A CIFRA DE VERNAM"
    - Resultado da operação XOR (em três formatos):
            Unicode: [123, 104, 110, ...]
            Representação oficial: ['\x7b', '\x68', '\x6e', ...]
            Binário: ['01111011', '01101000', '01101110', ...]
            Hexadecimal: ['0x7b', '0x68', '0x6e', ...]

:Note: A operação XOR é simétrica, o que significa que o texto pode ser cifrado e decifrado utilizando a mesma chave.
"""

text = 'ESTAMOS NA AULA DE CRIPTOGRAFIA'
key = 'ESTOU A UTILIZAR UMA CHAVE ALEATÓRIA PARA A CIFRA DE VERNAM'

def text_to_unicode(text: str, preserve_not_alpha: bool) -> list:
    """
    Converte o texto em uma lista de valores Unicode. Caracteres não alfabéticos podem ser preservados 
    dependendo do parâmetro preserve_not_alpha.
    
    :param text: Texto a ser convertido.
    :type text: str
    :param preserve_not_alpha: Indica se os caracteres não alfabéticos devem ser preservados
    :type preserve_not_alpha: bool
    
    :return: Retorna uma lista de valores Unicode. Se preserve_not_alpha for verdadeiro, caracteres não alfabéticos são mantidos.
    :rtype: list

    :Example:
    >>> text_to_unicode("OLA!", True)
    [79, 76, 65, '!']
    >>> text_to_unicode("OLA!", False)
    [79, 76, 65]
    """
    list_cha_unicode = []
    for cha in text:
        if cha.isalpha():
            list_cha_unicode.append(ord(cha))
        elif preserve_not_alpha:
            list_cha_unicode.append(cha)

    return list_cha_unicode

def xor_operator(text: str, key: str) -> list:
    """
    Realiza a operação XOR entre os caracteres do texto e os valores da chave, gerando uma lista cifrada.
    Para descriptografar, basta aplicar a operação XOR novamente com o mesmo texto cifrado e a mesma chave.

    :param text: Texto a ser cifrado/desifrado.
    :type text: str
    :param key: Chave utilizada na cifragem.
    :type key: str

    :return: Retorna uma lista com os valores Unicode resultantes da operação XOR entre o texto e a chave.
    :rtype: list

    :Example:
    >>> cipher_text = xor_operator("ESTAMOS NA AULA", "ola")
    >>> print(cipher_text)
    [42, 63, 53, 46, 33, 46, 60, ' ', 34, 32, ' ', 46, 57, 45, 46] 
    """
    uni_text = text_to_unicode(text, True)
    uni_key = text_to_unicode(key, False)
    index_key = 0
    cipher_text = []
    for value in uni_text:
        if isinstance(value, int):
            letter_xor = value ^ uni_key[index_key%len(uni_key)]
            cipher_text.append(letter_xor)
            index_key += 1
        else:
            cipher_text.append(value)
    return cipher_text

def format_cipher(cipher_text: list) -> list:
    """
    Converte o texto cifrado em três formatos diferentes: representação oficial, binário e hexadecimal.
    
    :param cipher_text: Lista de valores resultantes da operação XOR.
    :type cipher_text: list

    :return: Retorna uma tupla contendo três listas:
                1. Representação oficial (valores Unicode representados como strings).
                2. Binário (valores binários de 8 bits).
                3. Hexadecimal (valores hexadecimais).
    :rtype: list

    :Example:
    >>> official, binary, hexadecimal = format_cipher([42, 63, 53, 46, 33, 46, 60, ' ', 34, 32, ' ', 46, 57, 45, 46])
    >>> print(official)
    ["'*'", "'?'", "'5'", "'.'", "'!'", "'.'", "'<'", ' ', '\'"\'', "' '", ' ', "'.'", "'9'", "'-'", "'.'"]
    >>> print(binary)
    ['00101010', '00111111', '00110101', '00101110', '00100001', '00101110', '00111100', ' ', '00100010', '00100000', ' ', '00101110', '00111001', '00101101', '00101110']
    >>> print(hexadecimal)
    ['0x2a', '0x3f', '0x35', '0x2e', '0x21', '0x2e', '0x3c', ' ', '0x22', '0x20', ' ', '0x2e', '0x39', '0x2d', '0x2e']
    """
    official = []
    binary = []
    hexadecimal = []
    for value in cipher_text:
        if isinstance(value, int):
            official.append(repr(chr(value)))
            binary.append(format(value, '08b'))
            hexadecimal.append(hex(value))
        else:
            official.append(value)
            binary.append(value)
            hexadecimal.append(value)


    return official, binary, hexadecimal


if __name__ == '__main__':
    """
    O programa executa o processo completo da cifra de Vernam, criptografando um texto utilizando uma chave e,
    em seguida, exibindo os resultados em diferentes formatos.

    :Program Flow:
    1. A função xor_operator() é chamada para cifrar o texto (text) utilizando a chave (key).
    2. A função format_cipher() é chamada para converter o texto cifrado em três formatos:
        - Unicode
        - Representação oficial
        - Binário
        - Hexadecimal
    3. O resultado é exibido na tela, mostrando os três formatos de saída.
    """
    cipher_text = xor_operator(text, key)

    official, binary, hexadecimal = format_cipher(cipher_text)
        
    print(f"""RESULTADO\n
    Unicode: {cipher_text}\n
    Representação oficial: {official}\n
    Binário: {binary}\n
    Hexadecimal: {hexadecimal}""")