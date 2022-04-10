def karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y

    split_len = max(len(str(x)), len(str(y))) // 2

    x_len = len(str(x))
    y_len = len(str(y))

    x_0 = int(str(x)[:x_len - split_len])
    x_1 = int(str(x)[x_len - split_len:])
    y_0 = int(str(y)[:y_len - split_len])
    y_1 = int(str(y)[y_len - split_len:])

    m_0 = karatsuba(x_0, y_0)
    m_1 = karatsuba(x_1, y_1)
    m_2 = karatsuba(x_0 + x_1, y_0 + y_1)

    return (m_0 * 10**(2 * split_len)
            + ((m_2 - m_0 - m_1) * 10**split_len) + m_1)
