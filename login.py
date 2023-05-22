import subprocess
import time


serialNumber = 'RQ8RB05G4TN' #Samsung SM-127F utilizado para teste, com as coordenadas do mesmo.
email = 'mgbrsg@gmail.com'
senha = 'senhateste'

#Abrindo app
subprocess.check_output(['adb', 'shell', 'am start -n io.ionic.starter/io.ionic.starter.MainActivity'])
time.sleep(5)

adb_command = f'adb shell input tap 903 1300' # Clica no campo de E-mail
subprocess.run(adb_command, shell=True)
time.sleep(3)

adb_command = f'adb shell input text "{email}"' # Insere o email
subprocess.run(adb_command, shell=True)
time.sleep(3)

adb_command = f'adb shell input tap 100 100' # Clica Fora
subprocess.run(adb_command, shell=True)

adb_command = f'adb shell input tap 520 1430'  # Clica no campo de Senha
subprocess.run(adb_command, shell=True)
time.sleep(3)

adb_command = f'adb shell input text "{senha}"' # Insere a senha
subprocess.run(adb_command, shell=True)
time.sleep(3)

adb_command = f'adb shell input tap 123 123' # Clica Fora
subprocess.run(adb_command, shell=True)
time.sleep(3)

adb_command = f'adb shell input tap 570 1700' # Clica no Botão login
subprocess.run(adb_command, shell=True)
