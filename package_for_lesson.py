import os

def ls(directory, flag='-a'):
    if flag == '-a':
        for item in os.listdir(directory):
            print(item)

    if flag == '-l':
        pass

    else:
        raise 

def pwd():
    print(os.getcwd())

def mkdir(directory_name):
    os.mkdir(directory_name)

def rm(file_or_directory):
    os.remove(file_or_directory)

def cat(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    else:
        print("Файл не знайдено.")

    
def cp(sourse, destination):    
    pass

def mv(sourse, destination):
    os.rename(sourse, destination)


print('--------------------------------------------------------------------------------')
ls(r'C:\Users\intit\Documents\test_for_package')
print('--------------------------------------------------------------------------------')
cat(r'C:\Users\intit\Documents\test_for_package\file.txt')
print('--------------------------------------------------------------------------------')
pwd()
print('--------------------------------------------------------------------------------')
