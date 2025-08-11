import sys
import time
import io
from collections import OrderedDict
import tarfile
from .Sheets import Sheet

class Tar:
    files = []
    header = None
    def __init__(self, tar_filename: str = None):
        self.files = []
        self.header = None
        if tar_filename:
            self.extract(tar_filename)
        self.generate_header()

    def add(self, file_name: str, sheet: str | dict | list[OrderedDict]) -> bool:
        if isinstance(sheet, list):
            pass
            # sheet = Sheet.export_csv(sheet)
        elif isinstance(sheet, dict):
            sheet = Sheet.export_csv(sheet, list(sheet.keys()))

        self.files.append(Sheet(name=file_name.strip(), sheet=sheet))
        self.generate_header()
        return True

    def remove(self, name: str) -> bool:
        file_index = self.find(name)
        if file_index >= 0:
            self.files.pop(file_index)
            self.generate_header()
            return True
        return False

    def extract(self, tar_path: str, detect_entity : bool = True) -> bool:
        try:
            with tarfile.open(tar_path, 'r') as tar:
                for member in tar.getmembers():
                    if member.isfile():  # Process only files, not directories
                        file_data = tar.extractfile(member)
                        if file_data:
                            content = file_data.read()
                            if member.name != "header.txt":
                                self.files.append(Sheet(name=member.name, sheet=content))
        except tarfile.ReadError:
            print(f"Error: Could not read tar file: {tar_path}", file=sys.stderr)
            return False
        except FileNotFoundError:
            print(f"Error: Tar file not found: {tar_path}", file=sys.stderr)
            return False
        return True

    def archive(self, include_header: bool = True) -> tarfile:
        tar_buffer = io.BytesIO()
        with tarfile.open(fileobj=tar_buffer, mode="w") as tar:
            if include_header:
                tarinfo = tarfile.TarInfo(name="header.txt")
                tarinfo.size = len(self.header)
                tar.addfile(tarinfo=tarinfo, fileobj=io.BytesIO(self.header.encode()))
            for file in self.files:
                tarinfo = tarfile.TarInfo(name=file.name)
                raw_data = file.raw()
                tarinfo.size = len(raw_data)
                tar.addfile(tarinfo=tarinfo, fileobj=io.BytesIO(raw_data))

        return tar_buffer.getvalue()

    def find(self, name: str) -> int:
        i = 0
        while i < len(self.files):
            if self.files[i].name == name.strip():
                return i
            i += 1
        return -1

    def generate_header(self) -> bool:
        current_timestamp = time.time()
        time_struct_utc = time.gmtime(current_timestamp)
        formatted_time = time.strftime("%b %d, %Y %I:%M:%S %p", time_struct_utc)
        final_timestamp_string = f"{formatted_time} GMT"

        listing = []
        self.remove("header.txt")
        for file in self.files:
            listing.append(file.name.lower().replace(".csv", "").replace(".txt", ""))

        header_file = f"Time : {final_timestamp_string}\n"
        header_file += "IP Address : 10.0.0.10\n"
        header_file += "CCM : master-12.5.1.12900-115.i386\n"
        if listing:
            header_file += "File : "
            header_file += f"\nFile : ".join(listing)

        self.header = header_file
        return True

    def save(self, tar_file: str, include_header: bool = True) -> bool:
        with open(tar_file, "wb") as f:
            f.write(self.archive(include_header))
        return True
