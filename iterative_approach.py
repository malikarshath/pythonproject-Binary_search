length = int(input("Enter length of list: "))
int_list=[]

for i in range(length):
    element = int(input("Enter element: "))
    int_list.append(element)

int_list=sorted(int_list)
print(int_list)

target = int(input("Enter target: "))

start = 0
end = length-1
position = -1

while(start<=end):

    mid = (start+end)//2

    if int_list[mid] == target:
        position = mid+1
        break
    elif target < int_list[mid]:
        end = mid-1
    elif target > int_list[mid]:
        start = mid+1

if position == -1:
    print('Element not in list')
else:
    print('Element found at position: ',str(position))
