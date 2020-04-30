import shutil, os

os.chdir('C:\\')
shutil.copy('C:\\spam.txt', 'C:\\delicious')
shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
