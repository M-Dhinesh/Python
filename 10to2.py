def binToDec(dec):
    if dec==0:
        return ''
    return binToDec(dec//2)+str(dec%2)

print(binToDec(int(input("Enter n:"))))