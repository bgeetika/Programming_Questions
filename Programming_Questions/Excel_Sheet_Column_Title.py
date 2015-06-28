
n = 26

def convert_base(n, base):
    n = n-1
    lis = []
    while True:
        q = n/base
        rem = n % base
        n = q - 1
        lis = [rem] + lis
        if q == 0:
            break
    return lis

def convert_char(n):
            return chr(ord('a')+n)

def convertToTitle(n):
        output = convert_base(n,26)
        l = []
        for x in output:
            l = l + [convert_char(int(x))]
        return l

            
print convertToTitle(n)



#print convert_base(729,26)
