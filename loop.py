#Merging Lists Conditionally
list1 = [10, 20, 25, 30, 35] #odd
list2 = [40, 45, 60, 75, 90]
result_list=[]
def new_list(list1,list2):
 for n in list1:
  if n%5!=0:
   result_list.append(n)
 for num in list2:
  if num%5==0:
   result_list.append(num)
 return result_list
print("result list: ",new_list(list1,list2))   
