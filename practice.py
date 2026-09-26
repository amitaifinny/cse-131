def get_temp(t_value, t_type):
    t_value = input("What is the temperature value? ")
    t_type = input("What is the temperature type (k, f, or c)? ")

def convert_temp(t_value, t_type, t_output):
    if t_type == "f" and t_output == "c":
        final_temp = (t_value - 32) * 5 / 9
        return final_temp
    if t_type == "c" and t_output == "f":
        final_temp = (t_value * 9 / 5) + 32
        return final_temp
    if t_type == "c" and t_output == "k":
        final_temp = t_value - 273.15
        return final_temp
user_temp_info = get_temp()
conversion = convert_temp()
print(conversion)
        

