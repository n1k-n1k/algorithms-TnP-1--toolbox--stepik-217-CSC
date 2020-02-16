'''
Кодирование Хаффмана

По данной непустой строке s длины не более 10^4,
состоящей из строчных букв латинского алфавита,
постройте оптимальный беспрефиксный код.

В первой строке выведите количество различных букв k,
встречающихся в строке, и размер получившейся закодированной строки.
В следующих k строках запишите коды букв в формате "letter: code".
В последней строке выведите закодированную строку.

'''

'''
def hencode_old(st):
    ch_sorted = freq_list(st)
    st_code = dict()
    ch_len = len(ch_sorted)
    code = '0'

    st_code[ch_sorted[0]] = code
    if ch_len == 2:
        st_code[ch_sorted[1]] = '1'
    else:
        for c in ch_sorted[1:-2]:
            code = '1' + code
            st_code[c] = code
        st_code[ch_sorted[-2]] = code[:-1] + '10'
        st_code[ch_sorted[-1]] = code[:-1] + '11'
    return st_code
'''


def freq_dict(st, sort=True):
    st_freq = {c: st.count(c) for c in st}

    if not sort:
        return st_freq
    else:
        # dict sorted by values
        return dict(sorted(st_freq.items(),
                           key=lambda x: x[1], reverse=True))


def huffman_encode(st, ch_dict):
    return ''.join(ch_dict[c] for c in st)


def huffman_dict(st):
    ch_sort = freq_list(st)
    ch_len = len(ch_sort)
    ch_dict = dict()

    ch_dict[ch_sort[0]] = '0'
    if ch_len > 1:
        for i in range(1, ch_len - 1):
            ch_dict[ch_sort[i]] = '1' * i + '0'
        ch_dict[ch_sort[ch_len - 1]] = '1' * (ch_len - 2) + '1'

    return ch_dict


def freq_list(st):
    st_freq = {c: st.count(c) for c in st}
    return tuple(dict(sorted(st_freq.items(),
                             key=lambda x: x[1], reverse=True)).keys())


def test_output(st):
    h_dict = huffman_dict(st)

    print(freq_dict(st))
    print()
    print(freq_list(st))
    print()
    print(h_dict)

def main():
    st = 'accepted'
    # st = input()
    h_dict = huffman_dict(st)
    st_encoded = huffman_encode(st, h_dict)

    print(len(h_dict), len(st_encoded), sep=' ')
    for k, v in h_dict.items():
        print(k, v, sep=': ')
    print(st_encoded)


if __name__ == '__main__':
    test_output('accepted')
    #main()
