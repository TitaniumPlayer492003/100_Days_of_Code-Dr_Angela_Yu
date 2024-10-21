# Whenever we write the 'return' keyword our function exits

def format_name(f_name,l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name,l_name
    print(f'Result: {f_name},{l_name}')

# That is as soon as a function encounters a return key word, the function just gives it as the output