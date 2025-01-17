# Learning
Learning Docker concepts
Steps :
If you are creating a software it needs environment like libs, options etc so to deploy on it its difficult.
To deploy we gonna use Container as docker which contaoins all to run in any system
KEY COMPONENTS:
Cointainers based on image
@Installation
~Windows
https://www.docker.com/products/docker-desktop - Download first depends on your |Sys requirement| when i was trying to install ARM64 it doesn't supported so i Used **AMD64**.
#TOOLS
https://git-scm.com/download/win   - download git for windows installer.

**Notes : I am doing side by side so don't worry. if any mistake comes we'll face together.**
# Setup
Go start search windows feature turn off/on then check these three which has tick mark
1. Hyper V
2. Windows subsystem for linux
3. Virtual Machine platform
[**Note i had only Windows subsytem for linux**]
need all three .
I am gonna install wsl how ? 
Search powershell and run as admin 
Prompt :  wsl --intstall ( it will take time for installing ubuntu)
It will ask you to create use name use your name default(case sensitive).
when entering password it won't show any so keep on mind, then restart computer.
Enter prompt :  wsl --set-default-version 2
for Hyper V install 
prompt : Get-ComputerInfo | Select-Object HyperVisorPresent
in windows feature tick windows hyperversion and restart.
next to verify docker install prompt : docker --version

"You will be pissed of for restarting often "
Last is git setup in shell 
1. git --version
2. 2.git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
3. git config --global core.autocrlf true
4. ssh-keygen -t ed25519 -C "your.email@example.com"
![image](https://github.com/user-attachments/assets/fd1c906d-c083-45aa-b400-3047654939f1)

Make sure login to docker lol.



