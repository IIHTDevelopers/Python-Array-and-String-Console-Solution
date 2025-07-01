
#Convert last given number of characters into upper case in the string.
def convert_upper_at_last(string,n):
    # First part of the string
    start = string[:len(string) - n]
    # last part of the string that we're converting.
    end = string[len(string) - n:]
    result=start + end.upper()
    return result

if __name__=="__main__":
    string = input("String to convert: ")
    n = int(input("How many last letters should be converted into upper case? "))
    result=convert_upper_at_last(string,n)
    print(result)
