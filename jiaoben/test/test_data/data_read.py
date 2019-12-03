'''f = open("./teatdata.txt","r")
data = f.readlines()
f.close()'''
with open("./teatdata.txt","r") as f :
    data = f.readlines()
    #print (data)
    #print (type(data))

test_data=[]
for d in data:
    test_data.append (d.strip("\n"))
    print (test_data)
