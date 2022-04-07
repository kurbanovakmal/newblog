import random

# b = []
# b.append({a: 'qwqwqwq'})
#
# product = []
# print(b)
# x = input('est account? ')

a = str(random.expovariate(32))
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
        # if prov_id == 'exit':
        #     break
        for x in customers:
            if prov_id == x["id"]:
                new_prods= input('vedite product')
                x["prods"].append(new_prods)
                print(customers)
    elif prov == 'net':
        cust_new = {}
        cust_new["id"] = a
        cust_new["name"] = input('vedite imya')
        cust_new["prods"] = input('vedite producti ').split(", ")
        customers.append(cust_new)
        print(customers)
    elif prov == 'exit':
        break









