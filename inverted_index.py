

def inverted_index(texts):
    res = {}
    for index,text in enumerate(texts):
        for word in text.lower().split(' '):
            if word in res.keys():
                res[word].append(index)
            else:
                res[word] = [index]
    return res


texts = ['A risk management plan is a','this focus on risk management']

print(inverted_index(texts))