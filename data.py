import os
import json
from faker import Faker

fake = Faker("ru_RU")

# Declare an empty dictionary
data_fake = []

titles = ['Number', 'Name', 'Age', 'Address', 'Phone Number', 'Email']
path = os.path.join(os.getcwd(), 'static', 'data', 'users.json')

# Iterate the loop based on the input value and generate fake data
for n in range(0, 100):
    temp = {}
    temp['name'] = fake.name()
    temp['age'] = fake.random_number(digits=2)
    temp['address'] = fake.address()
    temp['phone'] = fake.phone_number()
    temp['email'] = fake.email()

    data_fake.append(temp)

    # Write the data into the JSON file
with open(path, 'w') as fp:
    json.dump(data_fake, fp)

# print("File has been created.")

'''
                <td>{{ item.name() }}</td>
              <td>{{ item.age }}</td>
              <td>{{ item.address }}</td>
              <td>{{ item.phone }}</td>
              <td>{{ item.email }}</td>
  '''
