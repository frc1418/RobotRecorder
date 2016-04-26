import matplotlib.pyplot as plt
import matplotlib.animation as animation

from NTStorage import NTStorage

class NTPlotter:
    
    def __init__(self, session, config, live=False):
        if not isinstance(session, NTStorage):
            raise('Session must be of type \'NTStroage\'')
        
        self.session = session
        self.config = config
        self.live = live
        
        self.f = None
        self.axarr = None
        
        self._setup_graph()
        
        if self.live:
            session.add_listener(self.update_listener)
            self.ani = animation.FuncAnimation(self.f, self.redraw, interval=1)
        
    def _setup_graph(self):
        if self.f is None or self.axarr is None:
            self.f, self.axarr = plt.subplots(len(self.config["plots"]), sharex=True)
            print(self.f)
        
        for i, plot in enumerate(self.config["plots"]):
            for j, key in enumerate(plot["keys"]):
                if plot["type"] == "xy":
                    if self.session.get_key(key) is not None:
                        self.axarr[i].plot(self.session.get_times(key), self.session.get_values(key), label=key.replace("/SmartDashboard/", ""))
                elif plot["type"] == "bool":
                    if self.session.get_key(key) is not None:
                        spans = self.session.get_boolean_spans(key)
                        for span in spans:
                            self.axarr[i].axvspan(span[0], span[1], color=plot["keycolors"][j], alpha=0.5, label=key.replace("/SmartDashboard/", ""))
                
            if "highlight" in plot:
                for j, highlight in enumerate(plot["highlight"]):
                    if self.session.get_key(highlight) is not None:
                        spans = self.session.get_boolean_spans(highlight)
                        for span in spans:
                            self.axarr[i].axvspan(span[0], span[1], color=plot["highlightcolor"][j], alpha=0.5, label=highlight.replace("/SmartDashboard/", ""))
                
            self.axarr[i].set_title(plot["keys"][0].replace("/SmartDashboard/", ""))
            self.axarr[i].legend()
            
    def show_graph(self):
        plt.legend()
        plt.show()
    
    def close(self):
        plt.close()
    
    def redraw(self ,i):
        for ax in self.axarr:
            ax.clear()
        self._setup_graph()
        
    def update_listener(self, key, values):
        self.session.set_key(key, values);