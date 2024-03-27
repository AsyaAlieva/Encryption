# Произвести шифрование произвольной фразы следующими тремя методами:
# Шифр Цезаря,гаммирование по модулю 2, DES

def func1(words, position): #Шифр Цезаря
    answer = []
    for i in words:
        num_before = ord(i)
        num_after = 0
        if i.isalpha(): #условие, чтобы не затрагивать ничего, кроме букв
            if num_before >= ord('А') and num_before <= ord('Я'):
                num_after = ((num_before - ord('А') + position) % 32) + ord('А')
            elif num_before >= ord('а') and num_before <= ord('я'):
                num_after = ((num_before - ord('а') + position) % 32) + ord('а')
            elif num_before >= ord('A') and num_before <= ord('Z'):
                num_after = ((num_before - ord('A') + position) % 26) + ord('A')
            elif num_before >= ord('a') and num_before <= ord('z'):
                num_after = ((num_before - ord('a') + position) % 26) + ord('a')
        else:
            num_after = num_before
        letter_after = chr(num_after)
        answer.append(letter_after)
    print(f"Зашифрованный текст: {''.join(answer)}")

# phrase = input("Введите фразу для шифрования: ")
# position = int(input("Введите шаг сдвига: "))
# func1(phrase, position)
############################################################################################
############################################################################################

def gamma_module_2(words, key): #гаммирование по модулю 2
    symbols = list(words)
    key_symbols = list(key)
    answer = []

    for j in key_symbols:
        if len(key_symbols) < len(symbols):
            key_symbols.append(j)

    list_bin = []
    for s1, s2 in zip(symbols, key_symbols): #проходимся по спискам, и переводим каждый символ в двоичную систему


        ord_s1 = ord(s1)
        ord_s2 = ord(s2)

        bin_s1 = bin(ord_s1).replace("0b", "")
        bin_s2 = bin(ord_s2).replace("0b", "")
        zero = '0'

        while len(bin_s1) < 8:
            bin_s1 = zero + bin_s1

        while len(bin_s2) < 8:
            bin_s2 = zero + bin_s2

        temp = ''
        for bs1, bs2 in zip(bin_s1, bin_s2): #цикл для того чтобы с двоичным кодом каждого символа провести операцию XOR
            if bs1 == bs2:
                temp += '0'
            else:
                temp += '1'


        list_bin.append(temp)
    for el in list_bin: #переводим числа из двоичной системы (полученных при шифровании) в символы
        decimal_number = int(el, 2)

        if decimal_number < ord('A'):
            num_after = ((decimal_number + ord('A')) % 26) + ord('A')
        elif decimal_number > ord('Z'):
            num_after = ((decimal_number + ord('Z')) % 26) + ord('Z') #!!
        elif decimal_number < ord('a'):
            num_after = ((decimal_number + ord('a')) % 26) + ord('a')
        elif decimal_number > ord('z'):
            num_after = ((decimal_number + ord('z')) % 26) + ord('z') #!!
        else:
            num_after = decimal_number

        answer.append(chr(num_after))

    print(''.join(answer))


phrase = input("Введите фразу для шифрования: ")
key = input("Введите ключ: ")
gamma_module_2(phrase, key)

def des(words): #DES
    matrix_start_replace = [
        [58, 50, 42, 34, 26, 18, 10, 2],
        [60, 52, 44, 36, 28, 20, 12, 4],
        [62, 54, 46, 38, 30, 22, 14, 6],
        [64, 56, 48, 40, 32, 24, 16, 8],
        [57, 49, 41, 33, 25, 17, 9, 1],
        [59, 51, 43, 35, 27, 19, 11, 3],
        [61, 53, 45, 37, 29, 21, 13, 5],
        [63, 55, 47, 39, 31, 23, 15, 7]
    ]

    matrix_end_replace = [
        [40, 8, 48, 16, 56, 24, 64, 32],
        [39, 7, 47, 15, 55, 23, 63, 31],
        [38, 6, 46, 14, 54, 22, 62, 30],
        [37, 5, 45, 13, 53, 21, 61, 21],
        [36, 4, 44, 12, 52, 20, 60, 28],
        [35, 3, 43, 11, 51, 19, 59, 27],
        [34, 2, 42, 10, 50, 18, 58, 26],
        [33, 1, 41, 9, 49, 17, 57, 25]
    ]

# num_before >= ord('A') and num_before <= ord('Z'):
# num_after = ((num_before - ord('A') + position) % 26) + ord('A')
# num_before >= ord('a') and num_before <= ord('z'):
# num_after = ((num_before - ord('a') + position) % 26) + ord('a')
