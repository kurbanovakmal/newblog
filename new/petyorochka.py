import random

# b = []
# b.append({a: 'qwqwqwq'})
#
product = []
# print(b)
# x = input('est account? ')

a = random.expovariate(32)
# d = {a:input('vedite imya ')}
# b.append(d)
#
# print(d.keys())
# print(b)

customers = [{0.007: 'akmal'}, {0.008: 'roma'}]
g = input('cto to xoteli kupit? ')
while g == 'da':
    prov = input('est account? ')
    if prov == 'da':
        prov_id = input('vedite id')
        for x in customers:
            if prov_id == str(x.keys()):
                customer_prod = {prov_id: input('vedite product')}
                product.append(customer_prod)
                print(product)

    elif prov == 'net':
        cust_new = {a: input('vedite imya: ')}
        customers.append(cust_new)
        customer_prod = {a: input('vedite product')}
        product.append(customer_prod)
        print(product)








