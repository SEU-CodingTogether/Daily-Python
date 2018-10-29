class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num > 3999 or num < 1 :
            return ""
        str = ""
        while num :
            if num >= 1000:
                str = str+ "M"
                num=  num -1000
                continue
            if num >= 900:
                str = str+ "CM"
                num=  num -900
                continue
            if num >= 500:
                str = str+ "D"
                num=  num -500
                continue
            if num >= 400:
                str = str+ "CD"
                num=  num -400
                continue
            if num >= 100:
                str = str+ "C"
                num=  num -100
                continue
            if num >= 90:
                str = str+ "XC"
                num=  num -90
                continue
            if num >= 50:
                str = str+ "L"
                num=  num -50
                continue
            if num >= 40:
                str = str+ "XL"
                num=  num -40
                continue
            if num >= 10:
                str = str+ "X"
                num=  num -10
                continue
            if num >= 9:
                str = str+ "IX"
                num=  num -9
                continue
            if num >= 5:
                str = str+ "V"
                num=  num -5
                continue
            if num >= 4:
                str = str+ "IV"
                num=  num -4
                continue
            if num >= 1:
                str = str+ "I"
                num=  num -1
                continue
        return str