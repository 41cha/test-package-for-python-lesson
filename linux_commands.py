import os, time, stat

def ls(directory, flag='-a'):

    if flag == '-a':
        for item in os.listdir(directory):
            print(item)

    if flag == '-l':
        for item in os.listdir(directory):

            path = os.path.join(directory, item)

            stats = os.stat(path)

            permissions = stat.filemode(stats.st_mode)

            size = stats.st_size

            create_time = time.ctime(stats.st_birthtime)

            print(f'parth is: {path}\n, permissions: {permissions}\n, size is: {size}\n, time is: {create_time}\n')
        
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

