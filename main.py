class better_float:
    
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