def main():
    print(int32_to_ip(2149583361))


def int32_to_ip(int32):
    tohex = hex(int32)[2:].zfill(8) 
    return f'{int(tohex[0:2],16)}.{int(tohex[2:4],16)}.{int(tohex[4:6],16)}.{int(tohex[6:8],16)}'
  

if __name__ == "__main__":
    main()