from faker import Faker

faker = Faker()
i=0
j=int(input("How many fake profiles do you want?\n"))
while i<=j:
    print(faker.simple_profile(sex=None))
    i=i+1
