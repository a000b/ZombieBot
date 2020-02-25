import gnupg

def encrypt(gpg_object,input_file, recipients_list, output_file):
    try:
       with open(input_file, 'rb') as f:
           status = gpg_object.encrypt_file(
               f, recipients=recipients_list,
               output=output_file)
       return status
    except:
       pass
    return None

def decrypt(gpg_object, input_file, passphrase, output_file):
    with open(input_file, 'rb') as f:
        status = gpg_object.decrypt_file(f, passphrase=passphrase, output=output_file)
    return status

def main():
    gpg_path = '/home/maciej/.gnupg'
    input_file = '/home/maciej/myfiles/logs.log'
    input_file2 = '/home/maciej/myfiles/jobs.txt'
    recipients = ['logs@qxz.pl']
    encrypted = '/var/www/html/logs.txt.gpg'
    encrypted2 = '/var/www/html/jobs.txt.gpg'
    gpg = gnupg.GPG(gnupghome=gpg_path)
    # status = decrypt(gpg, encrypted,input("p: "), 'decryped.txt')
    status = encrypt(gpg,input_file, recipients, encrypted)
    status2 = encrypt(gpg,input_file2, recipients, encrypted2)
    #print('ok: ', status.ok)
    #print('status: ', status.status)
    #print('stderr: ', status.stderr)

main()
