from pathlib import Path
import shutil
import logging
from datetime import datetime
from collections import defaultdict


class SortFiles():
    """Class for sorting and organizing files."""

    def __init__(self, download_path):
        logging.info('Files have been sorted')
        self.download_path = download_path

    def __del__(self):
        logging.info('Program termination')
    # 1.Odczyt wszystkich plików znajdujących się w katalogu, w postaci słownika gdzie key=rozszerznie, value=nazwa pliku
    def sortingFiles(self):
        all_files = defaultdict(dict)
        for file_path in Path(self.download_path).iterdir():
            if file_path.is_file():
                all_files[file_path.suffix.upper()][file_path.stem] = {}
                all_files[file_path.suffix.upper()][file_path.stem]['size'] = round(file_path.stat().st_size/1048576, 6)
                all_files[file_path.suffix.upper()][file_path.stem]['date'] = datetime.fromtimestamp(file_path.stat().st_ctime)
            
        self.all_files = all_files

    def creatingFolders(self):
        years = set()
        extensions = set()

    #Stworzenie list rozszerzeń i roku utworzenia pliku
        for folder in self.all_files:
            extensions.add(folder[1:])
            years.update(file_info['date'].year for file_info in self.all_files[folder].values())

    #Utworzenie folderów z datami oraz plików rozszer         
        for date in years:
            folder_path_dates = Path(self.download_path) / str(date)
            if not folder_path_dates.exists():
                folder_path_dates.mkdir(parents=True, exist_ok=False)

            for extension in extensions:
                folder_path_extension = folder_path_dates / str(extension)
                if not folder_path_extension.exists():
                    folder_path_extension.mkdir(parents=True, exist_ok=False)
              
    def movingFiles(self):
        for ext in self.all_files:
            for f in self.all_files[ext]:
                year = self.all_files[ext][f]['date'].year
                filename = f + ext
                file_path = Path(self.download_path) / filename
                destinationPath = Path(self.download_path) / str(year) / ext[1:] / filename
                try:
                    shutil.move(file_path, destinationPath)
                except Exception as e:
                    logging.error(f"Error moving file {filename}: {e}")

        logging.info('Operatiton completed successfully')

if __name__== "__main__":
    download_path = r'C:\Users\mjedr\Desktop\Pobrane_Opera_test'
    logging.basicConfig(level=logging.INFO)

    sorter = SortFiles(download_path)
    sorter.sortingFiles()
    sorter.creatingFolders()
    sorter.movingFiles()


