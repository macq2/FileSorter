import SortFiles as p

def main(path):
    sort = p.SortFiles(path)
    sort.sortingFiles()
    sort.creatingFolders()
    sort.movingFiles()


folderPath = r'C:\Users\mjedr\Desktop\Pobrane_Opera_test'
main(folderPath)
# 4. Zrobienie wykresu, ile plików znajduje się w poszczególnych folderach (na osi X rok, na Y ilość plików pobranych)
# 5. Wykres 
