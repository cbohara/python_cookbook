import os

# store list of directories in the current directory
filenames = os.listdir('.')

# create a list of files ending with .py in the current directory
py_files = [name for name in filenames if name.endswith('.py')]
print(py_files)
