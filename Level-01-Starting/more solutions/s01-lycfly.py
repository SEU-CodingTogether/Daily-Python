def checkio(data: str) -> bool:
    determine = [0, 0, 0]
    for i in range(len(data)):
        if ord(data[i]) in range(48, 58):determine[0] = 1
        elif ord(data[i]) in range(65, 91):determine[1] = 1
        elif ord(data[i]) in range(97, 123):determine[2] = 1
        if determine == [1, 1, 1]:
            return not (len(data) < 10)
    return False


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
