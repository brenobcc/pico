# Raspberry Pi Pico 2

## 📌 Projects

### 🌡️ Internal Temperature Reading

This code uses the Raspberry Pi Pico's internal sensor to measure temperature and display values in the console.

📄 **File:** `temperature.py`

🔹 **Features:**
- Measures temperature using the internal ADC.
- Converts sensor readings to Celsius.
- Displays values periodically in the terminal.

### 📡 Morse Code with LED

Convert text messages into Morse code and display them by blinking an LED! ✨

📄 **File:** `morse.py`

🔹 **Features:**
- Converts text into Morse code.
- Uses an LED to transmit the message in dots and dashes.
- Prompts the user for a new message to send.

### 💡 LED Blinking

A simple script to make the Raspberry Pi Pico's built-in LED blink. Ideal for testing digital output.

📄 **File:** `cronometer.py`

🔹 **Features:**
- Turns the built-in LED on and off every 0.5 seconds.

## 🛠️ How to Use

1. **Connect** the Raspberry Pi Pico to your computer.
2. **Copy** the desired code to the microcontroller.
3. **Run** the scripts using the MicroPython interpreter.

## ⚡ Technologies Used
- 🐍 **MicroPython**
- 🔌 **Raspberry Pi Pico 2**
- 💾 **`machine` library for GPIO and ADC**