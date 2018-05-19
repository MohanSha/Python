
# Description			: Scans the recyclebin and displays the files in there, originally got this script from the Violent Python book

import os					# Load the Module
import optparse			# Load the Module
from _winreg import *	# Load the Module

def sid2user(sid):		# Start of the function to gather the user
  try:
    key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList" + '\\' + sid)
    (value, type) = QueryValueEx(key, 'ProfileImagePath')
    user = value.split('\\')[-1]
    return user
  except:
    return sid


def returnDir():			# Start of the function to search through the recyclebin
  dirs=['c:\\Recycler\\','C:\\Recycled\\','C:\\$RECYCLE.BIN\\']
  #dirs=['c:\\$RECYCLE.BIN\\']
  for recycleDir in dirs:
    if os.path.isdir(recycleDir):
      return recycleDir
  return None
  
def findRecycled(recycleDir):	# Start of the function, list the contents of the recyclebin
  dirList = os.listdir(recycleDir)
  for sid in dirList:
    files = os.listdir(recycleDir + sid)
    user = sid2user(sid)
    print '\n[*] Listing Files for User: ' + str(user)
    for file in files:
      print '[+] Found File: ' + str(file)

def main():
  recycleDir = returnDir()
  findRecycled(recycleDir)
  
if __name__ == '__main__':
  main()