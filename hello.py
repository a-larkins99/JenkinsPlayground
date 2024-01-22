# overly complex hello world program

def greet(name):
    ''' 
    returns a greeting to the screen

    >>> greet("Aaron")
    'Hello, Aaron'
    '''

    return f"Hello, {name}"


if __name__ == "__main__":
    team = ["Jacob", "Chris", "Duc"]
    for member in team:
        print(greet(member))
