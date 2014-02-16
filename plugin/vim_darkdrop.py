from crypto_functions import *
from getpass import getpass
import hashlib
import vim

def DarkDropFile():
    password = getpass()
    key = hashlib.sha256(password).digest()

    homedir = os.path.expanduser('~')
    filename = homedir + '/.securenotes/' + str(random.randint(0, 0xFF)) + '.tmp'
    noteDump = open(filename, 'w')
    noteDump.write('\n'.join(vim.current.buffer))

    encrypt_file(key, filename);
    os.remove(filename)
    noteDump.close()

