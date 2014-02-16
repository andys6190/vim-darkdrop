from crypto_functions import *
from secure import dropbox_keys
import hashlib
import vim
import dropbox
import os

def python_input(message = 'input'):
    vim.command('call inputsave()')
    vim.command("let user_input = input('" + message + ": ')")
    vim.command('call inputrestore()')
    return vim.eval('user_input')

def backup_to_cloud(filename, datadir, cloud_provider = 'dropbox'):
    cloud_provider = cloud_provider.lower()

    if cloud_provider == 'dropbox':
        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(dropbox_keys.DROPBOX_KEY, dropbox_keys.DROPBOX_SECRET)

        access_token_filename = datadir + 'access_token'

        if os.path.isfile(access_token_filename):
            with open(access_token_filename, 'r') as access_token_file:
                access_token = access_token_file.readline()
        else:
            authorize_url = flow.start()
            print '1. Go to: ' + authorize_url
            print '2. Click "Allow" (you might have to log in first)'
            print '3. Copy the authorization code.'
            code = python_input('authorization code')
            access_token, userId = flow.finish(code)

            with open(access_token_filename, 'w') as access_token_file:
                access_token_file.write(access_token)

        client = dropbox.client.DropboxClient(access_token)

        with open(filename + '.enc', 'rb') as encfile:
            client.put_file('/' + os.path.basename(filename), encfile)

def dark_drop_file():
    current_buffer = vim.current.buffer
    password = python_input('Password')
    key = hashlib.sha256(password).digest()

    datadir = os.path.expanduser('~') + '/.darkdrop/'
    if not os.path.exists(datadir):
        os.makedirs(datadir)

    buffname = os.path.basename(current_buffer.name).split('.')[0]
    filename = datadir + buffname + '.note'

    with open(filename, 'w') as note_dump:
        note_dump.write('\n'.join(current_buffer))

    encrypt_file(key, filename)

    # Dropbox backup
    backup_to_cloud(filename, datadir, 'dropbox')

    os.remove(filename)

