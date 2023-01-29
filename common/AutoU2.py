import uiautomator2 as u2
from common import ConfigUtils
class AutoU2:

    def __init__(self):
        self.device = ConfigUtils.get('adb_host_port')
        self.d = u2.connect(self.device)

    def start(self):
        if self.d:
            self.d.service("uiautomator").start()
    
    def stop(self):
        if self.d:
            self.d.service("uiautomator").stop()

    def getD(self):
        return self.d