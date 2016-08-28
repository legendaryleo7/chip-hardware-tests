import pid

class SousVide():
    def __init__(self, temp-sensor, output, setpoint, Kp, Ki, Kd, controllerdirection):
        self.temp = temp-sensor
        self.output = output
        self.pid = PID(self.temp, self.output, setpoint, Kp, Ki, Kd, controllerdirection )
        
    def run(self):
        self.pid.compute()
        
class SousVideRelay(SousVide):
        def __init__(self, windowsize=5000):
            self.windowsize = windowsize
            self.windowstarttime = lambda: int(round(time.time() * 1000))
            self.pid.set_output_limits(0, self.windowsize)
            self.pid.set_mode("automatic")
        
        def run(self):
            self.pid.compute()
            self.now = lambda: int(round(time.time() * 1000))
            if self.now - self.windowstarttime > self.windowsize:
                self.windowstarttime += self.windowsize
            
            if self.pid.output > self.now - self.windowstarttime:
                GPIO.set_mode(self.output, GPIO.LOW)
            else 
                GPIO.set_mode(self.output, GPIO.HIGH)    