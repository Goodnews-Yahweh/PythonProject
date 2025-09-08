
'''JavaScript Object Notation'''

import json

person_hobbies: dict = '''
{
    "people": [
    {
        "name": "John",
        "age": "18",
        "hobby": ["plays games","eats"],
        "likes_reading": false
    },

    {
        "name": "Jane",
        "age": null,
        "hobby": ["reads","codes"],
        "likes_reading": true
    }
  ]
}
'''

data = json.loads(person_hobbies)

print(data)
