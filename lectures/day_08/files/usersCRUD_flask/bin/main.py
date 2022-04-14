import subprocess, os




def make_env():
    subprocess.run(["pipenv", "install", "flask", "pymysql"])
    subprocess.run(["pipenv", "shell"])

make_env()