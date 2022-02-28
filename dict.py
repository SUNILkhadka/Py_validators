
dictn = {
    'name': 'Doleshor',
    'age': 29,
    'color': 'Grey white',
    'height': 5.5,
    'desc': 'Hello everyone!'
}


def validate(dictionary, dictionary_keys,data_type_rules,data_range_rules):
    # variables for checking and counting the loops 
    '''
        Return whether or not given dictionary is valid or not on the basis of given dictionary keys,
        data type rules & data range rules.
        If the dictionary is valid this function returns ``True``, otherwise
        gives error massages and return ``false`` 
    '''
    check = 0 
    count = 0
    index = 0
    range_rules_list = []
    if dictionary is not dict or dictionary_keys is not list or data_type_rules is not list or data_range_rules is not dict:
        print('''
    Error !!!!
    This functions takes dictionary(dict) as first, dictionary keys(list) as second, data_type_rules(list) as third
    & data_range_rules(dict) as fourth arguement.
    eg.
        dictionary = {
            'name': 'Doleshor',
            'age': 29,
            'color': 'Grey white',
            'height': 5.5,
            'desc': 'Hello everyone!'
            }
        keys = ['name', 'age', 'color', 'height', 'desc']
        data_type_rules = ['string',int,str,float,str]   

        data_range_rules = {
            "name_min" : 5,
            'name_max' : '-',
            'age_min' : 10,
            'age_max' : 50,
            'color_min' : 5,
            'color_max' : 20,
            'height_min' : 5.0,
            'height_max' : 6.0,
            'desc_min' : 10,
            'desc_max' : 100
            }
        
        >>> validate( dictionary, keys, data_type_rules, data_range_rules )
            True
        
        ''')
        return False

    if len(dictionary.keys()) != len(dictionary_keys):
        print("Error! Dictionary keys is is of different length.")
        return False

    if len(data_range_rules)!= 2*len(dictionary_keys):
        print('Error! less or more number of maximum and minimum data range is provided: ',len(data_range_rules))
        print("Given keys length'",len(dictionary_keys),"' which should have '",2*len(dictionary_keys),"' values in data range rules")
        return False   

    for i in dictionary_keys:
        range_rules_list.append(data_range_rules[i+'_min'])
        range_rules_list.append(data_range_rules[i+'_max'])

    for z in data_type_rules:
        string = str(z).lower()
        if string.find('str') >=0 :
            ind = data_type_rules.index(z)
            data_type_rules.remove(data_type_rules[ind])
            data_type_rules.insert(ind,str)
        elif string.find('bool') >=0:
            ind = data_type_rules.index(z)
            data_type_rules.remove(data_type_rules[ind])
            data_type_rules.insert(ind,bool)
        elif string.find('int') >=0:
            ind = data_type_rules.index(z)
            data_type_rules.remove(data_type_rules[ind])
            data_type_rules.insert(ind,int)
        elif string.find('float') >=0:
            ind = data_type_rules.index(z)
            data_type_rules.remove(data_type_rules[ind])
            data_type_rules.insert(ind,float)
        else:
            print("Error! Data type rules contains keyword '",z,"' which is not recognised as data type .")
            return False
    for x in dictionary.keys():
        if x not in dictionary_keys:
            print("Error! '",x,"' key not found in given dictionary keys")
            return False
        data = dictionary[x]
        data_type =  type(data)
        # loop for keys as index of parameter keys may differ from given dictionary keys 
        for y in range(len(dictionary)):
            # checking the parameter dictionary keys with the parameter keys
            if x == dictionary_keys[y]:
                # Extracting minimum and maximum parameters for each matched keys
                min = range_rules_list[count]
                max = range_rules_list[count+1]
                try:
                    if min < max:
                        pass
                    else:
                        raise KeyError()
                except KeyError :
                    return "Error occured while checking! 'minimum value is greater than maximum value'"
                except Exception as e:
                    pass
                # Count is increased by two as the maximum and minimum parameter differs by value two
                count+=2
                # checking wether the given value is float or int or string
                check_type = data_type_rules[index]
                if data_type is int or data_type is float:
                    index +=1
                    if data_type == check_type:
                        if max == '-':
                            if  min < data :
                                check +=1
                        elif min == '-':
                            if  data < max:
                                check +=1
                        else:
                            if  min < data < max:
                                check +=1
                    else:
                        print('Error! Integer of Float not matched as data type in dictionary is ',data_type,' and data type in provided data type rules is ',check_type)
                        return False
                if data_type is str:
                    index+=1
                    if data_type == check_type:
                        if max == '-':
                            if  min < len(data):
                                check +=1 
                        elif min == '-':
                            if  len(data)< max:
                                check +=1 
                        else:
                            if  min < len(data):
                                check +=1 
                    else:
                        print('Error! String not matched as data type in dictionary is ',str(data_type)[-5:-2],' and data type in provided data type rules is ',check_type)
                        return False 
                if data_type is bool:
                    index+=1
                    if data_type == check_type:
                        if data is True or False:
                            check +=1
                    else:
                        print('Error! Boolean not matched as data type in dictionary is ',data_type,' and data type in provided data type rules is ',check_type)
                        return False

    # Finally checking the counter and returning boolean value
    if check == len(dictionary):
        return True
    else:
        return False


data_range_rules = {
    "name_min" : 5,
    'name_max' : '-',
    'age_min' : 10,
    'age_max' : 50,
    'color_min' : 5,
    'color_max' : 20,
   'height_min' : 5.0,
   'height_max' : 6.0,
   'desc_min' : 10,
   'desc_max' : 100
}
arg = {
    'keys': ['name', 'age', 'color', 'height', 'desc'],
    'data_type_rules': ['string',int,str,float,str],
    # 'data_range_rules': [5,'-',10,50,5,20,5.0,6.0,10,100]
    # data range list values is first minimum and second maximum of key in keys corresponding to key
    # pass '-' if you don't want to specify specific length
}

print(validate('dictn',arg['keys'],arg['data_type_rules'],data_range_rules))