# Lambda function  in python
# lambda function is small anonymous function in single line.
# USe for simple one-time-tasks
# lambda use built in function like map(), filter()

add = lambda a,b: a+b
print(add(5,5)) 

sqaure = lambda a: a*a
print(sqaure(2))

nums = [1,2,3,4,5]
square = list(map(lambda x: x*x,nums))
print(square)

numbers=[1,2,3,4,5]
sq=list(map(lambda x: x*x*x,numbers))
print(sq)