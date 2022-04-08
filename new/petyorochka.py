import random
a = str(random.expovariate(32))
product = [{"id":"1", "price": "50","name":"cola" },{"id":"2", "price": "40","name":"pepsi" }]
customers = [{"id": "1212", "name": "akmal", "prods": ["water"]}, {"id": "12121", "name": "roma","prods": ["cola"]}]
g = input('Do you want to buy something? ')
while g == 'Yes' or g == 'yes':
    summ = 0
    prov = input("do you have an account? ")
    if prov == "yes" or prov == "Yes":
        prov_id = input('Enter your id: ')
        if prov_id == 'exit':
            break
        for x in customers:
            if prov_id == x["id"]:
                new_prods= input("Choose a product: ")
                x["prods"].append(new_prods)
                print(customers)
    elif prov == "No" or prov == "no":
        cust_new = {}
        cust_new["id"] = a
        cust_new["name"] = input("Enter a name: ")
        cust_new["prods"] = input("Choose a product: ").split(", ")
        customers.append(cust_new)
        print(customers)
    elif prov == "exit":
        break









