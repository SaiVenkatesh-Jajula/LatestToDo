def reading(filename):
    """TO GET THE CONTENT IN A FILE"""
    with open(filename, 'r') as file:
        content = file.readlines()
    return content


def writing(filename,newlist):
    """TO WRITE CONTENT IN A FILE"""
    with open(filename, 'w') as file:
        file.writelines(newlist)


def appending(filename,item):
    with open(filename, 'a') as file:
        file.writelines(item + '\n')

if __name__=="__main__":
    print("This is Backend")
    print("Checking ToDos List: \n", reading())

#ok!