#JDownloader2 - DownloadsUnpacker
JDownloader2 music dirctory unpacker/sorter

This program:
- collect songs from the downloads directory
- renames the songs
- sorts the songs in your music directory
- if there is a directory with the same name as the song author, it will be moved i this directory

Icon: https://icons8.com/icon/pack/music/cute-clipart

---

Install
```bash
$ pip install -r requirements.txt
```

Build
```bash
$ pyinstaller --onefile --icon=icon.ico main.py
```