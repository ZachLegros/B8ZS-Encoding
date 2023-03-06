def B8ZS_encode(msg):
    patterns = ['-+0+-', '+-0-+']
    last_polarity = 0
    consecutive_0s = 0
    result = ""
    for i in range(len(msg)):
        bit = msg[i]
        if bit == '1':
            consecutive_0s = 0
            last_polarity = not last_polarity
            result = result + ['-', '+'][last_polarity]
        elif bit == '0':
            consecutive_0s = consecutive_0s + 1
            if consecutive_0s == 8:
                result = result[:i-4] + patterns[last_polarity]
                consecutive_0s = 0
            else:
                result = result + '0'
        else:
            raise("Invalid message.")
    return result


def B8ZS_decode(msg):
    patterns = ['-+0+-', '+-0-+']
    result = ""
    i = 0
    while(i < len(msg)):
        if msg[i:i+5] in patterns:
            result = result + '00000'
            i = i + 5
        else:
            bit = msg[i]
            result = result + ('1' if bit != '0' else '0')
            i = i + 1
    return result


def validate_message(msg):
    is_valid = True
    for bit in msg:
        if bit != '0' and bit != '1':
            is_valid = False
            break
    return is_valid


if __name__ == "__main__":
    inputs = ["100000000", "100000000000100", "1100000000110000010", "1101001"]
    outputs = ["+000+-0-+", "+000+-0-+000-00", "+-000-+0+-+-00000+0", "+-0+00-"]

    for i, o in zip(inputs, outputs):
        if B8ZS_encode(i) == o:
            print(f"PASS ENCODE: {i}")
        else:
            print(f"FAILED ENCODE: {i}")
        if B8ZS_decode(B8ZS_encode(i)) == i:
            print(f"PASS DECODE: {o}")
        else:
            print(f"FAILED DECODE: {o}")
