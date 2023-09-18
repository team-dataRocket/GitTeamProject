def fizzbuzz(num:int) :
    for i in range(1,num+1) :
        if i == 15 :
            print('fizzbuzz')
        else :     
            if i % 3 == 0 :
                print('fizz')
            elif i % 5 == 0 :
                print('buzz')
            else :
                print(i)
                
if __name__ == '__main__' : 
    fizzbuzz(15)