def main():
    var = encode('hey hey HALLO there!!')
    print(decode(var))


def encode(string):
    ret = ''
    tmp = ''
    for s in string:
        s = ord(s)
        s = bin(s)[2:].zfill(8)
        tmp += s
    print('encoded string: ',tmp)
    for i in range(len(tmp)):
        if tmp[i] == '0':
            ret += '000'
        else:
            ret += '111'
    print('encoded string with added bits: ', ret)
    return ret


def decode(bits):
    bit_split = []
    bits_list = []
    ascii_value = []
    word = ''
    tmp = ''

    for i in range(0, len(bits), 3):
        tmp += bits[i]
        tmp += bits[i+1]
        tmp += bits[i+2]
        bit_split.append(tmp)
        tmp = ''

    one, zero = 0, 0
    for item in bit_split:
        if item[0] == '1':
            one += 1
        else:
            zero += 1
        if item[1] == '1':
            one += 1
        else:
            zero += 1
        if item[2] == '1':
            one += 1
        else:
            zero += 1
        if one > zero:
            bits_list.append('1')
        else:
            bits_list.append('0')
        one, zero = 0, 0
    
    for i in range(0, len(bits_list), 8):
        
        tmp += bits_list[i]
        tmp += bits_list[i+1]
        tmp += bits_list[i+2]
        tmp += bits_list[i+3]
        tmp += bits_list[i+4]
        tmp += bits_list[i+5]
        tmp += bits_list[i+6]
        tmp += bits_list[i+7]
        ascii_value.append(tmp)
        tmp = ''
    
    for item in ascii_value:
        item = int(item, 2)
        word += chr(item)
      
    return word           

    

if __name__ == "__main__":
    main()