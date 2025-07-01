#Fetch first N number of elements from array
def fetch_n_elements(arr,n):
    elements=arr[0: n]
    return elements

if __name__=="__main__":
    # array = [55, 12, 37, 831, 57, 16, 93, 44, 22]
    # print("Array: ", array)
    str_elements=input("Enter space seperated array elements")
    str_array=str_elements.split()
    integer_map_obj = map(int,str_array)
    integer_array=list(integer_map_obj)
    n = int(input("Number of elements to fetch from array: "))
    L=fetch_n_elements(integer_array,n)
    print(' '.join(str(x) for x in L))
