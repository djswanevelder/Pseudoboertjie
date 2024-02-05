import os
import urllib.request

def download_and_install_vscode():
    installer_url = "https://go.microsoft.com/fwlink/?LinkID=623548"
    installer_filename = "vscode.exe"

    # Download the installer
    urllib.request.urlretrieve(installer_url, installer_filename)

    # Run the installer
    os.startfile(installer_filename)

if __name__ == "__main__":
    download_and_install_vscode()

