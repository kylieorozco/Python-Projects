'''
Name: Kylie Orozco
Purpose: Program determines if two numbers are "friendly", which is when the factors added together for both numbers have equal sums.
Pre-conditions: User enters two numbers (integers that must be greater than zero)
Post-conditions: Program outputs whether the two numbers are friendly or not (integers)
'''

def main():
    # Prompt user for first number and prevent less than zero
    firstnum = 0;
    while firstnum <= 0:
        firstnum = int(input("Enter first number: "));
        if(firstnum <= 0):
            print("Please enter a number greater than zero");
    # Prompt for second number and prevent less than zero
    secondnum = 0;
    while secondnum <= 0:
        secondnum = int(input("Enter second number: "));
        if(secondnum <= 0):
            print("Please enter a number greater than zero");
            
    # Adds all factors of a number and returns sum
    def factors(num):
        sum=0                     
        for i in range(1, num+1):
            if(num%i == 0):
                sum+=i             
        return sum 
    
    # Takes 2 numbers and checks if friendly or not, uses boolean function
    def friendly(firstnum, secondnum):
        if(factors(firstnum)/firstnum == factors(secondnum)/secondnum):       
            z = True                                  
        else:                                     
            z = False
        return z  
    
    # Depending on boolean function the numbers will either be friendly or not friendly
    friend = friendly(firstnum, secondnum)
    if(friend == True):
        print();
        print(firstnum, "and", secondnum, "are friendly")
    else:
        print();
        print(firstnum, "and", secondnum, "are not friendly")    
main()

'''
A. 31
B. 252
C. 93/40 and 93/40
D. 13/6 and 8/5
E. 30 and 140 are friendly
F. 120 and 150 are not friendly
'''