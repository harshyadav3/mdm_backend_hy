

class SharedObject:
    shared_instance = None

    def __init__ (self,value):
        if SharedObject.shared_instance is None :
            SharedObject.shared_instance = self 
            self.value = value 