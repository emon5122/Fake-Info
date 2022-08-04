from faker import Faker

faker = Faker()
i=0
while i<=10:
    print(faker.simple_profile(sex=None))
    i=i+1