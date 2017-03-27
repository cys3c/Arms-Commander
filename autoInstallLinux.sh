#Execute script by typing either ./autoInstallLinux.sh OR
#/root/$PATH/ExtractedDirectory/autoInstallLinux.sh OR
#/home/USER/$PATH/ExtractedDirectory/autoInstallLinux.sh

#Only works in Kali Linux
#move entire directory for ArmsCommander to /root directory
mkdir /root/ArmsCommander #creates the new directory
cp -r ./ /root/ArmsCommander #copies contents to the new directory
cp /root/ArmsCommander/Launch\ Arms\ Commander.desktop /root/Desktop # move launcher icon to Desktop for Kali Linux Desktop DIrectory
chmod 777 ./ArmsCommander.py #makes the launcher executable
cp -r ./ArmsCommander.py /usr/local/bin #copies the main launcher into the /usr/local/bin directory, allowing someone to start AC by typing "ArmsCommander.py" in terminal
