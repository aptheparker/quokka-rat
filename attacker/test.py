import subprocess

# ls 명령어 실행
output = subprocess.run('ls -a', shell=True, stdout=subprocess.PIPE, text=True)

# 결과 출력
print(output.stdout)