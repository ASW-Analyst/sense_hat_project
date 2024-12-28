from sense_hat import SenseHat
from datetime import datetime

class SenseHatMessage:
    def __init__(self, user_name = "Andy", scroll_speed = 0.05, text_colour = [255, 255, 255], back_colour = [0, 0, 0]):
        """
        Initialises the Sense HAT message with custom user arguments.

        :param user_name: The users name to be included in the message.
        :param scroll_speed: Speed at which the message scrolls on the LED matrix.
        :param text_colour: The RGB for controlling the colour of the scrolling text.
        :param back_colour: The RGB for controlling the background colour.
        """
        self.sense = SenseHat()
        self.user_name = user_name
        self.scroll_speed = scroll_speed
        self.text_colour = text_colour
        self.back_colour = back_colour

    def get_sensor_data(self):
        """
        Retrieves the current time, temperature and pressure data from the Sense HAT.
        :return: A tuple (current_time, current_temp, current_pressure)
        """
        current_time = datetime.now().strftime("%H:%M:%S")
        current_temp = self.sense.get_temperature()
        current_pressure = self.sense.get_pressure()
        return current_time, current_temp, current_pressure
    
    def create_message(self):
        """
        Creates a formatted message for displaying on the LED matrix.
        :return: A formatted string.
        """
        current_time, current_temp, current_pressure = self.get_sensor_data()
        return(
            f"Hello {self.user_name}! "
            f"At {current_time} "
            f"the temperature is {current_temp:.1f}C "
            f"and the pressure is {current_pressure:.1f}hPa"
        )
    
    def display_message(self):
        """
        Displays the formatted message on the LED matrix.
        """
        message = self.create_message()
        self.sense.clear()
        self.sense.show_message(
            message,
            scroll_speed = self.scroll_speed,
            text_colour = self.text_colour,
            back_colour = self.back_colour
        )
        self.sense.clear()

if __name__ == "__main__":
    sense_message = SenseHatMessage(user_name = "Andy")
    sense_message.display_message()
