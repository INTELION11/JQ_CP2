from faker import Faker

fake = Faker()
while True:
    print(fake.name())
    print(fake.address())
    print(fake.age())
    to = input("")