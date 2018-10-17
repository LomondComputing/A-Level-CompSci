# List operation

def insert(New,L):
     p = 0
     ListLength = len(L)
     if ListLength > 0:
          while p < ListLength and L[p] < New:
               p += 1
          L.append(None)
          ListLength += 1
          for q in range(ListLength-1, p, -1):
               L[q] = L[q-1]
     L[p] = New     
     return L

nums = [1, 5, 7, 11, 19, 35]
print(nums)
print(insert(-1,nums))
