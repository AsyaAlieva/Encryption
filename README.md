# Алгоритмы шифрования
Производится шифрование произвольной фразы следующими тремя методами:
1. Шифр Цезаря
На вход подаются текст {words}, который необходимо зашифровать и шаг сдвига {position}, 
с помощью которого и шифруется текст.
2. Гаммирование по модулю 2
На вход подаются текст {words}, который необходимо зашифровать 
и ключ в виде символов {key}, с помощью которого и шифруется текст.
3. DES
На вход подаются текст {text}, состоящий из 8 символов (8 байт) и 
8-байтовый ключ {des_key}.

Все входные данные вводятся пользователем, за исключением 8-байтового ключа {des_key}.
Он заранее задан внутри кода (для удобства)