from pythontools.core import tools, logger
import os, time

downloads_path = os.getenv("HOMEPATH") + "\\Downloads"
logger.log("§rChecking directory '" + str(downloads_path) + "'")
music_path = os.getenv("HOMEPATH") + "\\\Music"
for dir in os.listdir(downloads_path):
    if tools.existDirectory(downloads_path + "\\" + dir):
        ok = False
        for file in os.listdir(downloads_path + "\\" + dir):
            file_ending = os.path.splitext(file)[1]
            if file_ending in [".ogg", ".mp3", ".m4a"]:
                try:
                    title = file.split("-")[1].split("(")[0].strip().replace(file_ending, "")
                    author = file.split("-")[0].strip()
                    file_path = music_path
                    def searchDir(path, name):
                        for d in os.listdir(path):
                            if tools.existDirectory(path + "\\" + d):
                                if d.lower() == name.lower(): return path + "\\" + d
                                result = searchDir(path + "\\" + d, name)
                                if result is not None: return result
                        return None
                    searched_dir = searchDir(music_path, author)
                    if searched_dir is not None:
                        file_path = searched_dir
                    try:
                        tools.copyFile(downloads_path + "\\" + dir + "\\" + file, file_path)
                        os.rename(file_path + "\\" + file, file_path + "\\" + title + " - " + author + file_ending)
                        logger.log("§aFile §e'" + str(title + " - " + author + os.path.splitext(file)[1]) + "'§a moved to '" + str(file_path) + "'")
                        ok = True
                    except:
                        logger.log("§cFailde to move file §e'" + str(title + " - " + author + os.path.splitext(file)[1]) + "'§c to '" + str(file_path) + "'")
                except: pass
        if ok is True:
            #logger.log("§rDirectory '" + downloads_path + "\\" + dir + "' removed")
            tools.clearDirectory(downloads_path + "\\" + dir)
            os.removedirs(downloads_path + "\\" + dir)

logger.log("§aFinished!")
time.sleep(3)
#pyinstaller --onefile --icon=icon.ico main.py
