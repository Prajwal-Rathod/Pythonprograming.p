#while loop to find sum of first n numbers
endpoint=int(input("enetr the value of endpoint:"))
sum_of_numbers=0
i=0
while i <=endpoint:
    sum_of_numbers=sum_of_numbers+i
    i=i+1
print("the sum of first {} whole numbers is {}".format(endpoint,sum_of_numbers))