import os

from sys import argv


FOLDERS = {
    'text': [
        'pdf',
        'txt',
        'doc',
        'docx',
        'djvu',
        'epub',
        'odt',
        'rtf',
    ],
    'archives': [
        'zip',
        'rar',
        'tar',
        'gz',
        'tgz',
    ],
    'images': [
        'jpg',
        'jped',
    ],
    'videos': [
        'mp4',
        'avi',
        'mpeg',
        'mpg',
    ]
}

def create_dir(path, dirname):
    if not os.path.exists(os.path.join(path, dirname)):
        os.mkdir(os.path.join(path, dirname))

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def get_list_of_files(path):
    return os.listdir(path)

def main():
    path = argv[1]
    files = get_list_of_files(path)

    for folder in FOLDERS:
        create_dir(path, folder)

    for file in files:
        for folder in FOLDERS:
            if file.split(os.extsep)[-1] in FOLDERS[folder]:
                if not os.path.exists(os.path.join(path, folder, file)):
                    os.rename(os.path.join(path, file), os.path.join(path, folder, file))
                else:
                    os.rename(os.path.join(path, file), os.path.join(path, folder, f'{file.split(".")[0]}-copy.{file.split(".")[-1]}'))


if __name__ == '__main__':
    main()