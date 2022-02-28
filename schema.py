
from cerberus import Validator



schema = {
    'name' : {'type' :'string','minlength':5 ,'maxlength': 20},
    'age': {'type': 'integer'},
    'sex': {'type': 'string'},
    'location':{
        'type': 'dict',
        'schema': {
            'latitude': {'type': 'float' },
            'longitude': {'type':'float'}
        }
    },
    'address':{
        'type': 'dict',
        'allow_unknown': True,
        'schema':{
            'country': {'type':'string'},
            'city': {'type': 'string'}
            }
    }
}
v = Validator(schema)
print(v.validate({
    'name':'sunil khadka',
    'age': 29,
    'sex':'M' ,
    'address':'itahari',
    'location': {'latitude':28.394857,'longitude':84.124008},
    'address': {'country':'Nepal','city':'Dharan','street':'mahendra road'}
    }))


