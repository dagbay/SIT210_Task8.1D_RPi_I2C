from smbus import SMBus

addr = 0x8 # Address of where the byte will be sent to.
bus = SMBus(1) # Uses Port I2C1

num = 1

try:
    while num == 1:
        
        try:
            led_state = int(input("Enter your choice (1/0): "))
        except:
            continue
        
        if led_state == 1:
            bus.write_byte(addr, 0x1) # Sends a single byte to the slave device which will turn off the in-built LED.
        elif led_state == 0:
            bus.write_byte(addr, 0x0) # Sends a single byte to the slave device which will turn on the in-built LED.
        else:
            num = 0
            
except KeyboardInterrupt:
    bus.write_byte(addr, 0x0) # Sends a single byte to the slave device which will turn off the in-built LED if the Keyboard has been interrupted.
