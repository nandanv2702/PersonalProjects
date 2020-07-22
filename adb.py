import os

prefix = "/Users/nandanv/Downloads/apks/"

os.chdir("/Users/nandanv/Downloads/apks/")
files = os.listdir()
output = os.popen('adb devices')
if (len(output.read()) > 26):
    for file in files:
        if('.apk' in file):
            os.system('adb install ' + prefix + file)
#
# output = os.popen('adb shell pm list packages')
# # if "sharechat" in output.read():
# #     print('yes')
#
# foundString = output.read()
# ind = foundString.find("facebook")
# print(foundString[ind-100:ind+100])
# # print(type(output.read()))
