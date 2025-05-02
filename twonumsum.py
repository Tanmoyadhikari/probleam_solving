"""
It is a system like broutforce for matching a target number by additioning [0,1],[0,2],[0,3]....[x,y] => [x+y] == check
1.  Define a condition  for get oparation status after compleating fully.
2. make a array [2,3,4] which we use for broutforce.
3.set z = target_number.
4. make a nested loop like.
                    [2,3]   [2,4]   [3,2]   [3,4]   [4,3]   [4,4]
-> in inner loop -> Try adding the innter matrix element the two number & match the target number .. 
5. If matched show the value and index position , else show a message 'Not Matched'


#Testing Instance ...
    defining a object -->    test1 = Twonum(21)


    calling the object-->    print(test1.test())

"""
class Twonum():
    # def __init__(self,numb):
    #     self.num = numb
    # def test(self):
    #     condition = True
    #     initval = [1,2,3,4,20]
    #     y=0 
    #     z = self.num
    #     for x in initval:
    #         inity = 0
    #         for v in initval:
    #             matching  = x+initval[inity]
    #             if z ==  matching:
    #                 condition = True
    #                 return(f"[({x}+{initval[inity]})] , arr_index => [{y},{inity}]"); 
    #                 break
                    
                    
    #             inity+=1
    #         y+=1
    #     if condition:
    #         return "Not matched any number."
    def __init__(self, numb):
        self.num = numb

    def test(self):
        initval = [1, 2, 3, 4, 20]
        for i in range(len(initval)):
            for j in range(len(initval)):
                if initval[i] + initval[j] == self.num:
                    return f"[({initval[i]}+{initval[j]})] , arr_index => [{i},{j}]"
                
        return "Not matched any number."
        
