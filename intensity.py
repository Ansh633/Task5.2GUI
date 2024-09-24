
import RPi.GPIO as GPIO  


import tkinter as tk    

# Set up GPIO using the BCM (Broadcom chip-specific) numbering
GPIO.setmode(GPIO.BCM)

# Define GPIO pin numbers for the red, green, and blue LEDs
RED_PIN = 18
GREEN_PIN = 22
BLUE_PIN = 23

# Set up the defined GPIO pins as output (since we are controlling LEDs)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Set up Pulse Width Modulation (PWM) on each pin with a frequency of 1000Hz
red_pwm = GPIO.PWM(RED_PIN, 1000)
green_pwm = GPIO.PWM(GREEN_PIN, 1000)
blue_pwm = GPIO.PWM(BLUE_PIN, 1000)

# Start PWM with an initial duty cycle of 0 (LEDs turned off)
red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

# Function to update the LED intensity based on the values of the sliders
def update_led_intensity():
    # Get the current values from the sliders
    red_intensity = red_slider.get()   # Red slider value (0-100)
    green_intensity = green_slider.get() # Green slider value (0-100)
    blue_intensity = blue_slider.get()  # Blue slider value (0-100)

    # Change the duty cycle of each LED to match the slider value
    # This adjusts the brightness of each LED
    red_pwm.ChangeDutyCycle(red_intensity)
    green_pwm.ChangeDutyCycle(green_intensity)
    blue_pwm.ChangeDutyCycle(blue_intensity)

# Function to turn off all the LEDs by setting duty cycle to 0
def turn_off_leds():
    # Turn off red LED
    red_pwm.ChangeDutyCycle(0)  
    # Turn off green LED
    green_pwm.ChangeDutyCycle(0)
    # Turn off blue LED
    blue_pwm.ChangeDutyCycle(0)  

# Function to exit the application and clean up the GPIO
def close_app():
    turn_off_leds()  # Turn off LEDs before exiting
    red_pwm.stop()   # Stop the PWM for red LED
    green_pwm.stop()  # Stop the PWM for green LED
    blue_pwm.stop()   # Stop the PWM for blue LED
    GPIO.cleanup()    # Reset the GPIO settings to default
    window.quit()     # Close the Tkinter window and exit the app

# Create the main window for the GUI
window = tk.Tk()
window.title("LED Intensity Controller")  # Set window title

# Create a label and a slider for adjusting the red LED intensity
red_label = tk.Label(window, text="Red LED Intensity")  # Label for red slider
red_label.pack()  # Display the label
red_slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda x: update_led_intensity())  
red_slider.pack()  # Display the slider

# Create a label and a slider for adjusting the green LED intensity
green_label = tk.Label(window, text="Green LED Intensity")  # Label for green slider
green_label.pack()  # Display the label
green_slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda x: update_led_intensity())
green_slider.pack()  # Display the slider

# Create a label and a slider for adjusting the blue LED intensity
blue_label = tk.Label(window, text="Blue LED Intensity")  # Label for blue slider
blue_label.pack()  # Display the label
blue_slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda x: update_led_intensity()) 
blue_slider.pack()  # Display the slider

# Create a button to turn off all LEDs
off_button = tk.Button(window, text="Turn Off All LEDs", command=turn_off_leds)  # Button to turn off LEDs
off_button.pack(pady=10)  # Display the button with padding

# Create an exit button to close the application and clean up GPIO
exit_button = tk.Button(window, text="Exit", command=close_app)  # Exit button
exit_button.pack(pady=10)  # Display the exit button with padding

# Main loop to keep the Tkinter window open and responsive
window.mainloop()
