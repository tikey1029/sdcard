import os
path = 'E:'
os.chdir(path)

LOOP = 3000
success = 0
for i in range(LOOP):
    with open('test.txt','w') as f:
        f.write('add\n')
        success += 1
        print(success)
    os.remove('test.txt')
with open('test.txt','w') as f:
    f.write('add\n')
    success += 1
print(success)