import shutil
import logging
import json
from datetime import datetime
from collections import defaultdict
from pathlib import Path

class FileSorter():
    """Class for sorting and organizing files."""


    def __init__(self, download_path):
        logging.info('Initializing...')
        self.download_path = download_path

    def __del__(self):
        logging.info('Program termination')


    def sorting_files(self):
        """Sort files and give information about extension, size and date to a dictionary"""

        logging.info('Sorting file...')
        all_files = defaultdict(dict)
        for file_path in Path(self.download_path).iterdir():
            if file_path.is_file():
                all_files[file_path.suffix.upper()][file_path.stem] = {}
                all_files[file_path.suffix.upper()][file_path.stem]['size'] = round(file_path.stat().st_size/1048576, 6)
                all_files[file_path.suffix.upper()][file_path.stem]['date'] = datetime.fromtimestamp(file_path.stat().st_mtime)
            
        self.all_files = all_files
        logging.info('Files sorting completed')

    def creatingFolders(self):
        """Create folder for each extension and file creation date"""

        logging.info('Creating folders...')
        folder_date = defaultdict(list)

        for ext in self.all_files.keys():
            for fname in self.all_files[ext].values():
                date_dict = fname['date'].year
                if ext[1:] not in folder_date[date_dict]:
                    folder_date[date_dict].append(ext[1:])

        for date in folder_date:
            folder_path_dates = Path(self.download_path) / str(date)
            if not folder_path_dates.exists():
                folder_path_dates.mkdir(parents=True, exist_ok=False)

            for file_ext in folder_date[date]:
                folder_path_extension = folder_path_dates / str(file_ext)
                if not folder_path_extension.exists():
                    folder_path_extension.mkdir(parents=True, exist_ok=False)               

        logging.info('Folder creation completed')

    def movingFiles(self):
        """Move file to a specific folder by extension and date"""

        output_dict = defaultdict(int)
        logging.info('Moving files...')

        for extension in self.all_files:
            for fname in self.all_files[extension]:
                year_output = self.all_files[extension][fname]['date']
                year_output_str = year_output.strftime('%Y-%m-%d')
                size_output = self.all_files[extension][fname]['size']
                output_dict[year_output_str] += size_output
                filename = fname + extension
                file_path = Path(self.download_path) / filename
                destinationPath = Path(self.download_path) / str(year_output.year) / extension[1:] / filename

                try:
                    shutil.move(file_path, destinationPath)
                except FileNotFoundError as e:
                    logging.error(f"File not found {filename}")
                except Exception as e:
                    logging.error(f"Error moving file {filename}: {e}")

        self.output_dict = output_dict
        logging.info('Files movement completed')


    def saving_dict(self):
        """Saving all needed data to .json file"""

        filename = 'data.json'

        try:
            with open(filename, 'r') as f:
                try:
                    existing_data = json.load(f)
                except json.decoder.JSONDecodeError:
                    existing_data = {}

            for key, value in self.output_dict.items():
                existing_data[key] = existing_data.get(key, 0) + value

            with open(filename, 'w') as f:
                json.dump(existing_data, f, indent=3)

            logging.info('Data has been saved')

        except FileNotFoundError:
            with open(filename, 'w'):
                pass

            logging.info('File has been created.')
            self.saving_dict()
        
        except Exception as e:
            logging.error(f"Error updating data: {e}")


if __name__== "__main__":
    download_path = r'C:\Users\mjedr\Desktop\Pobrane_Opera_test'
    logging.basicConfig(level=logging.INFO)

    sorter = FileSorter(download_path)
    sorter.sorting_files()
    sorter.creatingFolders()
    sorter.movingFiles()
    sorter.saving_dict()


