

def translate(message):
    s = message.text
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    prev = values[s[0]]
    result = 0

    for c in s:
        current = values[c]
        # если значение очередного символа больше, чем значение предыдущего,
        # значит предыдущий должен был вычитаться.
        # Поскольку он до этого уже был прибавлен - вычитаю его в двойном объеме.
        if current > prev:
            result -= prev * 2

        result += current
        prev = current

    return result
