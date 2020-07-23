import os

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

print(uninstall)


