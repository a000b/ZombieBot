import gnupg

def list(gpg_object, key_dic={}):
    for key in gpg_object.list_keys():
        key_dic.update({key['keyid']: key['uids']})
    return key_dic

def encrypt(gpg_object,input_file, recipients_list, output_file):
    with open(input_file, 'rb') as f:
        status = gpg_object.encrypt_file(
            f, recipients=recipients_list,
            output=output_file)
        return status

def decrypt(gpg_object, input_file, passphrase, output_file):
    with open(input_file, 'rb') as f:
        status = gpg_object.decrypt_file(f, passphrase=passphrase, output=output_file)
    return status

# def sign(gpg_object, input_file, passphrase, output_file):
#     with open(input_file, 'rb') as f:
#         status = gpg_object.
#     return status

def main():
    gpg_path = 'HOME$/.gnupg' #ścieżka do gpg
    input_file = 'logs.log'
    recipients = ['jon.doe@domain.com'] #klucz pub musi być zaimportowany do gpg
    encrypted = 'logs.txt.gpg'

    gpg = gnupg.GPG(gnupghome=gpg_path)
    #szyfrowanie
    status = encrypt(gpg,input_file,recipients,'logs.txt.gpg')

    #odszyfrowanie
    # status = decrypt(gpg, encrypted,input("p: "), 'decryped.txt')

    #status
    # print('ok: ', status.ok)
    # print('status: ', status.status)
    # print('stderr: ', status.stderr)

main()