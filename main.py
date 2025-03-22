class better_float:
    
    # float exponentiation function
    def powerF(float_num, degree):
        
        string = str(float_num)
        dot_index = string.find('.')
        after_dot = len(string[dot_index + 1:])
        before_dot = int(string[:dot_index])
        without_dot = int(string.replace('.',''))

        if before_dot != 0:
            pre_rez = without_dot**degree
            space_count = after_dot * degree
            
            # rez = str[:-dot] + '.' + str[-dot:]
            # rez - rezult
            # dot - index with dot 
            
            rez = float(str(pre_rez)[:-space_count] + '.' + str(pre_rez)[-space_count:])
        else:
            pre_rez = without_dot**degree
            space_count = after_dot * degree
            
            if pre_rez > 0:
                dop_zero = '0'*space_count + str(pre_rez)
                rez = float(str(dop_zero)[:-space_count] + '.' + str(dop_zero)[-space_count:])
            
            else:
                dop_zero = '-' + '0'*space_count + str(pre_rez)[1:]
                rez = float(str(dop_zero)[:-space_count] + '.' + str(dop_zero)[-space_count:])
        
        return rez


    # float summation function
    def sumF(*float_nums):
        
        list_of_rezs = []
        output = 0

        for float_num in float_nums:
            string = str(float_num)
            dot_index = string.find('.')
            after_dot = len(string[dot_index + 1:])
            before_dot = int(string[:dot_index])
            without_dot = int(string.replace('.',''))

            max_dot = 0

            if after_dot > max_dot: max_dot = after_dot

            list_of_rezs.append((without_dot, after_dot))

        for num, dot in list_of_rezs:
            output += int(num + '0'*(max_dot - dot))

        rez = str(output)[:-max_dot] + '.' + str(output)[-max_dot:]

        return rez

