input_int = 12
bin_con = bin(input_int)[2:]
decimal_str = ""

print("Binary convertion of Input decimal number: "+bin_con)

for i in range(len(bin_con)):
    if bin_con[i] == '0':
        # bin_con[i] = '1'
        decimal_str = decimal_str + '1'
    else:
        # bin_con[i] = '0'
        decimal_str = decimal_str + '0'
        
int_con = int(decimal_str,2)
print(int_con)
