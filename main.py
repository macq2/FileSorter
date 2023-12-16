from pathlib import Path
import shutil
from datetime import datetime
from collections import defaultdict

dp = r'C:\Users\mjedr\Desktop\Pobrane_Opera_test'

# 1.Odczyt wszystkich plików znajdujących się w katalogu, w postaci słownika gdzie key=rozszerznie, value=nazwa pliku
def sortingFiles(downloadPath):
    allFiles = defaultdict(dict)
    for file_path in Path(downloadPath).iterdir():
        if file_path.is_file():
            allFiles[file_path.suffix][file_path.stem] = {}
            allFiles[file_path.suffix][file_path.stem]['size'] = round(file_path.stat().st_size/1048576, 6)
            allFiles[file_path.suffix][file_path.stem]['date'] = datetime.fromtimestamp(file_path.stat().st_ctime)
    
    print(allFiles)


# 2. Podział ich na date pobrania, utworzenie poszczególnych folderów z rokiem pobrania

# 3. Przeniesienie ich do poszczególnych folderów zgodnie z rozszerzeniami
# 4. Zrobienie wykresu, ile plików znajduje się w poszczególnych folderach (na osi X rok, na Y ilość plików pobranych)
# 5. Wykres 
sortingFiles(dp)