x_list = [10, 20, -30, -40]




if len(x_list) > 0 and len(x_list) < 5:
    print('List has some elements')
else:
    print('no elements')



if 10 in x_list:
    print('10 is in the list')
else:
    print('10 is not the list')

for i in x_list:
    if i < 0:
        print(i)
        break
