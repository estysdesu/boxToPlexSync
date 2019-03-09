from boxsdk import OAuth2, Client
from os import listdir
from os.path import isfile, join
import requests


def get_remote_files(client, shared_link_url):
    remote_folder = client.get_shared_item(shared_link_url)
    remote_files = remote_folder.get_items(limit=500, offset=0)
    return remote_files


def get_local_files(local_path):
    local_content = listdir(local_path)
    local_files = []
    for item in local_content:
        if isfile(join(local_path, item)):
            local_files.append(item)
    return local_files


def download_files(client, shared_link_url, local_path):
    remote_files = get_remote_files(client, shared_link_url)
    local_files = get_local_files(local_path)

    def compare_files(remote_files, local_files):
        files_to_download = []
        for remote_file in remote_files:
            if remote_file.name not in local_files:
                files_to_download.append(remote_file)
        return files_to_download

    files_to_download = compare_files(remote_files, local_files)
    for file_to_download in files_to_download:
        print("Downloading file")
        download_url = file_to_download.get_shared_link_download_url()
        filename = file_to_download.name
        r = requests.get(download_url, stream=True)
        with open(local_path + "/" + filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)


def run():
    oauth = OAuth2(
        client_id=None,
        client_secret=None,
        access_token=""
    )
    client = Client(oauth)
    shared_link_url = "https://uc.box.com/v/estests-videos"
    local_path = "/Users/tylerestes/BoxSync/Media/TEST"

    download_files(client, shared_link_url, local_path)


if __name__ == "__main__":
    run()
