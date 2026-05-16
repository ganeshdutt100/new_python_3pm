# file = open('test.txt', 'w')
# file.write("hello Abhishek")
# file.close()

# file = open('test.txt','r')
# data = file.read()
# print(f'your data is {data}') 
# file.close()

# level-2 
# with open('test.txt','r') as file:
#     data = file.read()
#     print(f'your data is {data}') 


# with open("hello.txt",'w') as file:
#     file.write("hello world ")z
#     file.write('i am Python')
# print("data successfully write ")    


with open('test.txt','a') as file:
    file.write(' new line here \n')
print('new data added')    