"""拡張子を.jpg-largeから.jpgへリネームする"""

import os
def rename_large():
    """拡張子を.jpg-largeから.jpgへリネームする"""
    extension_list = ['jpg', 'png']
    current_working_directory = os.getcwd()
    print('working directory is', current_working_directory)

    file_list = os.listdir(current_working_directory)
    for extension in extension_list:
        for file_name in file_list:
            if '.{}_large'.format(extension) in file_name:
                file_renamed = file_name.replace('{}_large'.format(extension), '{}'.format(extension))
                if file_renamed in file_list:
                    print(file_renamed, 'is already exist.')
                else:
                    os.rename(file_name, file_renamed)
                    print(file_name, 'was renamed to', file_renamed)
    print('done.')

if __name__ == '__main__':
    rename_large()