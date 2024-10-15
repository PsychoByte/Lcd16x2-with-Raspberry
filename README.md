# Interfacing 16x2 LCD with Raspberry Pi to Display Messages

This project demonstrates how to interface a 16x2 LCD with a Raspberry Pi to display custom messages. It includes the necessary components, wiring details, and instructions for setting up the connections and powering the circuit.

## Components

- Raspberry Pi (with internet connection via Wi-Fi/Ethernet)
- 16x2 LCD display
- Jumper wires 
- Potentiometer (for contrast adjustment) or 1kΩ to 5kΩ resistor any one
- Breadboard
- Power supply (for Raspberry Pi)
- HDMI Cable (Raspberry Pi to monitor connection)

## LCD Pin Connections

The following table shows how to connect the LCD to the Raspberry Pi. Each pin on the LCD has a specific function, and its connection to the Raspberry Pi is listed below:

| LCD Pin Number | LCD Pin Name     | Connection                                                |
| -------------- | ---------------- | --------------------------------------------------------- |
| 1              | VSS              | GND (Ground)                                              |
| 2              | VCC              | 5V (Power)                                                |
| 3              | VEE              | Resistor (One end to GND, other end to LCD Pin 3)          |
| 4              | RS               | Raspberry Pi Pin 32 (Physical Pin)                        |
| 5              | R/W              | GND                                                       |
| 6              | E                | Raspberry Pi Pin 26 (Physical Pin)                        |
| 7              | D0               | No connection (skip)                                      |
| 8              | D1               | No connection (skip)                                      |
| 9              | D2               | No connection (skip)                                      |
| 10             | D3               | No connection (skip)                                      |
| 11             | D4               | Raspberry Pi Pin 24 (Physical Pin)                        |
| 12             | D5               | Raspberry Pi Pin 22 (Physical Pin)                        |
| 13             | D6               | Raspberry Pi Pin 18 (Physical Pin)                        |
| 14             | D7               | Raspberry Pi Pin 16 (Physical Pin)                        |
| 15             | Backlight LED (+) | 5V (Power)                                                |
| 16             | Backlight LED (-) | GND (Ground)                                              |

## Breadboard Power Setup

To properly power the components, make sure to follow these steps:

1. Attach the 5V and GND pins of the Raspberry Pi to the positive and negative rails of the breadboard.  
    - Connect Raspberry Pi 5V (Pin 2) to the breadboard's positive rail.
    - Connect Raspberry Pi GND (Pin 6) to the breadboard's negative rail.
2. Use these rails to power other components (LCD and potentiometer/resistor).

Ensure all GND and 5V connections for the LCD and other components are routed through the breadboard, using the positive and negative rails.

---

## Steps to Set Up and Run the Code

### Step 1: Clone the Library Repository
Clone the necessary library for controlling the 16x2 LCD from GitHub:

```bash
git clone https://github.com/PsychoByte/Lcd16x2-with-Raspberry
```

### Step 2: Navigate to the Cloned Directory
Go to the directory where the repository was cloned and list the files:

```bash
cd Lcd16x2-with-Raspberry
ls
```

### Step 3: Run `setup.py` 
Check if the `setup.py` file exists. If it's available, run the following command to install the required dependencies:

```bash
sudo python3 setup.py install
```

### Step 4: Run the Script Manually
This step is optional. If you prefer, you can manually copy the code below into a "Script Code" and run it using a Python IDE like Thonny or IDLE. 
Alternatively, you can modify the `Message.py` file. To run the script with a custom message, edit the `Message.py` file line `lcd.message("Your Custom Message Here")` using nano/vim/texteditor:

Then, run the script using:

```bash
sudo python3 Message.py
```

---

## Script Code

Here is the Python code for controlling the 16x2 LCD:

```python
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
```

### Additional Notes:
- You can modify the GPIO pin numbers based on your specific wiring setup. 
- Use the `lcd.message()` function to display any text on the 16x2 LCD.
---

<h2 align="center" >Made with ❤️ by <a href="https://github.com/PsychoByte">PsychoByte</a></h2>
