import string

def checkio(data: str) -> bool:

    #replace this for solution
    if len(data) < 10:
        return False
    #count upper,lower,digits
    i=u=l=d=0
    for i in range(len(data)):
        if data[i] in string.digits:
            d += 1
        if data[i] in string.ascii_uppercase:
            u += 1
        if data[i] in string.ascii_lowercase:
            l += 1
    if d>0 and u>0 and l>0:
        return True
    
    return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    password = input("input password: ")
    if checkio(password):
        print("Good Password")
    else:
        print("Bad Password")