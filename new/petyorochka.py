import random
a = str(random.expovariate(32))
customers = [{"id": "1212", "name": "akmal","age":23, "prods": ["water"]}, {"id": "12121", "name": "roma","prods": ["cola"]}]
g = input('Do you want to buy something? ')
while g == 'Yes' or g == 'yes':
    prov = input("do you have an account? ")
    if prov == "yes" or prov == "Yes":
        prov_id = input('Enter your id: ')
        if prov_id == 'exit':
            break
        for x in customers:
            if prov_id == x["id"]:
                new_prods= input("Choice a product: ")
                x["prods"].append(new_prods)
                print(customers)
            elif prov_id != x["id"]:
                print("error!! Please enter correct id! ")

    elif prov == "No" or prov == "no":
        cust_new = {}
        cust_new["id"] = a
        cust_new["name"] = input("Enter a name: ")
        cust_new["age"] = int(input("Enter your age: "))
        cust_new["prods"] = input("Choice a product: ").split(", ")
        customers.append(cust_new)
        print(customers)
    elif prov == "exit":
        break









