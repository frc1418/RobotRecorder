from networktables import NetworkTable
import optparse

import logging
logger = logging.getLogger('dashboard')
log_datefmt = "%H:%M:%S"
log_format = "%(asctime)s:%(msecs)03d %(levelname)-8s: %(name)-20s: %(message)s"

from NTStorage import NTStorage
import pickle
import time

class RobotRecorder:
    
    def __init__(self, options):
        NetworkTable.setIPAddress(options.ip)
        NetworkTable.setClientMode()
        NetworkTable.initialize()
        logger.debug("Networktables Initialized")
        
        self.current_session = None
        
        self.sd = NetworkTable.getTable("/")
        self.sd.addConnectionListener(self)
        
        self.run()
    
    def connected(self, nt):
        logger.debug("NetworkTables Connected")
        self.new_recording_session()
    
    def disconnected(self, nt):
        logger.debug("NetworkTables Disconnected")
        self.sd.removeGlobalListener(self.updated_value)
        
        if self.current_session is not None:
            pickle.dump(self.current_session, open("saves/%s.ntstore" %(time.time()), "wb"))
            self.current_session = None
        
    def new_recording_session(self):
        self.current_session = NTStorage()
        self.sd.addGlobalListener(self.updated_value)
    
    def updated_value(self, key, value, isNew):
        if isNew:
            self.current_session.registar_key(key)
        self.current_session.put_value(key, value)
    
    def run(self):
        while True:
            pass
        
    
    
if __name__ == '__main__':
    parser = optparse.OptionParser()
    
    parser.add_option('--ip', default='127.0.0.1', help="Address of NetworkTable server")
    
    parser.add_option('-v', '--verbose', default=False, action='store_true', help='Enable verbose logging')
    
    options, args = parser.parse_args()
    
    # Setup logging
    logging.basicConfig(datefmt=log_datefmt, format=log_format, level=logging.DEBUG if options.verbose else logging.INFO)
    
    recorder = RobotRecorder(options)
    