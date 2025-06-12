# This function demonstrates the use of **kwargs (keyword arguments)
def myInfo(fname, lname, **kargs):
    # Combine first name and last name
    name = f'Name : {fname} {lname}'
    
    # Access specific keys from kwargs
    print(kargs['location'])     # Will raise KeyError if 'location' is not provided
    print(kargs['occupation'])   # Will raise KeyError if 'occupation' is not provided

    # Loop through all key-value pairs in kwargs
    for key, value in kargs.items():
        print(f'{key} : {value}')
        
    return name

# Calling the function with named arguments
info = myInfo(fname='Sifat', lname='Samin', age=24, location='Bangladesh', occupation='Student')
print(info)


def myInfo(fname, lname, **kargs):
    name = f'Name : {fname} {lname}'

    # Safe access to dictionary values
    location = kargs.get('location', 'Not Provided')
    occupation = kargs.get('occupation', 'Not Provided')

    print(f'Location: {location}')
    print(f'Occupation: {occupation}')

    for key, value in kargs.items():
        print(f'{key} : {value}')

    return name

info = myInfo(fname='Sifat', lname='Samin', age=24)
print(info)
