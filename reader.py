import optparse

from NTStorage import NTStorage
import pickle
import time
import json
import matplotlib.pyplot as plt

class RobotRecorder:
    
    def __init__(self, options):
        with open(options.file, "rb") as f:
            self.session = pickle.load(f)
        
        with open(options.config) as config_file:
            self.config = json.load(config_file)
        
        if options.listkeys:
            for key in self.session.get_keys():
                print(key)
                
        f, axarr = plt.subplots(len(self.config["plots"]), sharex=True)
        
        for i, plot in enumerate(self.config["plots"]):
            for key in plot["keys"]:
                axarr[i].plot(self.session.get_times(key), self.session.get_values(key), label=key.replace("/SmartDashboard/", ""))
            
            if "highlight" in plot:
                for j, highlight in enumerate(plot["highlight"]):
                    spans = self.session.get_boolean_spans(highlight)
                    for span in spans:
                        axarr[i].axvspan(span[0], span[1], color=plot["highlightcolor"][j], alpha=0.5, label=highlight.replace("/SmartDashboard/", ""))
            
            axarr[i].set_title(plot["keys"][0].replace("/SmartDashboard/", ""))
            axarr[i].legend()
        
        #plt.title("Recorded Robot")
        plt.legend()
        plt.show()
    
if __name__ == '__main__':
    parser = optparse.OptionParser()
    
    parser.add_option('-f', '--file', default="saves/examples/CameraLowBar.ntstore",help="NTStorage file to be red")
    
    parser.add_option('-c', '--config', default="ExampleConfig.json", help='Config for graph layout')
    
    parser.add_option('-l', '--listkeys', default=False, action='store_true', help='Print out keys from dump')
    
    options, args = parser.parse_args()
        
    recorder = RobotRecorder(options)
    