import sys
import subprocess

def clip(output):
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode())

# takes the argument from your terminal, stores it in a variable, splits that variable by '?source' (the point where Medium knows you're clicking this link from your email)

link = sys.argv[1]

link = link.split('?source')

# stores the basic link to the article

final_link = link[0]

# copies the link to your clipboard so you can directly paste it in your browser

clip(final_link)
