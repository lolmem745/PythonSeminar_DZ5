def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


text = 'AAAAAAAAAAAAAaaaaaaaaaaaaVVVVVVVVDDDDDDDDdaSSSSSd'
print(text)
data = rle_encode(text)
print(data)
decoded_text = rle_decode(data)
print(decoded_text)
