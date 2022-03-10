while True:
    a = input('viberite tovar: sigaret = 1, kofe = 2,terminate = 3, back = 4: ')
    if a == '1':
        b = input('vedite vaw vozrast')
        if b >= '18':
            print('vawi sigareti')
        else:
            print('prostite no ya vam ne mogu prodat sigareti')
    elif a == '4':
        continue

    elif a == '3':
        break
    else:
        print('kofe')
print('out')


