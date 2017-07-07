import json

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23,
    'anthoer_json': {
        'name': 'acer'
    }
}

data['xx'] = [0]
print (dir(data))
json_str = json.dumps(data)

print (json_str)