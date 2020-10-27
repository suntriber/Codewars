"""
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""

def main():
    print(count_bits(0), 0)
    print(count_bits(4), 1)
    print(count_bits(7), 3)
    print(count_bits(9), 2)
    print(count_bits(10), 2)
    
    

def count_bits(n):
    #num_bits = str(bin(n)[2:])
    #return len([bit for bit in str(num_bits) if bit == '1'])
    return len([bit for bit in str(bin(n)[2:]) if bit =='1'])

if __name__ == "__main__":
    main()