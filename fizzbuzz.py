def fizzbuzz(num:int) :
    for i in range(1, num+1):
        if i%3==0 or i%5==0:
            print('fizz'*(i%3==0)+'buzz'*(i%5==0))
        else :
            print(i)
                
if __name__ == '__main__' : 
    fizzbuzz(15)


