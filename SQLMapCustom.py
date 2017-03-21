# coding=UTF-8
import os
import socket
import operator
from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

print """


███████╗ ██████╗ ██╗         ███╗   ███╗ █████╗ ██████╗
██╔════╝██╔═══██╗██║         ████╗ ████║██╔══██╗██╔══██╗
███████╗██║   ██║██║         ██╔████╔██║███████║██████╔╝
╚════██║██║▄▄ ██║██║         ██║╚██╔╝██║██╔══██║██╔═══╝
███████║╚██████╔╝███████╗    ██║ ╚═╝ ██║██║  ██║██║
╚══════╝ ╚══▀▀═╝ ╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝

 ██████╗██╗   ██╗███████╗████████╗ ██████╗ ███╗   ███╗
██╔════╝██║   ██║██╔════╝╚══██╔══╝██╔═══██╗████╗ ████║
██║     ██║   ██║███████╗   ██║   ██║   ██║██╔████╔██║
██║     ██║   ██║╚════██║   ██║   ██║   ██║██║╚██╔╝██║
╚██████╗╚██████╔╝███████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝



"""
class Parameters_URL_Connect(object):
    def __init__ (self, URL, verbosity, detection_Level, detection_Risk, brute_Force_Checks, save_Traffic_File, save_Config):
        self.URL = URL
        self.verbosity = verbosity
        # self.tor = tor
        # self.check_Tor = check_Tor
        # self.delay = delay
        # self.timeout = timeout
        # self.retries = retries
        # self.optimization = optimization
        self.detection_Level = detection_Level
        self.detection_Risk = detection_Risk
        self.brute_Force_Checks = brute_Force_Checks
        self.save_Traffic_File = save_Traffic_File
        self.save_Config = save_Config
    @classmethod
    def from_input(cls):
        return cls(
            str(raw_input("Enter the URL you want to test: ")),
            str(raw_input("Enter the level of verbosity (how much text info it prints out) from 0 (none) to 6 (highest): ")),
            # str(raw_input("Type '--tor' to conceal your traffic in the Tor anonymity network: ")),
            # str(raw_input("Type '--check-tor' to verify that Tor is working: ")),
            # str(raw_input("Enter the number of seconds of delay: ")),
            # str(raw_input("Enter the number of seconds to wait before timing out: ")),
            # str(raw_input("Enter the number of retries after a time-out: ")),
            # str(raw_input("Enter any performance optimization features or '-o' for ALL: ")),
            str(raw_input("Enter the level of detecton tests, 1 (lowest) and 5 (highest): ")),
            str(raw_input("Enter the risk of tests to perform, 1 (lowest) and 3 (highest): ")),
            str(raw_input("Enter the type of brute-force checks you would like to perform, either or both, '--common-tables' or '--common-columns': ")),
            str(raw_input("Enter the path where you want to save the HTTP traffic file, /$PATH/FILE.TXT: ")),
            str(raw_input("Enter the path you want to save the CONFIG file, /$PATH/CONFIG.INI: "))

        )

class Parameters_DBMS_Connect(object):
    #[21:13:47] [CRITICAL] invalid target details, valid syntax is for instance 'mysql://USER:PASSWORD@DBMS_IP:DBMS_PORT/DATABASE_NAME' or 'access://DATABASE_FILEPATH'

    def __init__ (self, user, password, tor, check_Tor, dbms_IP, dbms_Port, db_Name, save_Traffic_File, save_Config, dump_Format):
        self.user = user
        self.password = password
        self.tor = tor
        self.check_Tor = check_Tor
        self.dbms_IP = dbms_IP
        self.dbms_Port = dbms_Port
        self.db_Name = db_Name
        self.save_Traffic_File = save_Traffic_File
        self.save_Config = save_Config
        self.dump_Format = dump_Format
        return
    @classmethod
    def from_input(cls):
        return cls(
            str(raw_input("USER: ")),
            str(raw_input("PASSWORD: ")),
            str(raw_input("Tor? Type '--tor': ")),
            str(raw_input("Check Tor functionality? '--check-tor': ")),
            str(raw_input("DBMS IP Address: ")),
            str(raw_input("DBMS Port: ")),
            str(raw_input("Traffic File Save Path: ")),
            str(raw_input("Config File Save Path: ")),
            str(raw_input("Dump File Format (CSV, HTML, SQLITE, etc.): "))

        )

class Parameters_Logfile_Connect(object):
    def __init__ ():
        return
    @classmethod
    def from_input(cls):
        return cls(

        )

class Parameters_Sitemap_Connect(object):
    def __init__ ():
        return
    @classmethod
    def from_input(cls):
        return cls(

        )

class Parameters_GoogleDork_Connect(object):
    def __init__ ():
        return
    @classmethod
    def from_input(cls):
        return cls(

        )

class Parameters_HTTP_Request_Load_Connect(object):
    def __init__ ():
        return
    @classmethod
    def from_input(cls):
        return cls(

        )

def URL_Connect():
        #def __init__ (self, URL, verbosity, tor, check_Tor, delay, timeout, retries, optimization, detection_Level, detection_Risk, brute_Force_Checks, save_Traffic_File, save_Config):
    URL_Connect = Parameters_URL_Connect.from_input()

    URL_Connect_cmd_string = "sqlmap -u {0} -v {1} --tor --check-tor -o --level={2} --risk={3} {4} -t {5} --save={6} --beep --dependencies".format(
                    URL_Connect.URL,
                    URL_Connect.verbosity,
                    URL_Connect.detection_Level,
                    URL_Connect.detection_Risk,
                    URL_Connect.brute_Force_Checks,
                    URL_Connect.save_Traffic_File,
                    URL_Connect.save_Config
    )
    print colored(URL_Connect_cmd_string,'red','on_white')
    os.system(URL_Connect_cmd_string)
    return
def DBMS_Connect():    #[21:13:47] [CRITICAL] invalid target details, valid syntax is for instance 'mysql://USER:PASSWORD@DBMS_IP:DBMS_PORT/DATABASE_NAME' or 'access://DATABASE_FILEPATH'
#save_Traffic_File, save_Config, dump_Format

    DBMS_Connect = Parameters_DBMS_Connect.from_input()
    URL_Conect_cmd_string = "sqlmap -d mysql://{0}:{1}@{2}:{3}/{4} -t {5} --save={6} --dump-format={7}".format(
                                                            DBMS_Connect.user,
                                                            DBMS_Connect.password,
                                                            DBMS_Connect.dbms_IP,
                                                            DBMS_Connect.dbms_Port,
                                                            DBMS_Connect.db_Name,
                                                            DBMS_Connect.save_Traffic_File,
                                                            DBMS_Connect.save_Config,
                                                            DBMS_Connect.dump_Format
    )
    return
def Logfile_Connect():
    return
def Sitemap_Connect():
    return
def GoogleDork_Connect():
    return
def HTTP_Request_Load():
    return
def Load_Config():
    Config_File_Path = str(raw_input("Enter the FULL PATH of your previous saved .ini file (example: /root/Documents/config.ini): "))
    os.system('sqlmap -c {0}').format(Config_File_Path)
    return

while True:

    print colored('SQLMap, is a MASSIVE PROGRAM, and I can only implement so many features that will be useful for your first scan','red','on_white')
    print """
    It is highly suggested that you actually learn how to use SQLMap, particularly how to
    A.\tcustomize your payload,
    B.\trun search queries,
    C.\tattempt to access a exposed or compromised SQL Database Management System in a post-exploitation campaign.

    But for first-timers, I have implemented the following options:

    1. URL Connect, vulnerability testing
    2. Direct Connection to the DBMS, requires username/password
    3. INCOMPLETE, Load a logfile from Burpsuite or WebScarab and parse targets
    4. INCOMPLETE, Load a sitemap (xml) file and parse targets
    5. INCOMPLETE, Process GoogleDork URLs as targets
    6. INCOMPLETE, Load HTTP Request from a file
    7. Load from a previous configuration file (Resume a previous scan)
    """
    print colored('#1 has THIRTEEN different variables that this program will ask you to fill in!','red','on_white')
    user_Choice = str(raw_input("Enter a option listed above: "))

    if user_Choice == "1":
        URL_Connect()
    elif user_Choice == "2":
        DBMS_Connect()
    elif user_Choice == "3":
        Logfile_Connect()
    elif user_Choice == "4":
        Sitemap_Connect()
    elif user_Choice == "5":
        GoogleDork_Connect()
    elif user_Choice == "6":
        HTTP_Request_Load()
    elif user_Choice == "7":
        Load_Config()
    else:
        print colored('You have entered a invalid option','red','on_white')
