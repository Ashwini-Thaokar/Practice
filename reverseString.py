def reverseString(a_string):
    arr= (a_string).split(" ")
    reverse= []
    while len(arr)!=0:
        reverse.append(arr.pop())
    return " ".join(reverse)

if __name__=="__main__":
    output= reverseString("Today is very cloudy day")
    print (output)
