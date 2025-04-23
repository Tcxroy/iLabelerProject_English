import os

def get_data_path(file_name):
    try:
        cur_dir = os.path.abspath(os.path.curdir)
        data_dir_1 = 'src'
        data_path = os.path.join(cur_dir,data_dir_1,file_name)
    except:
        raise("file name should be a string")
    return data_path
