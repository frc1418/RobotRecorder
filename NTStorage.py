import time

class NTStorage():
    def __init__(self):
        self.vars = {}
        self.last_recorded_time = None;
        self.listeners = []
        
        self.reset_timer()
    
    def reset_timer(self):
        self.start_time = time.time()  
    
    def registar_key(self, key):
        self.vars[key] = [[],[]]
        
    def put_value(self, key, value):
        time_now = time.time() - self.start_time
        self.last_recorded_time = time_now
        
        self.vars[key][0].append(time_now)
        self.vars[key][1].append(value)
        
        self._fire_listener(key, self.vars[key])
        
    def get_key(self, key):
        try:
            return self.vars[key]
        except KeyError:
            return None
    
    def set_key(self, key, values):
        self.vars[key] = values
    
    def get_times(self, key):
        try:
            return self.vars[key][0]
        except KeyError:
            return None
    
    def get_values(self, key):
        try:
            return self.vars[key][1]
        except KeyError:
            return None
    
    def get_boolean_spans(self, key, inverted=False):
        '''returns the time spans of true values'''
        if not isinstance(self.vars[key][1][0], bool):
            return None
        
        true_spans = []
        
        #print(self.vars[key])
        
        times = self.vars[key][0]
        values = self.vars[key][1]
        
        for i,value in enumerate(values):
            if inverted == value and i-1 > -1:
                true_spans.append([times[i-1], times[i]])
        
        if values[len(values)-1]:
            true_spans.append([times[len(times)-1], self.last_recorded_time])
        
        #print(true_spans)
        return true_spans
    
    def get_keys(self):
        return self.vars.keys()
    
    def add_listener(self, callable):
        '''Fires every time verable is changed
            
            :param callable: A callable that has this signature: `callable(key, value)`
        '''
        self.listeners.append(callable)
    
    def _fire_listener(self, key, value):
        for listener in self.listeners:
            listener(key, value)
        