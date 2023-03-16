
# you've files and u'd want to group them by their name 
# arabic -> arabic dir. english -> english dir and so on
# match if the name of the file is the name of the dir and throw it there 
# end task

import pathlib, os, shutil, configparser

def _create_dir_if_doesnt_exist(dir_path: str) -> None:
    """checks if the dir is there, and creates it if not

    Args:
        dir_path (str): path to the directory
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def _move_file(file_path: str,dir_path:str ) -> None:
    """copies the files from one dir to another

    Args:
        file_path (str): source file path to be copied
        dir_path (str): distination where to copy to
    """
    # i understood from the pdf that we want to organize the files; meaning MOVE not copy them
    shutil.move(file_path, dir_path)


def organize_files(root_dir: str, dist_dir:str)-> None:
    try:
        for file in os.listdir(root_dir):
            # print(file)
            file_name = file.split("-")[0]

            # check if a dir with the name of the file exsists and create it 
            _create_dir_if_doesnt_exist(os.path.join(dist_dir,file_name))
            # move the file there 

            if file.find(file_name) >= 0 :
                _move_file(os.path.join(root_dir, file), os.path.join(dist_dir,file_name))
    except Exception as ex:
        print(ex)
        print("not really needed or placed correctly but meh")

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini")

    root_dir = config["DEFAULT"].get("root_dir", "nothing but tenticels and disapointment. . . ")
    organized_files_dir = config["DEFAULT"].get("organized_files_dir", "nothing but tenticels and disapointment. . . ")

    print("you could also run `python -i main.py` from the same dir to load the functions :P ")


