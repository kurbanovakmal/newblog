# def shop():
#     c = input('enter ur name: ')
#     print(f'hello,{c}')

# def prov():
#     a = input('skolko vam let? ')
#     if a >= '18':
#         print('vi sovershennoletniy')
#     else:
#         print('vi nesovershennoletniy')


# def sum(x, y):
#     return x + y

# c = sum(3, 4)
# print(c)

a = [1,2,3,4,5]

def summ(a):
    sum = 0
    for x in a:
        sum = sum + int(x)
    return sum
c = summ(a)
print(c)
