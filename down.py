import os
from webdav3.client import Client
from pathlib import Path

options = {
 'webdav_hostname': 'https://surfdrive.surf.nl/files/public.php/webdav/',
 'webdav_login': 'KisXdyS1duLXkxa',
 'webdav_password': 'jgq!khp6MFC3prv.tmn'
}

client = Client(options)
client.download_sync(remote_path="/", local_path=Path(__file__).parent)