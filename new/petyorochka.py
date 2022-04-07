import random

# b = []
# b.append({a: 'qwqwqwq'})
#
# product = []
# print(b)
# x = input('est account? ')

# a = random.expovariate(32)
# d = {a:input('vedite imya ')}
# b.append(d)
#
# print(d.keys())
# print(b)

customers = [{"id": "1212", "name": "akmal", "prods": ["water"]}, {"id": "1212", "name": "roma","prods": ["cola"]}]
g = input('cto to xoteli kupit? ')
while g == 'da':
    prov = input('est account? ')
    if prov == 'da':
        prov_id = input('vedite id')
        for x in customers:
            if prov_id == x["id"]:
                new_prods= input('vedite product')
                x["prods"].append(new_prods)
                print(customers)

    elif prov == 'net':
        for i in customers:
            i[0,1,2] = cust_new[0,1,2]
            cust_new = {a: input('vedite imya, i product').split(", ")}
        
            customers.append(cust_new)
            customer_prod = {a: [input('vedite product').split()]}
            product.append(customer_prod)
            print(product)









