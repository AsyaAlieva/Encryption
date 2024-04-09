# Произвести шифрование произвольной фразы следующими тремя методами:
# Шифр Цезаря,гаммирование по модулю 2, DES

def interface():
    print("\nМеню")
    print("---------------------------")
    print("1. Шифр Цезаря")
    print("2. Гаммирование по модулю 2")
    print("3. DES")
    print("4. Выход")
    print("---------------------------")
    print("Выберите метод шифрования: ")
    item = int(input())

    if item == 1:
        method_choice(item)
    elif item == 2:
        method_choice(item)
    elif item == 3:
        method_choice(item)
    elif item == 4:
        return

def method_choice(item):
    if item == 1:
        phrase = input("Введите фразу для шифрования: ")
        position = int(input("Введите шаг сдвига: "))
        caesar_cipher(phrase, position)
    elif item == 2:
        phrase = input("Введите фразу для шифрования: ")
        key = input("Введите ключ: ")
        gamma_module_2(phrase, key)
    elif item == 3:
        des_key = b'x13x34x57x79x9BxBCxDFxF1'
        text = input("Введите шифруемый текст: ")
        print(des(text, des_key))

def caesar_cipher(words, position): #Шифр Цезаря
    answer = []
    for i in words:
        num_before = ord(i)
        num_after = 0
        if i.isalpha(): #условие, чтобы не затрагивать ничего, кроме букв (русских и английских)
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


def gamma_module_2(words, key): #гаммирование по модулю 2
    symbols = list(words)
    key_symbols = list(key)
    answer = []

    for j in key_symbols: #уравниваем длину ключа и длину текста
        if len(key_symbols) < len(symbols):
            key_symbols.append(j)

    list_bin = []
    for s1, s2 in zip(symbols, key_symbols): #проходимся по спискам, и переводим каждый символ в двоичную систему

        ord_s1 = ord(s1) #переводим в кодировку аски
        ord_s2 = ord(s2)

        bin_s1 = bin(ord_s1).replace("0b", "")
        bin_s2 = bin(ord_s2).replace("0b", "")
        zero = '0'

        while len(bin_s1) < 8: #приписываем в начало нули, если длина двоичного кода меньше 8 (для символа текста)
            bin_s1 = zero + bin_s1

        while len(bin_s2) < 8: #приписываем в начало нули, если длина двоичного кода меньше 8 (для символа ключа)
            bin_s2 = zero + bin_s2

        temp = ''
        for bs1, bs2 in zip(bin_s1, bin_s2): #цикл для того чтобы с двоичным кодом каждого символа провести операцию XOR
            if bs1 == bs2:
                temp += '0'
            else:
                temp += '1'

        list_bin.append(temp) #добавляем двоичный код после операции XOR будущего символа
    for el in list_bin: #переводим числа из двоичной системы (полученных при шифровании) в символы
        decimal_number = int(el, 2)

        if words == words.upper() and key == key.upper(): #условия для нахождения в пределах англ. алфавита
            if decimal_number < ord('A'):
                num_after = ((decimal_number + ord('A')) % 26) + ord('A')
            elif decimal_number > ord('Z'):
                num_after = ((decimal_number + ord('Z')) % 26) + ord('Z')
            else:
                num_after = decimal_number
        elif words == words.lower() and key == key.lower():
            if decimal_number < ord('a'):
                num_after = ((decimal_number + ord('a')) % 26) + ord('a')
            elif decimal_number > ord('z'):
                num_after = ((decimal_number + ord('z')) % 26) + ord('z')
            else:
                num_after = decimal_number

        answer.append(chr(num_after)) #формирование ответа

    print(''.join(answer))


def des(text, des_key): # DES

    # Начальная перестановка
    initial_permutation = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]

    R1_X1 = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1
    ]

    # Конечная перестановка
    inverse_permutation = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 21,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]

    sub_box = [

        [
            14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
            0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
            4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
            15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
        ],
        [
            15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
            3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
            0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
            13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
        ],
        [
            10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
            13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
            13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
            1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
        ],
        [
            7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
            13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
            10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
            3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
        ],
        [
            2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
            14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
            4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
            11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
        ],
        [
            12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
            10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
            9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
            4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
        ],
        [
            4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
            13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
            1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
            6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
        ],
        [
            13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
            1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
            7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
            2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
        ]
    ]

    # Перестановка блока H1
    permutation = [
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25
    ]

    # Генерирование ключевых элементов
    generating_key_elements = [
        57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
    ]

    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    # Перестановка сжатия
    compression_swap = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]

    # Начинаем решать непосредственно саму задачу
    def permute(key, permutation):
        return [key[p - 1] for p in permutation]

    # функция выполнения циклического сдвига битов
    def left_shift(bits, shift):
        return bits[shift:] + bits[:shift]

    # генерация раундовых ключей на основе основного ключа шифрования
    def key_schedule(key):
        # Преобразуем ключ в список 64 битов
        key_bits = [int(b) for b in format(int.from_bytes(key, byteorder='big'), '064b')]

        # Первоначальная перестановка ключа PC1
        permuted_key = permute(key_bits, generating_key_elements)

        # Делим переставленный ключ на левую и правую части
        C = permuted_key[:28]
        D = permuted_key[28:]

        round_keys = []

        for i in range(16):
            # Левый сдвиг C и D
            C = left_shift(C, shifts[i])
            D = left_shift(D, shifts[i])

            # Объединение C и D
            CD = C + D

            # Перестановка PC-2
            round_key = permute(CD, compression_swap)
            round_keys.append(round_key)

        # Преобразование обратно в байты
        round_keys_bytes = [int(''.join(map(str, k)), 2).to_bytes(6, byteorder='big') for k in round_keys]

        return round_keys_bytes

    # преобразование шифруемого текста в двоичный код
    def text_to_binary_64bit(text):
        binary_string = ''
        for char in text:
            binary_char = format(ord(char), '08b')  # Преобразуем символ в двоичную строку длиной 8 бит
            binary_string += binary_char
        return binary_string[:64]  # Возвращаем только первые 64 бита


    # text = input("Введите шифруемый текст: ")
    T = text_to_binary_64bit(text)
    T_new = ''

    # Начальная перестановка блока T
    for j in initial_permutation:
        T_new += T[j-1]

    L = T_new[:32]
    R = T_new[32:]

    # Здесь реализуется сеть Фейсталя (16 раундов)
    for i in range(16):
        X1 = ''
        for l in R1_X1:
            X1 += R[l-1]

        # Генерация ключа и его двоичное представление полученное из байтового
        byte_string_key = key_schedule(des_key)[i] #передаем значение ключа в зависимости от итерации i
        K1 = ''.join([bin(byte)[2:].zfill(8) for byte in byte_string_key])

        H1 = ''
        # Гаммирование по модулю 2 (операция XOR)
        for j in range(len(X1)):
            H1_part = int(K1[j]) ^ int(X1[j])
            H1 += str(H1_part)

        b_dict = {'00': 0, '01': 1, '10': 2, '11': 3}

        count = 0
        intermediate_result = []  # здесь будем собирать ответ в 10-ой системе счисления
        for m in range(0, len(H1), 6):
            row = H1[m] + H1[m+5]
            b1b6 = b_dict[row] # получаем номер строки
            b2b3b4b5 = int(H1[m+1:m+5], 2) # получаем номер столбца
            index = 16 * b1b6 + b2b3b4b5 # находим индекс нужного элемента/числа
            intermediate_result.append(sub_box[count][index]) # добавляем ответ в список проходясь по матрице sub_box
            count += 1

        # здесь полученный ответ будет храниться в двоичной системе счисления (32 бита)
        H1_new = ''.join([bin(byte)[2:].zfill(4) for byte in intermediate_result])

        H2 = ''
        for q in permutation:
            H2 += H1_new[q - 1]

        # Гаммирование по модулю 2 (операция XOR)
        R2 = ''
        for p in range(len(L)):
            R2_part = int(L[p]) ^ int(H2[p])
            R2 += str(R2_part)
        L2 = R

        L = L2
        R = R2

    T_last = L + R
    C = ''
    for k in inverse_permutation: # выполняем конечную перестановку
        C += T_last[k-1]

    # Превращаем двоичный код в текст (это будет зашифрованный текст)
    text_output = ''
    # Проходим по строке с шагом в 8 бит (1 байт)
    for i in range(0, len(C), 8):
        # Берем очередные 8 бит и преобразуем в десятичное число
        byte = C[i:i + 8]
        decimal_value = int(byte, 2)

        # Опрделяем границы, чтобы ответ состоял исключительно из символов английского алфавита
        if decimal_value < ord('a'):
            num_after = ((decimal_value + ord('a')) % 26) + ord('a')
        elif decimal_value > ord('z'):
            num_after = (ord('z') - (decimal_value + ord('z')) % 26 + 1)
        else:
            num_after = decimal_value

        # Конвертируем десятичное число в символ по ASCII
        character = chr(num_after)
        text_output += character

    return text_output


if __name__ == "__main__":
    interface()