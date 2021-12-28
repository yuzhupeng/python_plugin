import json

books = [
    {
        'title': '钢铁是怎样练成的',
        'price': 9.8
    },
    {
        'title': '红楼梦',
        'price': 9.9
    }
]

dumps_json = json.dumps(books, ensure_ascii=False)
print(dumps_json)
load_json = json.loads(dumps_json)
print(load_json)