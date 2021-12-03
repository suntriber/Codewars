"""
Background information
The Hamming Code is used to correct errors, so-called bit flips, in data transmissions. Later in the description follows a detailed explanation of how it works.
In this Kata we will implement the Hamming Code with bit length 3; this has some advantages and disadvantages:

[ + ] It's simple to implement
[ + ] Compared to other versions of hamming code, we can correct more mistakes
[ - ] The size of the input triples
Task 1: Encode function
Implement the encode function, using the following steps:

convert every letter of the text to its ASCII value;
convert ASCII values to 8-bit binary;
triple every bit;
concatenate the result;
For example:

input: "hey"
--> 104, 101, 121                  // ASCII values
--> 01101000, 01100101, 01111001   // binary
--> 000111111000111000000000 000111111000000111000111 000111111111111000000111  // tripled
--> "000111111000111000000000000111111000000111000111000111111111111000000111"  // concatenated
Task 2: Decode function:
Check if any errors happened and correct them. Errors will be only bit flips, and not a loss of bits:

111 --> 101 : this can and will happen
111 --> 11 : this cannot happen
Note: the length of the input string is also always divisible by 24 so that you can convert it to an ASCII value.

Steps:

Split the input into groups of three characters;
Check if an error occurred: replace each group with the character that occurs most often, e.g. 010 --> 0, 110 --> 1, etc;
Take each group of 8 characters and convert that binary number;
Convert the binary values to decimal (ASCII);
Convert the ASCII values to characters and concatenate the result
For example:

input: "100111111000111001000010000111111000000111001111000111110110111000010111"
--> 100, 111, 111, 000, 111, 001, ...  // triples
-->  0,   1,   1,   0,   1,   0,  ...  // corrected bits
--> 01101000, 01100101, 01111001       // bytes
--> 104, 101, 121                      // ASCII values
--> "hey"
"""



def main():
    var = encode('h')

    
    print(decode(var))


def encode(string):
    # ret = ''
    # tmp = ''
    # for s in string:
    #     s = ord(s)
    #     s = bin(s)[2:].zfill(8)
    #     tmp += s
    # print('encoded string: ',tmp)
    
    # for i in range(len(tmp)):
    #     if tmp[i] == '0':
    #         ret += '000'
    #     else:
    #         ret += '111'
    # print('encoded string with added bits: ', ret)
    # return ret
    tmp = ''.join([bin(ord(s))[2:].zfill(8) for s in string])
    return ''.join([b+'11' if int(b) else b+'00' for b in tmp])


def decode(bits):
    # bit_split = []
    # bits_list = []
    # ascii_value = []
    # word = ''
    # tmp = ''

    # for i in range(0, len(bits), 3):
    #     tmp += bits[i]
    #     tmp += bits[i+1]
    #     tmp += bits[i+2]
    #     bit_split.append(tmp)
    #     tmp = ''

    # one, zero = 0, 0
    # for item in bit_split:
    #     if item[0] == '1':
    #         one += 1
    #     else:
    #         zero += 1
    #     if item[1] == '1':
    #         one += 1
    #     else:
    #         zero += 1
    #     if item[2] == '1':
    #         one += 1
    #     else:
    #         zero += 1
    #     if one > zero:
    #         bits_list.append('1')
    #     else:
    #         bits_list.append('0')
    #     one, zero = 0, 0
    
    # for i in range(0, len(bits_list), 8):
        
    #     tmp += bits_list[i]
    #     tmp += bits_list[i+1]
    #     tmp += bits_list[i+2]
    #     tmp += bits_list[i+3]
    #     tmp += bits_list[i+4]
    #     tmp += bits_list[i+5]
    #     tmp += bits_list[i+6]
    #     tmp += bits_list[i+7]
    #     ascii_value.append(tmp)
    #     tmp = ''
    
    # for item in ascii_value:
    #     item = int(item, 2)
    #     word += chr(item)
      
    # return word

    bit_split = [bits[i:i+3] for i in range(0, len(bits), 3)]
    bits_list = ''.join(['1' if i.count('1') >=2 else '0' for i in bit_split])       
    return ''.join([chr(int(bits_list[i:i+8], 2)) for i in range(0, len(bits_list), 8)])


    

if __name__ == "__main__":
    main()



# def encode(string):
#     return ''.join(map('{:08b}'.format, string.encode())).replace('0', '000').replace('1', '111')

# def decode(bits):
#     bytes_ = ('01'['11' in a+b+c+a] for a,b,c in zip(* [iter(bits)] * 3))
#     return bytes(int(''.join(b), 2) for b in zip(* [iter(bytes_)] * 8)).decode()


# def encode(uncoded):
#     encoded = ''.join(''.join(b * 3 for b in bin(ord(c))[2:].zfill(8)) for c in uncoded)
#     return encoded

# def decode(encoded):
#     patches = {'000':'0','001':'0','010':'0','100':'0','011':'1','101':'1','110':'1','111':'1'}
#     patched = ''.join(patches[encoded[i:i + 3]] for i in range(0, len(encoded), 3))
#     decoded = ''.join(chr(int(patched[i:i + 8], 2)) for i in range(0, len(patched), 8))
#     return decoded




# def encode(string):
#     values = "".join(format(x, "08b") for x in map(ord, string))
#     return values.replace("0", "000").replace("1", "111")


# def decode(bits):
#     bs = "".join("0" if xs.count("0") >= 2 else "1" for xs in zip(*[iter(bits)] * 3))
#     return "".join(chr(int("".join(b), 2)) for b in zip(*[iter(bs)] * 8))



# from re import sub,findall
# def encode(string):
#     return sub(r'(.)', r'\1\1\1',''.join(f'{ord(i):08b}' for i in string))

# def decode(bits):
#     return ''.join(chr(int(j,2)) for j in findall(r'.{8}',''.join(max(i,key=i.count) for i in findall(r'.{3}',bits))))