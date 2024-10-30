import hashlib
import sys
import requests


class Connect:
    ip_address: str = ""
    _itl_signature: dict = {}

    def __init__(self, ip_address, itl_lookup_device: str = None):
        self.ip_address = ip_address
        if itl_lookup_device:
            itl = self.itl_signature(itl_lookup_device)

    def download(self, filename: str, file_path: str = "") -> bytes:
        try:
            file = requests.get(f"http://{self.ip_address}:6970/{filename}").content
        except Exception as err:
            print(f"Error downloading TFTP {filename}: {err}", file=sys.stderr)
        else:
            if file_path:
                with open(file_path, "wb") as wav_file:
                    wav_file.write(file)
            return file

    @staticmethod
    def fingerprint(itl):
        itl = itl.hexdigest().upper()
        i = 0
        return_fingerprint = ""
        while i < len(itl):
            return_fingerprint += itl[i]
            return_fingerprint += itl[i+1]
            return_fingerprint += " "
            i += 2

        return return_fingerprint.strip()

    def itl_signature(self, phone_name: str = None, flatten: bool = False):
        if phone_name:
            if len(phone_name) == 12:
                phone_name = f"SEP{phone_name.upper()}"

            itl_file = requests.get(f"http://{self.ip_address}:6970/ITL{phone_name.upper()}.tlv").content
            self._itl_signature['md5'] = self.fingerprint(hashlib.md5(itl_file))
            self._itl_signature['sha1'] = self.fingerprint(hashlib.sha1(itl_file))
            self._itl_signature['sha512'] = self.fingerprint(hashlib.sha512(itl_file))

        if flatten:
            return_list = []
            for itl in self._itl_signature:
                return_list.append(self._itl_signature[itl])
            return return_list
        else:
            return self._itl_signature