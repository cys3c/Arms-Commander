# Arms-Commander
Malware Suite/Menu designed for "Speedy and No-Mistakes Penetration Testing", written in Python 2.7.13 and tested on Kali Linux 4.6, originally intended to only perform the Reconnaissance and Enumeration Stages (it's role is dramatically expanded now). Requires Python 2.7 + Pip + Termcolor Module. All code is entirely free to be used in your own projects. To install, you can either run the "autoInstallLinux.sh" script after "chmod 777" first, OR you can manually create the /root/ArmsCommander directory, copy everything in there, and then type "python /root/ArmsCommander/ArmsCommander.py"

# Installing Dependencies
#This will ensure that your version of Python is at least 2.7.13 and that Pip and Termcolor Modules are installed

Unzip the Arms-Commander.zip file
Navigate to directory
type "chmod 777 dependencyInstall.sh"
type "./dependencyInstall.sh"

# Installing the Malware Suite
#This will add a Desktop Launcher, as well as copy the main launcher into /usr/local/bin
#You will be able to run Arms-Commander by typing "ArmsCommander.py" in terminal

Unzip
Navigate to directory
type "chmod 777 autoInstallLinux.sh"
type "./autoInstallLinux.sh"
Run AC by typing "ArmsCommander.py" in Terminal
The main directory is /root/ArmsCommander

# NEW: First How-To Video, "2017: Generating a Resilient Metasploit Payload with EasyPeasey and Veil-Evasion"
https://github.com/tanc7/Arms-Commander/blob/master/DemonstrationOfFastPayloadGeneration.webm
This will walk you through the new revamped menu allowing you to (through msfvenom)...
1. Quickly choose a encoder
2. Select iterations to encode
3. Select a payload type/platform, arch
4. Further alter the signature of the payload with Veil-Evasion
5. Have a detection ratio of no more than 57% (according to VirusTotal, but then you gotta make a new one from scratch since it auto-submits to a database), or only 35 out of 61 antivirus programs are able to catch it via heuristics scanning.

# DISCLAIMER
#This is tested in Kali Linux ONLY
#For Ubuntu and other Debian Derivatives, a lot of commands that AC runs will not work in the first place because it requires System-Level Root
#For example, Metasploit requires root permissions or else you would get vague errors (try typing "route -n" as a regular user, and then as Root)

# Other Dependencies
#For reasons of your personal preference and security, I did not make it mandatory to install APKTools, Java or Ruby
#You will have to install them yourself if you want to use the APK Malware Injection Toolkit
#However, it's just a apt-get install away, and the required scripts and Java Signing Utilities are including in ArmsCommander regardless.

# Other Projects Pending (Notes by the Author for future patches/updates of ArmsCommander)
1. Consider adding a few of the things I learned from Violent Python, particularly the SSH Botnet Commander, as well as the SSH bruteforcer.
2. Disregard the SSH Hash brute-forcer from Violent Python, it MIGHT be bugged since it keeps returning broken keys
3. Incoporate the zip file cracker. Personally, I'd prefer just using the fcrackzip syntax because the Violent Python version appears to be bugged, it keeps returning more passwords after it found the first one. However, both fcrackzip and the Violent Python unzip.py managed to crack the password from the DarkComet release that I forked. The password for setup.zip is "infected", all lowercase, when using the RockYou wordlist.
4. For 7z file formats, which has much better encryption, consider http://davidalexandermejia.blogspot.com/2016/06/cracking-7z-files-using-john-ripper.html
5. Add the exifFetch.py program that I made from Violent Python. It seems really handy but hard to find image files with exif metadata (at least not ones with GPS metadata) these days.
6. "KtM Strike", or "Kill the Mailman Strike", it's the 2017 Adaption of the Kevin Mitnick Attack of December 25, 1994. It probably only works on low-end infrastructure websites, in other words, "personal sites" like... "My Cat Bob". I only managed to achieve this once and failed to take advantage of the window of opportunity in time. I need to replicate this, but due to the massive bandwidth capacity of modern broadband, it can take hours to properly match the TCP sequence. 
7. The "Twitter Stalker" Example in Chapter 6 of Violent Python is more of a proof of concept than anything concrete. For one, the author, probably out of concern on who would be reading his book, neglected to provide a complete dictionary of hashtags and geolocations to stalk the tweets of anyone other than the Red Sox. However, the social network info gathering part may be useful. It will take significantly more time to implement that however. Meanwhile, there are several APIs to consider. Facebook, MySpace, Tumblr, etc. Only two APIs were covered in detail, Twitter and Google.
8. Anonymous Googling part of Chapter 6 is indeed useful for those that are "paranoid". People still need to come to truths that there was never 100% privacy. A determined LE individual will still be able to get a ISP to reveal a person's info by order of a subpeona. 
