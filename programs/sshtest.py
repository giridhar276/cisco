

# pip install paramiko
import paramiko

HOST, USER, PASS = "test.rebex.net", "demo", "password"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(HOST, 22, USER, PASS, look_for_keys=False)

# Run a simple command (may vary based on server capabilities)
stdin, stdout, stderr = client.exec_command("ls -la")
print(stdout.read().decode() or stderr.read().decode())

# SFTP: list and download
sftp = client.open_sftp()
print("Root:", sftp.listdir("."))
print("/pub/example:", sftp.listdir("/pub/example"))
sftp.get("/pub/example/readme.txt", "readme_sftp.txt")
sftp.close()
client.close()
print("Downloaded readme_sftp.txt")
