def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      
# Driver Code 
duplicate = []
n=int(input("Enter the number for list :"))
print("Enter the list : ")
for i in range(0,n):
    ele=int(input())
    duplicate.append(ele)
print(Remove(duplicate))