##################################################
'''
Q1: 
'''

# TODO: Write your code here

##################################################
'''
Q2:
'''

# TODO: Write your code here

##################################################
'''
Q3:
'''

# TODO: Write your code here

##################################################
'''
Q4:
'''

# TODO: Write your code here

##################################################
'''
Q5:
'''

# TODO: Write your code here

##################################################
'''
Q6:
'''

# TODO: Write your code here

##################################################
'''
def year(numberyears,balence,intrest,newdeposit,newbalence):
    print(f'{numberyears}: current balence: {balence} : intrest: {intrest} deposit: {newdeposit} new balence{newbalence}')



for intrest in range(1, 26):
    year(intrest,)
    print(f'')

'''

start_balance = 0
interest = 0
interest_rate = 0.065
deposit = 100
end_balance = 1000

for year in range(25):
    start_balance = end_balance
    interest = start_balance * interest_rate
    end_balance = start_balance + interest
    print(f'{year+1:02}: current balance: {start_balance:.2f}, intrest: {interest:.2f}, deposit: {deposit:.2f}, new balance: {end_balance:.2f}')
    end_balance += deposit
