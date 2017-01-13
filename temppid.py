import time

class PID ():
	def __init__(self, feedback, setpoint, Kp, Ki, Kd, controllerdirection):
		self.feedback = feedback

        self.setpoint = setpoint
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.in_auto = False
        self.set_output_limits(0, 255) # default PWM output
        self.sample_time = 100          # default is .1 second
        self.set_controller_direction(controllerdirection)
        self.set_tunings(self.Kp, self.Ki, self.Kd)
        self.last_time = lambda: int(round(time.time() * 1000)) #- self.sample_time

	def compute(self):
		"""This, as they say, is where the magic happens. This function should be called 
		every time "void loop()" executes. The function will decide for itself whether a new 
		pid Output needs to be computed. Returns true when the output is computed, 
		false when nothing has been done."""

		if in_auto == False:
			self.now =  lambda: int(round(time.time() * 1000))
			self.time_change =  self.now - self.last_time
			
			if self.time_change >= self.sample_time:
				#Compute all the working error variables
				self.error = self.setpoint - self.feedback
				self.i_term += self.Ki * self.error
				
				if self.i_term > self.out_max:
					self.i_term = self.out_max
				elif self.i_term < self.out_min:
					self.i_term = self.out_min
				
				self.d_input = self.input - self.last_input
				
				# Compute PID Output
				self.output = self.Kp * self.error + self.i_term - self.Kd * self.d_input
				
				if self.output > self.out_max:
					self.output = self.out_max
				elif self.output < self.out_min:
					self.output = self.out_min
				
				# Remember some variables for next time
				self.last_input = self.input
				self.last_time = lambda: int(round(time.time() * 1000))
				return True
		else: 
			return False
		
	
	def set_tunings(self, Kp, Ki, Kd):
		"""This function allows the controller's dynamic performance to be adjusted.  
		it's called automatically from the constructor, but tunings can also 
		be adjusted on the fly during normal operation"""

		if Kp < 0 or Ki < 0 or Kd < 0:
			return
		else:
			self.dispKp = Kp
			self.dispKi = Ki
			self.dispKd = Kd
			
			self.Kp = Kp
			self.Ki = Ki * self.sample_time
			self.Kd = Kd * self.sample_time
			
			if controllerdirection == "Reverse":
				self.Kp = 0 - self.Kp
				self.Ki = 0 - self.Ki
				self.Kd = 0 - self.Kd

				
	def set_sample_time(self, new_sample_time):
		"""sets the period, in Milliseconds, at which the calculation is performed"""
		if new_sample_time > 0:
			ratio = new_sample_time / self.sample_time
			self.Ki *= ratio
			self.Kd /= ratio
			self.sample_time = new_sample_time
			
	def set_output_limits(self, min, max):
		"""This function will be used far more often than SetInputLimits.  while 
		the input to the controller will generally be in the 0-1023 range (which is 
		the default already,)  the output will be a little different.  maybe they'll 
		be doing a time window and will need 0-8000 or something.  or maybe they'll 
		want to clamp it from 0-125.  who knows.  at any rate, that can all be done 
		here."""
		if min > max:
			return
		else:
			self.out_min = min
			self.out_max = max
		
		if in_auto:
			if self.output > self.out_max:
					self.output = self.out_max
			elif self.output < self.out_min:
					self.output = self.out_min
			
			if self.i_term > self.out_max:
					self.i_term = self.out_max
			elif self.i_term < self.out_min:
					self.i_term = self.out_min
	def set_mode(self, mode):
		"""Allows the controller Mode to be set to manual (0) or Automatic (non-zero) 
		when the transition from manual to auto occurs, the controller is 
		automatically initialized"""

		self.new_auto = mode == 'automatic'
		
		if self.new_auto != self.in_auto:
			self.initialize();
		self.in_auto = self.new_auto
	
	def initialize(self):
		"""does all the things that need to happen to ensure a bumpless transfer 
		from manual to automatic mode."""
		self.i_term = self.output
		self.last_input = self.input
		if self.i_term > self.out_max:
			self.i_term = self.out_max
		elif self.i_term < self.out_min:
			self.i_term = self.out_min
	def set_controller_direction(self, direction):
		""" The PID will either be connected to a DIRECT acting process (+Output leads  
		to +Input) or a REVERSE acting process(+Output leads to -Input.)  we need to 
		know which one, because otherwise we may increase the output when we should 
		be decreasing.  This is called from the constructor."""
		if self.in_auto and direction != self.controllerdirection:
			self.Kp = 0 - self.Kp
			self.Ki = 0 - self.Ki
			self.Kd = 0 - self.Kd
			self.controllerdirection = direction
	def get_Kp(self):
		return self.dispKp
	def get_Ki(self):
		return self.dispKi
	def get_Kd(self):
		return self.dispKd
	def get_mode(self):
		if self/in_auto:
			return "AUTOMATIC"
		else:
			return "MANUAL"
	def get_direction(self):
		return self.controllerdirection