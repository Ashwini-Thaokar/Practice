import Stack
def getBinary(dec_num):
        rem_stack= Stack()
        while dec_num>0:
            rem= (dec_num) % 2
            rem_stack.push(rem)
            dec_num= (dec_num)//2
        binary_string= ""
        while not rem_stack.is_empty():
            binary_string = binary_string + str(rem_stack.pop())
        return binary_string
        
print(getBinary(12))
