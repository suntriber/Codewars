"""
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Examples
ips_between("10.0.0.0", "10.0.0.50")  ==   50 
ips_between("10.0.0.0", "10.0.1.0")   ==  256 
ips_between("20.0.0.10", "20.0.1.0")  ==  246
"""

def main():
    print(ips_between("10.0.0.0", "10.0.0.50"), 50)
    print(ips_between("20.0.0.10", "20.0.1.0"), 246)


def ips_between(start, end):
    # strings to lists with integers
    start, end = [int(x) for x in start.split('.')], list(map(int, end.split('.')))
    return ((end[0] - start[0]) *256**3) + ((end[1] - start[1]) *256**2) + ((end[2] - start[2]) *255) + (end[3] - start[3])


if __name__ == "__main__":
    main()
