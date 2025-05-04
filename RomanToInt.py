class RomanInt():
    def __init__(self,strnum):
        
        self.s = strnum
    def output(self):
        
        x = self.s
        if not x:
            return ("Empty Roman numeral string")
        total_val = 0
        prev_val = 0
        roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        for y in reversed(x):
            if y not in roman:
                return(f"Invalid Roman numeral character: {y}")
            value = roman[y]
            if value < prev_val:
                total_val -= value
            else:
                total_val+=value
            prev_val = value
        return total_val

                  
n = RomanInt("")
print (n.output());

        