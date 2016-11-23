import subprocess
import time
import sys
from functools import partial

# process = ["python", path + "cluster.py", data, str(num_clusters)]
# process = [

# try:
	# output = subprocess.check_output(process)
# except subprocess.CalledProcessError as e:
	# print "error"
	# print e.output

sshProcess = subprocess.Popen(["ssh", "-p", "2222", "vagrant@127.0.0.1", "-i", "C:\\Users\\danil\\Documents\\GitHub\\dmc\\.vagrant\\machines\\default\\virtualbox\\private_key"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
sshProcess.stdin.write("cd notebooks/workshop-2\n")
sshProcess.stdin.write("python test2.py\n")
sshProcess.stdin.close()

# print sshProcess.stdout

# for line in sshProcess.stdout:
    # if line == "END\n":
        # break
    # print line

output = []

for line in sshProcess.stdout:
	s = line.split("python: ")
	# print s
	if len(s) > 1:
		output.append(s[1].strip())

print output

# for line in  sshProcess.stdout:
#     if line == "END\n":
#         break
#     print line

