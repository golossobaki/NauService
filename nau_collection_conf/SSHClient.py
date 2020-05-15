import paramiko


def GetFile(host, path, file_name):
    user = 'root'
    secret = '123456'
    port = 22
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)
    #    stdin, stdout, stderr = client.exec_command('ls -l')
    #    data = stdout.read() + stderr.read()

    sftp_client = client.open_sftp()
    remote_file = sftp_client.open(path + file_name)
    lines = []
    try:
        for line in remote_file:
            lines.append(line)
    finally:
        remote_file.close()
    client.close()
    return lines
