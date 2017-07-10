from time import sleep
import subprocess
import logging
import os

def avgkill():
    logging.info('starting avgmfapx.exe') #this is the avg uninstaller
    subprocess.call('"C:\\Program Files (x86)\\AVG\\AV\\avgmfapx.exe"'
                     ' /Appmode=Setup /uninstall /uilevel=Silent', shell=True)

def still_run(process):
    running = subprocess.check_output('tasklist', shell=True)
    if process in running:
        sleep(5)
        logging.info('avgmfapx.exe is still running...')
        still_run(process)
    else:
        logging.info('avgmfapx.exe is complete, moving to cleanup.')
        cleanup()
        

def cleanup():
    try:
        subprocess.call('rd /s /q "C:\\programdata\\AVG"', 
                        shell=True)
        subprocess.call('rd /s /q "C:\\program files (x86)\\AVG"', 
                        shell=True)
        subprocess.call('rd /s /q "C:\\users\\%USERNAME%\\appdata\\local\\AVG"', 
                        shell=True)
        subprocess.call('rd /s /q "C:\\users\\%USERNAME%\\appdata\\roaming\\AVG"', 
                        shell=True)
        logging.info('cleanup successful.')
    except:
        logging.error('cleanup failed.')

def main():
    #this is where the log will go
    if not os.path.exists('C:\\avgkill'):
        os.makedirs('C:\\avgkill')
    logging.basicConfig(filename='C:\\avgkill\\avgkill.log',
                        level=logging.DEBUG)
    avgkill()
    still_run('avgsetupx.exe') #this is the parent process of avgmfapx

main()
