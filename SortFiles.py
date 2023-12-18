from pathlib import Path
import shutil
from datetime import datetime
from collections import defaultdict


class SortFiles():
    """Pobiera dane ()"""

    def __init__(self, downloadPath):
        print('Pliki zostały posortowane')
        self.downloadPath = downloadPath

    def __del__(self):
        print('Zakończenie programu')
    # 1.Odczyt wszystkich plików znajdujących się w katalogu, w postaci słownika gdzie key=rozszerznie, value=nazwa pliku
    def sortingFiles(self):
        allFiles = defaultdict(dict)
        for file_path in Path(self.downloadPath).iterdir():
            if file_path.is_file():
                allFiles[file_path.suffix.upper()][file_path.stem] = {}
                allFiles[file_path.suffix.upper()][file_path.stem]['size'] = round(file_path.stat().st_size/1048576, 6)
                allFiles[file_path.suffix.upper()][file_path.stem]['date'] = datetime.fromtimestamp(file_path.stat().st_ctime)
            
        self.allFiles = allFiles

    def creatingFolders(self):
        years = []
        extensions = []

    #Stworzenie list rozszerzeń i roku utworzenia pliku
        for folder in self.allFiles:
            if folder not in extensions:
                extensions.append(folder[1:])

            for file in self.allFiles[folder]:
                date = self.allFiles[folder][file]['date']
                if date.year not in years:
                    years.append(date.year)

    #Utworzenie folderów z datami oraz plików rozszer         
        for date in years:
            folderPath_dates = Path(self.downloadPath) / str(date)
            if not folderPath_dates.exists():
                folderPath_dates.mkdir(parents=True, exist_ok=False)

            for extension in extensions:
                folderPath_extension = folderPath_dates / str(extension)
                if not folderPath_extension.exists():
                    folderPath_extension.mkdir(parents=True, exist_ok=False)
              
    def movingFiles(self):
        for ext in self.allFiles:
            for f in self.allFiles[ext]:
                year = self.allFiles[ext][f]['date'].year
                filename = f + ext
                filePath = Path(self.downloadPath) / filename
                destinationPath = Path(self.downloadPath) / str(year) / ext[1:] / filename
                shutil.move(filePath, destinationPath)
        print('Operacja przebiegła pomyślnie')

if __name__== "__main__":
    dp = r'C:\Users\mjedr\Desktop\Pobrane_Opera_test'
    sort = SortFiles(dp)
    sort.sortingFiles()
    sort.creatingFolders()
    sort.movingFiles()


