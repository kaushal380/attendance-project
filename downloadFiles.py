import io
import os
import pickle
import shutil
from mimetypes import MimeTypes

import requests
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload


class Drive:
    SCOPES = ["https://www.googleapis.com/auth/drive"]

    def __init__(self):
        self.creds = None

        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                self.creds = pickle.load(token)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", self.SCOPES
                )
                self.creds = flow.run_local_server(host="127.0.0.1", port=8000)
            with open("token.pickle", "wb") as token:
                pickle.dump(self.creds, token)
        self.service = build("drive", "v3", credentials=self.creds)
        results = (
            self.service.files()
            .list(
                pageSize=100,
                fields="files(id, name)",
            )
            .execute()
        )
        items = results.get("files", [])

        print("Here's a list of files: \n")
        # print(*items, sep="\n", end="\n\n")

        for i in range(len(items)):
            if((".jpg" in (items[i].get('name'))) or (".png" in (items[i].get('name')))):
                print(items[i])
        # for i in items:
        #     # print(i.get('id'), ' ', i.get('name'))
        #     name = i.get('name')
        #     print(name)

    def download(self, file_id, file_name):
        request = self.service.files().get_media(fileId=file_id)
        fh = io.BytesIO()

        downloader = MediaIoBaseDownload(fh, request, chunksize=204800)
        done = False

        try:
            while not done:
                status, done = downloader.next_chunk()

            fh.seek(0)

            with open(file_name, "wb") as f:
                shutil.copyfileobj(fh, f)

            print("File Downloaded")
            return True
        except:
            print("Something went wrong.")
            return False

    def upload(self, filepath):
        name = filepath.split("/")[-1]
        mimetype = MimeTypes().guess_type(name)[0]

        file_metadata = {"name": name}

        try:
            media = MediaFileUpload(filepath, mimetype=mimetype)

            file = (
                self.service.files()
                .create(body=file_metadata, media_body=media, fields="id")
                .execute()
            )

            print("File Uploaded.")

        except:
            print("unable to upload the file")
            # raise UploadError("Can't Upload File.")
def main():
    obj = Drive()
    action = 2
    # try:
    #     action = int(os.sys.argv[1])
    # except:
    #     help = f"USAGE: {os.sys.argv[0]} [1|2|3]\n1 - Download file, 2- Upload File, 3- Exit.\n"
    #     print(help)
    #     exit(0)

    if action == 1:
        f_id = input("Enter file id: ")
        f_name = input("Enter file name: ")
        obj.download(f_id, f_name)
    elif action == 2:
        f_path = input("Enter full file path: ")
        obj.upload(f_path)
    else:
        try:
            os.remove("token.pickle")
        except:
            pass
        finally:
            exit()
    try:
        os.remove("token.pickle")
        exit(0)
    except:
        exit(1)
main()