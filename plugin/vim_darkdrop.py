from crypto_functions import *
import hashlib
import vim

def DarkDropFile():
    password = 'testpassword'
    key = hashlib.sha256(password).digest()

    filename = str(random.randint(0, 0xFF)) + '.tmp'
    noteDump = open(filename, 'w')
    noteDump.write('\n'.join(vim.current.buffer))

    encrypt_file(key, filename);
    os.remove(os.path.abspath(filename))
    noteDump.close()

