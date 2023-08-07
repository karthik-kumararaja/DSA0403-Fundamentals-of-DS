a="An apple a day keeps us from doctor away, apple is also a renowned phone company"
b=a.split()
print(b)
count=0
for i in range(len(b)):
    if b[i] in b:
        count=count+1
        print(b[i],count)
        count=0
        
        
