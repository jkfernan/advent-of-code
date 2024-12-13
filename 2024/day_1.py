list1=[]
list2=[]
with open('advent1.txt','r') as f:
    for line in f:
        n = line.split()
        list1.append(int(n[0]))
        list2.append(int(n[1]))
        
list1.sort()
list2.sort()
           
diff_total=0
similarity_score_total=0

for i, element in enumerate(list1):
    diff_total+=abs(list1[i]-list2[i])
    element_count=list2.count(element)
    similarity_score=int(element)*element_count
    similarity_score_total+=similarity_score

print(diff_total)
print(similarity_score_total)
