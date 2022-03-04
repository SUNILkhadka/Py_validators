
fruits = [
    {
        'name':'apple',
        'color':'red',
        'price':500
    },
    {
        'name':'orange',
        'color':'orange',
        'price':300
    },
    {
        'name':'cherry',
        'color':'red',
        'price':800
    },
    {
        'name':'pinapple',
        'color':'yellow',
        'price':700
    },
    {
        'name': 'banana',
        'color':'yellow',
        'price':100
    },
]

count = 4
result = {}
res = []

result = {}
result = {}
def filter_by_color(keyword):
    if result == {}:
        for fruit in fruits:
            if fruit['color'] not in result:
                result[fruit['color']] = []

            if fruit['color'] in result:
                result[fruit['color']].append(fruit)
        return result[keyword]

    else:
        return result[keyword]
    
print(filter_by_color('red'))
print(filter_by_color('yellow'))
    
print(filter_by_color('red'))
print(filter_by_color('red'))








# for fruit in fruits:
#     if fruit['color'] not in result:
#         result[fruit['color']] = []
    
#     if fruit['color'] in result.keys():
#         result[fruit['color']].append(fruit)
    








# for x in fruits:
#     res = []
#     for y in range(count):
#         if x['color'] == fruits[y]['color']:
#             res.append(fruits[y])
#             count-=1
#     try:
#         if result[x['color']]:
#             continue
#     except:
#         result[x['color']] = res

print(result)