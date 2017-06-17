from pprint import pprint

def update(data, service, count):
    sum=[]
    sumj=0
    for  i in data:
        if len(data[i])==0:
            aux_dict={service: 0}
            data[i].update(aux_dict)
        for j in list(data[i]):
            if (service in data[i]) == False:
                aux_dict={service: 0}
                data[i].update(aux_dict)
            sumj=sumj+data[i][j]
        print(sumj)
        sum.append(sumj)
        sumj=0
    sumj=0
    
    while count>0:
        for j, i in enumerate(data):
            if count == 0:
                break
            if sum[j] == min(sum):
                sumj=data[i].get(service)+1
                data[i].update({service: sumj})
                sum[j]=sum[j]+1
                count=count-1
def main():
    example_data = {
        'ginger': {
            'django': 2,
            'flask': 3,
        },
        'cucumber': {
            'flask': 1,
       },
    }

    
    print("Configuration before:")
    pprint(example_data)
    update(example_data, 'pylons', 7)
    print("Configuration after:")
    pprint(example_data)

if __name__ == '__main__':
    main()
