
import json

person_string = '''
{
    "person": [
      {
        "name": "John Smith",
        "age": 18,
        "phone_number": 0908373882,
        "email": null,
        "has_license": false,
      
      },
    ]
}
'''

data = json.loads(person_string)
print(data)
