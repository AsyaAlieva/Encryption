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


phrase = input("Введите фразу для шифрования: ")
key = input("Введите ключ: ")
gamma_module_2(phrase, key)