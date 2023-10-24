## listdir ##
# import os

# # Specify the directory you want to list
# directory = './news_data'  # Replace with the path to your directory

# # List the files and directories in the specified directory
# files_and_directories = os.listdir(directory)

# # Print the list of files and directories ##
# for item in files_and_directories:
#     print(item)

## if __name__ == '__main__'
# def some_function():
#     print("This is a function in the module.")

# if __name__ == '__main__':
#     print("This is the main program.")
#     some_function()

import os

def get_file_list(dir_name):
    return os.listdir(dir_name)

def get_contents(file_list):
    y_class = []
    X_text = []
    
    class_dic ={1:'0', 2:'0', 3:'0', 4:'0', 5:'1', 6:'1', 7:'1', 8:'1'}

    for file_name in file_list:
        try:
            f = open(file_name, 'r', encoding='cp949')
            category = int(file_name.split(os.sep)[1].split('_')[0])
            y_class.append(class_dic[category])
            X_text.append(f.read())
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
    return X_text, y_class
        
if __name__ == '__main__':
    # dir_name = './news_data'
    dir_name = 'news_data'

    file_list = get_file_list(dir_name)
        
    for item in file_list:
        print(item)
    
    file_path_list = [os.path.join(dir_name, file_name) for file_name in file_list]
    
    for item in file_path_list:
        print(item)
        
    get_contents(file_path_list)