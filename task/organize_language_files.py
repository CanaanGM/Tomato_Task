
import  os, shutil, argparse
from typing import Tuple

def create_dir_if_doesnt_exist(dir_path: str) -> None:
    """checks if the dir is there, and creates it if not

    Args:
        dir_path (str): path to the directory
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def move_file(file_path: str,dir_path:str ) -> None:
    """copies the files from one dir to another

    Args:
        file_path (str): source file path to be copied
        dir_path (str): distination where to copy to
    """
    # i understood from the pdf that we want to organize the files; meaning MOVE not copy them
    shutil.move(file_path, dir_path)

def load_config() -> Tuple[str, str]:
    """loads the source/dist dirs from `config.ini` and returns them. 

    Returns:
        Tuple[str, str]: (source_dir, dist_sir)
    """
    config = configparser.ConfigParser()
    config.read( os.path.join(os.path.abspath(os.getcwd()),"config.ini" ) )

    return (
        config["DEFAULT"].get("root_dir", ""),
        config["DEFAULT"].get("organized_files_dir", "")
    )

def parse_args() -> Tuple[str, str]:
    parser = argparse.ArgumentParser(description="🍅🍅 task",
                                      formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-version', action='version', version='Version ' + "0.0.5",
                        help='laZagne version')

    parser.add_argument('-s',
                        '--source',  
                        default=os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")), "files") ,
                        help='source dir where the unsorted files live')
    
    parser.add_argument('-d',
                        '--dist',  
                        default=os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")), "organized_files_dir") ,
                        help='dir where the files will be sorted in')
    
    args = parser.parse_args()

    return (args.source, args.dist)

def organize_files(root_dir: str, dist_dir:str) -> int:
    """Organizes the files from the `source dir` to the `dist dir`

    Args:
        root_dir (str): path to the source directory
        dist_dir (str): path to the distenation directory

    Returns:
        int: the length of the sorted directory. not recursive!
    """
    try:
        unsorted_files = os.listdir(root_dir)

        if len(unsorted_files) > 0: 
            for file_path in os.listdir(root_dir):
                file_name = file_path.split("-")[0]

                create_dir_if_doesnt_exist(os.path.join(dist_dir,file_name))

                if file_path.find(file_name) >= 0 :
                    move_file(os.path.join(root_dir, file_path), os.path.join(dist_dir,file_name))
            return len(os.listdir(dist_dir))
        print("there are NO files to sort Q~Q!")
        return -1
    except Exception as ex:
        print(ex)
        print("not really needed or placed correctly but meh")
        return -1

if __name__ == "__main__":


    root_dir, organized_files_dir = parse_args()
    
    total_files_sorted = organize_files(root_dir, organized_files_dir)

    # simulating a usage or something xD
    if total_files_sorted == -1 :
        print("do something depening on the failure")
    else:
        print("do something depening on the sucess")


