'''
    Утверждения вызывают для проверки правильности кода
    если она возвращает false, то вызывается исключение

    (!) Утверждения можно использовать, скажем, для про
    верки правильности ввода или вывода

    (!) Если не перехватывать assert, как try/except,то
    класс приведет к падению программы
'''
assert 3 == 3
print(3)
assert 4 == 0, "Четыре не есть ноль"
print("sudo")
