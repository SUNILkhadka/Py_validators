def validate(dictionary,schema):
    # variables for checking and counting the loops 
    '''
        Return whether or not given dictionary is valid or not on the basis of given dictionary keys,
        data type rules & data range rules.
        If the dictionary is valid this function returns ``True``, otherwise
        gives error massages and return ``false`` 
    '''
    check = 0 
    schema_keys = list(schema.keys())  # or can use schema_keys = [*schema] to extract keys as list
    if type(dictionary) is not dict or type(schema) is not dict:
        print('''
    Error !!!!
    This functions takes dictionary(dict) as first and a schema which is dictionary of validation rules as second arguement.
    eg.
        dictionary = {
            'name': 'Doleshor',
            'age': 29,
            'color': 'Grey white',
            'height': 5.5,
            'desc': 'Hello everyone!'
            }
        schema = {
            'name' : {'type':'string','min':5},
            'age': {'type':'int','max':50},
            'color':{'type':'string','min':2,'max':20},
            'height':{'type':'float','min':5 ,'max':6},
            'desc':{'type':'string','min':10,'max':100}
            # min = minimum length of the string or minimum value of integer
            # max = maximum length of the string or maximum value of integer
            }

        
        >>> validate( dictionary, schema )
            True
        
        ''')
        return False

    if len(dictionary.keys()) != len(schema_keys):
        print("Error! Dictionary keys is is of different length.")
        return False
    for x in dictionary.keys():
        if x not in schema_keys:
            print("Error! '",x,"' key not found in given schema keys")
            return False
        data = dictionary[x]
        data_type =  type(data)
        # loop for keys as index of parameter keys may differ from given dictionary keys 
        for y in range(len(dictionary)):
            # checking the parameter dictionary keys with the parameter keys
            if x == schema_keys[y]:
                # Extracting minimum and maximum parameters for each matched keys
                schema_data = schema[x]
                string = str(schema_data['type']).lower()
                if string.find('str') >=0:
                    schema_data['type'] = str  
                elif string.find('bool') >=0:
                    schema_data['type'] = bool 
                elif string.find('int') >=0:
                    schema_data['type'] = int 
                elif string.find('float') >=0:
                    schema_data['type'] = float 
                else:
                    print("Error! Data type rules contains keyword '",string,"' which is not recognised as data type .")
                    return False       
                try:
                    min = schema_data['min']
                except:
                    min = None
                try:
                    max = schema_data['max']
                except:
                    max = None
                try:
                    if min < max:
                        pass
                    elif max==None or min==None:
                        raise Exception 
                    else:
                        raise KeyError()
                except KeyError :
                    return "Error occured while checking! 'minimum value is greater than maximum value'"
                except:
                    pass
                # checking wether the given value is float or int or string
                check_type = schema_data['type']
                if data_type is int :
                    if data_type == check_type:
                        if max == None:
                            if  min < data :
                                check +=1
                        elif min == None:
                            if  data < max:
                                check +=1
                        else:
                            if  min < data < max:
                                check +=1
                    else:
                        print('Error! Integer not matched as data type in dictionary is ',str(data_type)[-5:-2],' and data type in provided data type rules is ',check_type)
                        return False
                if data_type  is float:
                    if data_type == check_type:
                        if max == None:
                            if  float(min) < float(data) :
                                check +=1
                        elif min == None:
                            if  float(data) < float(max):
                                check +=1
                        else:
                            if  float(min) < float(data) < float(max):
                                check +=1
                    else:
                        print('Error! Float not matched as data type in dictionary is ',str(data_type)[-7:-2],' and data type in provided data type rules is ',check_type)
                        return False
                if data_type is str:
                    if data_type == check_type:
                        if max == None:
                            if  min < len(data):
                                check +=1 
                        elif min == None:
                            if  len(data)< max:
                                check +=1 
                        else:
                            if  min < len(data):
                                check +=1 
                    else:
                        print('Error! String not matched as data type in dictionary is ',str(data_type)[-5:-2],' and data type in provided data type rules is ',check_type)
                        return False 
                if data_type is bool:
                    if data_type == check_type:
                        if data is True or False:
                            check +=1
                    else:
                        print('Error! Boolean not matched as data type in dictionary is ',str(data_type)[-6:-2],' and data type in provided data type rules is ',check_type)
                        return False

    # Finally checking the counter and returning boolean value
    if check == len(dictionary):
        return True
    else:
        return False

dictn = {
    'name': 'Doleshor',
    'age': 50,
    'color': 'Grey white',
    'height': 5.5,
    'desc': 'Hello everyone!'
}
arg = {
    'name' : {'type':'string','min':5},
    'age': {'type':'int','max':50},
    'color':{'type':'string','min':2,'max':20},
    'height':{'type':'float','min':5 ,'max':6},
    'desc':{'type':'string','min':10,'max':100}
}
print(validate(dictn,arg))