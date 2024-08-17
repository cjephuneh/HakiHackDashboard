import requests
import json
from pprint import pprint

# Make API request
response = requests.get('https://random-person-generator.com/api')
data = response.json()  

# Add person data
person =  [{'name': data['identification']['full_name'],
           'dob': data['identification']['date_of_birth'],
           'email': data['contact_information']['email_address'],
           'service_num': data['financial_information']['cvv2'],
           'image': data['profile_photo']['256x256']}]

# Generate more data             
for i in range(10):
   response = requests.get('https://random-person-generator.com/api')
   data = response.json()
   
   person.append({'name': data['identification']['full_name'],
                'dob': data['identification']['date_of_birth'],
                'email':data['contact_information']['email_address'],
                'service_num':data['financial_information']['cvv2'],
                'image': data['profile_photo']['256x256']})
   
person_json = json.dumps(person, indent=2)
