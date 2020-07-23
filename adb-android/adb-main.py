import os

prefix = "/Users/nandanv/Downloads/apks/"

os.chdir("/Users/nandanv/Downloads/apks/")
files = os.listdir()
output = os.popen('adb devices')
if (len(output.read()) > 26):
    for file in files:
        if('.apk' in file):
            os.system('adb install ' + prefix + file)

# checking difference after manually uninstalling
preins = open('preins.txt', 'r')
unins = open('unins.txt', 'r')

preins_apps = []
unins_apps = []

if unins.mode == 'r' and preins.mode == 'r':
    contents = preins.read().splitlines()
    for line in contents:
        preins_apps.append(line)

    contents = ''
    contents = unins.read().splitlines()
    for line in contents:
        unins_apps.append(line)

unins.close()
preins.close()

uninstall = []

for i in range(len(preins_apps)):
    if preins_apps[i] not in unins_apps:
        uninstall.append(preins_apps[i].replace('package:',''))

# uninstalls each app in the above array
for app in uninstall:
    try:
        os.system('adb uninstall ' + app)
    except:
        print("An exception occurred")
