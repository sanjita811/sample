string1='ACEGAEGCAE'
for i in range(len(string1)-1,-1,-1):
    if(string1[i]=='A'):
        print(i)
        break
else:
    print('not found')
