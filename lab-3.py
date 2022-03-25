from shlex import quote
import subprocess
import sys
import boto3
import datetime

s3 = boto3.client('s3')

def main(argv):
    cmd = argv
    log_file_name = datetime.datetime.tzinfo.now().strftime("%m_%d_%Y") + "_logfile"
    log_file_name = quote(log_file_name)
    kickoff_subprocess(cmd, log_file_name)
    upload_output_to_S3(log_file_name)

def kickoff_subprocess(cmd, log_file_name):
    process = subprocess.call(cmd, shell=True)
    file = open(log_file_name, "a+")
    timestamp = datetime.datetime.tzinfo.now().strftime("%m/%d/%Y, %H:%M:%S")
    timestamp = quote(timestamp)
    output = timestamp + " Command: "+ cmd[0] + " | Return Code: " + str(process) + "\n"
    output = quote(output)
    file.write(output)
    close(log_file_name)

def upload_output_to_S3(log_file_name):
    f = open(log_file_name, "rb")
    s3.upload_fileobj(f, "arn:aws:s3:::python-reviewer", log_file_name)
     f.close(log_file_name)
    

if __name__ == "__main__":
   main(sys.argv[1:])
