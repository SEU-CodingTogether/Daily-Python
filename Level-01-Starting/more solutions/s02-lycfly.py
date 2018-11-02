def checkio(data: str) -> str:
    maxnum = 0
    max =''
    l = {}
    for i in data:
        if i.isalpha():              #判断是否为字母
            i = i.lower()            #改为小写
            if not l.__contains__(i):#将字母以及其频次存为字典
                l[i] = 1
            else:
                l[i] += 1
            if l[i] > maxnum:        #判断字母的频次以及字母ASCII值
                maxnum = l[i]
                max = i
            elif ord(i)<ord(max) and l[i] == maxnum:
                max = i
    return max
     

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "1st example"
    assert checkio("How do you do?") == "o", "2nd example"
    assert checkio("One") == "e", "3rd example"
    assert checkio("Oops!") == "o", "4th example"
    assert checkio("AAaooo!!!!") == "a", "5th example"
    assert checkio("abe") == "a", "6th example"
print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
