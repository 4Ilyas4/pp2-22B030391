import json
with open('C:\\Users\\User\\Desktop\\programming\\my\\pp2-22B030391\\tsis4\\Json\sample-data.json') as s:
  data = json.load(s)
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for i in range(3):
    l = data['imdata'][i]['l1PhysIf']['attributes']['mtu']
    k = data['imdata'][i]['l1PhysIf']['attributes']['speed']
    d = data['imdata'][i]['l1PhysIf']['attributes']['descr']
    print(str(data['imdata'][i]['l1PhysIf']['attributes']['dn'])+"               "+d+"               "+str(k)+"   "+str(l))

