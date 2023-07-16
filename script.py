import os
print("start")
p = str(input("Please Enter your path: "))
#p = os.getcwd()
print(os.path.isabs(p))
sizes = {}
def file(p):
    if (os.path.isabs(p)):
        for root, directories, files in os.walk(p):
            for _file in files:
                full_path = os.path.join(root, _file)
                size = os.path.getsize(full_path)
                sizes[full_path]=size
file(p)
sizes = sorted(sizes.items(),key=lambda x:x[1],reverse=True)
print(sizes[0])
