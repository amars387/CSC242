#Anthony Marsilio
#HW5
#Collabed with Shaan Barkat
def pascalLine(a):
    if a == 0:
        return [1]
    else:
        prev = pascalLine(a-1)
        lst = [1]
        for i in range(len(prev)-1):
            lst.append(prev[i] + prev[i+1])
        lst.append(1)
    return lst
def levy(a):
    if a == 0:
        return "F"
    else:
        turns = levy(a-1)
        return turns.replace("F", "LFRRFL")
def base(a,b):
    if a < b:
        return str(a)
    else:
        return base(a//b,b)+ str(a%b)

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw5TEST.py' ))
