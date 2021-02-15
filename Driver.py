from gpiozero import LED

class Driver:
    def __init__(self, lforward, lbackward, rforward, rbackward):
        self.lf = LED(lforward)
        self.lb = LED(lbackward)
        self.rf = LED(rforward)
        self.rb = LED(rbackward)

    def forwards(self):
        self.lf.on()
        self.lb.off()
        
        self.rf.on()
        self.rb.off()

    def backwards(self):
        self.lf.off()
        self.lb.on()
        
        self.rf.off()
        self.rb.on()

    def stop(self):
        self.lf.off()
        self.lb.off()
        
        self.rf.off()
        self.rb.off()

    def right(self):
        self.lf.on()
        self.lb.off()
        
        self.rf.off()
        self.rb.on()

    def left(self):
        self.lf.off()
        self.lb.on()
        
        self.rf.on()
        self.rb.off()