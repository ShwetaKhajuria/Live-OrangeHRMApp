import configparser
from symtable import Class

configparser=configparser.RawConfigParser()
configparser.read(".//Config/config.ini")

class READCONFIG:
    @staticmethod
    def getapplicationurl():
        url= configparser.get("Staging DB info",'BaseURL')
        return url

    @staticmethod
    def getapplicationuserid():
        userid= configparser.get("Staging DB info",'UserName')
        return userid

    @staticmethod
    def getapplicationpassword():
        password= configparser.get("Staging DB info",'Password')
        return password


