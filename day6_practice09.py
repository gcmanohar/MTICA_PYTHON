#string compransion--------------
'''ans=[]
for i in range(1,1001):
    if '6' in str(i):
        ans.append(i)
print(ans)'''


ans=[ i for i in range(900,1001) if '6' in str(i)]
print(ans)

print([ i for i in range(900,1001) if '6' in str(i)])
