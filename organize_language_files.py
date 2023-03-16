
# you've files and u'd want to group them by their name 
# arabic -> arabic dir. english -> english dir and so on
# match if the name of the file is the name of the dir and throw it there 
# end task

import  os, shutil, configparser
from typing import Tuple

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

def _load_config() -> Tuple[str, str]:
    config = configparser.ConfigParser()
    config.read("config.ini")

    return (
        config["DEFAULT"].get("root_dir", ""),
        config["DEFAULT"].get("organized_files_dir", "")
    )


def organize_files(root_dir: str, dist_dir:str) -> int:
    try:
        unsorted_files = os.listdir(root_dir)

        if len(unsorted_files) > 0: 
            for file in os.listdir(root_dir):
                # print(file)
                file_name = file.split("-")[0]

                # check if a dir with the name of the file exsists and create it 
                _create_dir_if_doesnt_exist(os.path.join(dist_dir,file_name))
                # move the file there 

                if file.find(file_name) >= 0 :
                    _move_file(os.path.join(root_dir, file), os.path.join(dist_dir,file_name))
            return len(os.listdir(dist_dir))
        print("there are NO files to sort Q~Q!")
        return -1
    except Exception as ex:
        print(ex)
        print("not really needed or placed correctly but meh")
        return -1

if __name__ == "__main__":
    

    root_dir, organized_files_dir = _load_config()

    total_files_sorted = organize_files(root_dir, organized_files_dir)

    print(f"total files sorted: {total_files_sorted}")


