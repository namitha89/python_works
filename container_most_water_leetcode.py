def container_most_water(arr):
    left = 0
    right = len(arr) -1
    area = 0

    while(left < right):
        area = max(area, min(arr[left], arr[right]) * (right - left))

        if arr[left] < arr[right]:
            left +=1
        else:
            right -=1
    return area

a = [1,5,6,3]
b = [3,1,2,4,5]

print(container_most_water(a))
print(container_most_water(b))
