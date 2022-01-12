#comman elements from the list
listA = [45, 20, 11, 50, 17, 45, 50,13, 45]
print("Given List:\n",listA)
res = max(set(listA), key = listA.count)
print("Common elements among the list:\n",res)
print("-------------------------------------------")
#comman elements from the tupple
t1 = ('Hi there', 'Hi Will,', 'Hi ', 'Hi there')

print("The tuple is : ")
print(t1)

my_result = ", ".join(sorted(set(t1[0].split()) & set(t1[1].split()) &
                             set(t1[2].split())))

print("Common words among the tuples: ")
print(my_result)
print("---------------------------------------------")
# Common elements Dictionary Value List
test_dict1 = { "Key1" : [1, 3, 4], "key2" : [4, 5] }
test_dict2 = { "Key1" : [1, 7, 3] }
print("The original dict 1 : " + str(test_dict1))
print("The original dict 2 : " + str(test_dict2))
res = dict()
for key in test_dict1:
   if key in test_dict2:
      res[key] = []
      for val in test_dict1[key]:
         if val in test_dict2[key]:
            res[key].append(val)
print("The common elements in dictionary : " + str(res))
