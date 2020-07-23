import os

os.chdir("/Users/nandanv/Downloads/apks/")

output = os.popen('adb shell pm list packages')

# use for checking all apps that are installed on phone
# f = open('preins.txt', 'w+')

# manually uninstall bloatware and check all apps now - find the difference between both files
f = open('unins.txt', 'w+')

f.write(output.read())

f.close()
