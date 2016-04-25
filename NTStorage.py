import time

class NTStorage():
    def __init__(self):
        self.vars = {}
        self.start_time = time.time()
        
    def registar_key(self, key):
        self.vars[key] = [[],[]]
        
    def put_value(self, key, value):
        self.vars[key][0].append(time.time()- self.start_time)
        self.vars[key][1].append(value)
        
    def get_key(self, key):
        return self.vars[key]
    
    def get_times(self, key):
        return self.vars[key][0]
    
    def get_values(self, key):
        return self.vars[key][1]
    
    def get_boolean_spans(self, key, inverted=False):
        '''returns the time spans of true values'''
        if not isinstance(self.vars[key][1][0], bool):
            return None
        
        true_spans = []
        
        times = self.vars[key][0]
        values = self.vars[key][1]
        
        for i,value in enumerate(values):
            if inverted == value and i-1 > -1:
                true_spans.append([times[i-1], times[i]])
        return true_spans
    
    def get_keys(self):
        return self.vars.keys()