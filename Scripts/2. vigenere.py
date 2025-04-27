"""
CIFRA DE VIGÉNERE - Criptografia e Descriptografia

Este script implementa a cifra de Vigenère, uma técnica de criptografia simétrica que usa uma 
chave alfabética para criptografar e descriptografar textos. Cada letra do texto é deslocada de 
acordo com a posição da letra correspondente da chave.

:Program Flow:
1. O usuário escolhe entre criptografar ou descriptografar um texto.
2. O usuário insere a mensagem que deseja criptografar/descriptografar.
3. O usuário fornece uma chave de segurança (alfabética).
4. A função converte o texto e a chave em unicode e aplica a cifra de Vigenère com a chave fornecida.
5. O programa retorna a representação do texto original e da chave em unicode, e o texto criptografado/descriptografado.

:Functions:
- text_to_unicode(text: str, preserve_symbols: bool) -> list
    Converte o texto para uma lista de valores Unicode, preservando caracteres não alfabéticos, se solicitado.
- vigenere_cipher(text_to: str, key: str, to_do: str) -> dict
    Aplica a cifra de Vigenère ao texto fornecido, usando a chave para criptografar ou descriptografar.

:Practical Examples:
1. Criptografar mensagem:
   - Mensagem: "OLA MUNDO!"
   - Chave: "SIM"
   - Resultado: "GTM ECZVW!"

2. Descriptografar mensagem:
   - Mensagem: "GTM ECZVW!"
   - Chave: "SIM"
   - Resultado: "OLA MUNDO!"

:Note: A chave deve ser composta apenas por letras do alfabeto. Qualquer caractere não alfabético na mensagem será preservado.
"""

def text_to_unicode(text: str, preserve_symbols: bool) -> list:
    """
    Converte o texto para uma lista de valores Unicode, preservando caracteres não alfabéticos, 
    se o parâmetro `preserve_symbols` for verdadeiro.
    
    :param text: Texto a ser convertido.
    :type text: str
    :param preserve_symbols: Indica se caracteres não alfabéticos devem ser preservados.
    :type preserve_symbols: bool

    :return: Lista de valores Unicode dos caracteres alfabéticos e preservação dos não alfabéticos.
    :rtype: list

    :Example:
    >>> text_to_unicode("OLA!", True)
    [79, 76, 65, ' ']
    >>> text_to_unicode("OLA!", False)
    [79, 76, 65]
    """
    list_cha_unicode = []
    for cha in text:
        if cha.isalpha():
            list_cha_unicode.append(ord(cha))
        elif preserve_symbols:
            list_cha_unicode.append(cha)

    return list_cha_unicode

def vigenere_cipher(text_to: str, key: str, to_do: str) -> dict:
    """
    Aplica a cifra de Vigenère ao texto fornecido, usando a chave para criptografar ou descriptografar.
    
    :param text_to: Texto a ser criptografado ou descriptografado.
    :type text_to: str
    :param key: Chave alfabética usada para a cifra de Vigenère.
    :type key: str
    :param to_do: Ação a ser realizada ('crip' para criptografar, 'decr' para descriptografar).
    :type to_do: str

    :return: Dicionário contendo o texto original em unicode, a chave em unicode e o resultado da operação.
    :rtype: dict

    :Example:
    >>> vigenere_cipher("OLA MUNDO", "SIM", "crip")
    {'unicode_text': [79, 76, 65, 32, 77, 85, 78, 68, 79], 'unicode_key': [83, 73, 77], 'result': 'GTM ECZVW!'}
    >>> vigenere_cipher("GTM ECZVW", "SIM", "decr")
    {'unicode_text': [71, 84, 77, 32, 69, 67, 90, 87], 'unicode_key': [83, 73, 77], 'result': 'OLA MUNDO!'}
    """
    uni_text = text_to_unicode(text_to, True)
    uni_key = text_to_unicode(key, False)

    result_text = ''
    index_key = 0

    for value in uni_text:
        if isinstance(value, int):
            letter_text = value - 65
            letter_key = uni_key[index_key%len(uni_key)] - 65

            if to_do == 'crip':
                letter_result = (letter_text + letter_key) % 26 + 65
            elif to_do == 'decr':
                letter_result = (letter_text - letter_key + 26) % 26 + 65
            result_text += chr(letter_result)
            index_key += 1
        else:
            result_text += value
    return {
        'unicode_text': uni_text,
        'unicode_key': uni_key,
        'result': result_text}

if __name__ == '__main__':
    """
    Executa o sistema de cifragem, permitindo que o usuário escolha entre criptografar ou descriptografar uma mensagem.

    O programa oferece as seguintes opções ao usuário:
    1. Criptografar mensagem
    2. Descriptografar mensagem
    3. Sair

    O programa solicita uma chave (alfabética) e a mensagem a ser cifrada ou decifrada.
    """
    while True:
        print('\nBEM VINDO AO SISTEMA QUE UTILIZA: CIFRA DE VIGÉNERE')
        print('\t1. Criptografar mensagem')
        print('\t2. Descriptografar mensagem')
        print('\t3. Sair')
        choice = input('O que deseja fazer? ')
        print()

        if choice in '12':
            print('CRIPTOGRAFAR' if choice == '1' else 'DESCRIPTOGRAFAR')
            print('Introduza a mensagem e a chave de segurança')
            orig_text = input('\tMensagem: ').upper()
            key = input('\tChave: ').upper()
        
            res = vigenere_cipher(orig_text, key, 'crip' if choice == '1' else 'decr')
            print(f"""
Mensagem Inicial: \t\t{orig_text}
Representação em unicode: \t{res['unicode_text']}
Chave Usada: \t\t\t{key}
Representação em unicode: \t{res['unicode_key']}
Resultado: \t\t\t{res['result']}""")
            
        else:
            break