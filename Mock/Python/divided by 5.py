number_List = list(eval(input('number_List[]=')))
import numpy
print('numbers that are divided by 5:', list([x for x in number_List if x % 5 == 0]))

seq_List = []
for i in range(len(number_List)):
    if number_List[i] % 5 == 0:
        seq_List.append(i)

print('Index', seq_List)


   
