#All For Chaining

def hashFunc(key):
    return key%len(hashTable)

def insertKey(hashTable,key,value):
    hashKey=hashFunc(key)
    hashTable[hashKey].append(value)#=value

def insertKeyValue(hashTable,key,value):
    hashKey=hash(key)%len(hashTable)
    key_exists=False
    bucket=hashTable[hashKey]
    for i,kv in enumerate(bucket):
        k,v=kv
        if key==k:
            key_exists=True
            break
    if key_exists:
        bucket[i]=((key,value))
    else:
        bucket.append((key,value))

def search(hashTable,key):
    hashKey=hash(key)%len(hashTable)
    bucket=hashTable[hashKey]
    for i,kv in enumerate(bucket):
        k,v=kv
        if key==k:
            return v

def delete(hashTable,key):
    hashKey=hash(key)%len(hashTable)
    key_exists=False
    bucket=hashTable[hashKey]
    for i,kv in enumerate(bucket):
        k,v=kv
        if key==k:
            key_exists=True
            break
    if key_exists:
        del bucket[i]
        print('Key {} deleted',format(key))
    else:
        print('Key {} not found',format(key))

hashTable=[[] for i in range(int(input("Enter the length of the HashTable ")))]
print("Enter key and the value correspondingly:")
for i in range(len(hashTable)):
    insertKeyValue(hashTable,int(input()),input())
print(hashTable)
print(search(hashTable,10))
print(search(hashTable,20))
print(search(hashTable,30))
delete(hashTable,40)
print(hashTable)
delete(hashTable,10)
print(hashTable)