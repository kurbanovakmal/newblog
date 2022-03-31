# dict = { "name":"Roma","age":24,"girls":['nastya','elena']}
# dict['status'] = "Yura"


# for k, v in dict.items():
#     print(k,v)

customers = []
for t in range(3):
    user = input("enter name, age, product").split(",")
    customers.append({"name":user[0],"age":user[1],"product":user[2]})

print(customers)

total_age = 0

for i in customers:
    total_age += int(i["age"])
avg_age = total_age / len(customers)
print(avg_age)