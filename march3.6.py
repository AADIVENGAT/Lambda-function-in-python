#lambda function used to call function for 1 time only. It can be used for single expression.
#used to pass mutiple arguments.
#It is anonymous.
x=lambda a:a+10
print(x(5))

x = lambda a,b:a*b
print(x(5,6))