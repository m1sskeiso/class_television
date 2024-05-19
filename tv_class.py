# Create Phyton Code for creating the Class named TV and a Test Driver program named 
# TestTV that will create two objects from Class TV and will produce the following OUTPUT:

# tv1's channel is 30 and volume level is 3
# tv2's channel is 3 and volume level is 2

class TV:
    def __init__(self):
    # Initialize TV attributes
        self.channel = 1
        self.volume_level = 1
        self.on = False

    def turn_on(self):
        # Turn the TV on
        self.on = True

    def turn_off(self):
        # Turn the TV off
        self.on = False

    def set_channel(self, channel):
        # Set the TV channel if the TV is on and the channel is valid
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    def set_volume(self, volume_level):
        # Set the TV volume if the TV is on and the volume level is valid
        if self.on and 1 <= volume_level <= 7:
            self.volume_level = volume_level

    def channel_up(self):
    # Increment the TV channel if the TV is on and the channel is below 120

    def channel_down(self):
    # Decrement the TV channel if the TV is on and the channel is above 1
    
    def volume_up(self):
    # Increment the TV volume if the TV is on and the volume level is below 7

    def volume_down(self):
    # Decrement the TV volume if the TV is on and the volume level is above 1


    
