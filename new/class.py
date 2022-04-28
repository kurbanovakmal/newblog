class Customer:
    def __init__(self, n, a, f):
        self.name = n
        self.age = a
        self.familiya = f
        self.products = []

    def __str__(self):
        return(f"name: {self.name}, age: {self.age}, familiya: {self.familiya} products: {self.products}")
    
    # def save(self):
    #     with open("db.txt, r+")

    def add_prod(self, title):
        self.products.append(title)



customers = []




user1 = Customer("Akmal",25,"Kurbanov")
user1.add_prod("pepsi")

customers.append(user1)
print(customers[0].name)
print(user1.products)

for c in customers