from ConfigDict import ConfigDict
import configparser

class Config():
    def __init__(self):
        self.section_dict = {}

    def getProperties(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
    
    def loadProperties(self):
        for each_section in self.config.sections():
            section = ConfigDict()
            for (each_key, each_val) in self.config.items(each_section):
                
                key_list = each_key.split('.')
                tmp = section

                for index, key in enumerate(key_list):
                    if key not in tmp:
                        if index == len(key_list)-1:
                            tmp[key] = each_val
                        else:
                            tmp[key] = ConfigDict()
                        tmp = tmp[key]
                    else:
                        tmp = tmp[key]
            self.section_dict[each_section] = section
    
        print(self.section_dict)
        print(self.section_dict['MODEL']['m4']['name'])
        print(self.section_dict['COMMON']['comm'])
        print(self.section_dict['COMMON']['comm']['mode'])
        print(self.section_dict['COMMON']['comm']['mode']['port'])

a = Config()
a.getProperties()
a.loadProperties()
