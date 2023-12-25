import argparse
import tkinter as tk
import logging
import sys
from tkinter import filedialog
from pathlib import Path

from File_Sorter import FileSorter


def is_valid_directory(directory):
    return Path(directory).is_dir()

def run_file_sorter(directory):
    sorter = FileSorter(directory)
    sorter.sorting_files()
    sorter.creatingFolders()
    sorter.movingFiles()

def get_directory_from_user():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title='Select a direcetory containing files to be sorted', initialdir=Path(r'C:\Users\mjedr\Desktop'))

    if not directory:
        logging.error('No directory selected.')
        sys.exit()
    
    return directory

def main(directory=None):
    if not directory:
        directory = get_directory_from_user()
        
    if not is_valid_directory(directory):
        logging.error(f"Error {directory} is not a valid directory")
        return
     
    try:
        run_file_sorter(directory)
    except Exception as e:
        logging.error(f"An error occured: {e}")
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sort and organize files in a folder')
    parser.add_argument('directory', nargs='?', help='Path to the folder containing files to be stored')
    args = parser.parse_args()
    
    logging.basicConfig(level=logging.INFO)
    main(args.directory)
