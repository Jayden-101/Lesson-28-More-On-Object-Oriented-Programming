# create class
class Employee:

    # Initializing
    def __init__(self):
        print("Employee Created")
    
    # Calling Destructor
    def __del__(self):
        print("Destructor called")
    
def Create_obj():
    print('Making Object... ')
    obj = Employee()
    print('function end...')
    return obj

print('Calling Create_obj() functiom...')
obj = Create_obj()
print('Program end...')