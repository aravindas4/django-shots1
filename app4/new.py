# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
# Find this single element that appears only once.
# Input: [1,1,2,3,3,4,4,8,8]
#


def find_min(array, start, end):
    mid = len(array) // 2

    if len(array) == 3:
        return array[0]

    if len(array[start:mid+1]) % 2 == 1:
        return find_min(array[start:mid+1], start, mid)
    elif len(array[mid+1:end]) % 2 == 1:
        return find_min(array[mid+1:end], mid+1, end)


if __name__ == '__main__':
    inpu = [3,3,7,7,10,11,11]
    print(find_min(inpu, 0, len(inpu)))



# Employee: name, salary
# salaries = Employee.objects.order_by('salary').values('salary')
# [5000, 4000, 3000, 2000]
# Employee.objects.filter(salary=salaries[2]).values('name')
