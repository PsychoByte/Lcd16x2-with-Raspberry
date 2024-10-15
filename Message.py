import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import time

# Setup GPIO mode (BCM or BOARD)
# If using BOARD mode, use the physical pin numbers of the Raspberry Pi

# If using BCM mode, reference the GPIO pins directly
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connections
leg1 = 12  # Example GPIO pin
leg2 = 7   # Example GPIO pin
leg3 = 8   # Example GPIO pin
leg4 = 25  # Example GPIO pin
leg5 = 23  # Example GPIO pin

# Initialize the LCD with the correct pins
lcd = LCD.Adafruit_CharLCD(leg1, leg2, leg3, leg4, leg5, 0, 16, 2)

# Display a message on the LCD
lcd.message("PsychoByte GitHub")

# Delay for the message to be displayed
time.sleep(5)

# Clean up the GPIO pins after use
GPIO.cleanup()
