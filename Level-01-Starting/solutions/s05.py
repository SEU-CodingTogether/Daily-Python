def checkio(data):
    value_int=[1000,900,500,400,100,90,50,40,10,9,5,4,1];
    value_roman=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    ret="";
    temp=data;
    for i in range(len(value_int)):
        j=0;
        j=int(temp/value_int[i]);
        temp=temp-value_int[i]*j;
        for k in range(j):
            ret=ret+value_roman[i];
    #replace this for solution
    return ret

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')