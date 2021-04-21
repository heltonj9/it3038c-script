import json
import requests

r = requests.get('http://localhost:3000')

data = r.json()

count = 0;

for name in data:
    beggar = (data[count]["name"]) + " is " + (data[count]["color"]) + ".";
    print(beggar);
    count = count + 1; 


#Below are some attempts at making the format exactly as in the lab9 instructions. It feels like a waste to get rid of it, so I'm just keeping it there in case I ever come back and look at this. 

#for name in data:
#    beggar = print(data[count]["name"]), print("is "), print(data[count]["color"]), print('\n');
#    print(beggar);
#    count = count + 1;  

#for name in data:
#    print(data[count]["name"]), print(data[count]["color"])
#    count = count + 1;
    
#for name in data:
#    name1 == print(data[count]["name"]);
#    color1 == print(data[count]["color"]);
#    print("%s is %s"(name1, color1));
#    count = count + 1;
    
#for name in data:
#    print(data([count]["name"][count]["color"]))
#    count = count + 1;
#print(data['name']+[0],['color']+[0])
#print(type(data))
#for item in data:
#    for data_item in item['name']:
#        print(data_item[0], data_item[0])

#widgetName = data([0][0])
#print(widgetName)

#print(data(['name'][0]['color']))
#rint(data['weather'][0]['description'])
