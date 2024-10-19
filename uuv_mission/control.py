# control.py

class PDController:
    def __init__(self, KP: float = 0.15, KD: float = 0.6):
        self.KP = KP
        self.KD = KD
        self.previous_error = 0.0

    def compute_control(self, reference: float, output: float) -> float:
        # Calculate the error
        error = reference - output
        
        # Compute the control action
        control_action = (self.KP * error) + (self.KD * (error - self.previous_error))
        
        # Update the previous error
        self.previous_error = error
        
        return control_action
