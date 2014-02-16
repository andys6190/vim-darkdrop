import gnupg

def DarkDropFile():
    gpg = gnupg.GPG(gnupghome='/home/asiradas/.securenotes')

    if not gpg.list_keys():
        key = gpg.gen_key(str(gpg.gen_key_input()))
    else:
        key = gpg.list_keys()[0]['fingerprint']

    importResult = gpg.import_keys(str(key))

    text = vim.current.buffer.range('1','$')
    print text.start
