import os

def print_docs(directory, indent=0):
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        print(" " * indent + item)
        if os.path.isdir(path):
            print_docs(path, indent + 4)


print_docs("/home/artitiam/my/Programming/python-course")