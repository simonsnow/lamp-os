from led_strip import LedStrip
import uasyncio as asyncio

# Configuration for the PIN and number of pixels of the base and shade LED strips
pixel_config = {   
    "base":  { "pin": 12, "pixels": 5 },
    "shade": { "pin": 13, "pixels": 5 }     
}

# We love lamp.
class Lamp:
    def __init__(self, name, base_color, shade_color):
        self.name = name
        self.behaviours = []
        self.shade = LedStrip(shade_color, pixel_config['shade']['pin'], pixel_config['shade']['pixels'])
        self.base = LedStrip(base_color, pixel_config['base']['pin'], pixel_config['base']['pixels'])
    
    def add_behaviour(self,behaviour_class):
        b = behaviour_class(self)
        print(b)
        asyncio.create_task(b.run())
        
        self.behaviours.append(b) 
        print("Behaviour added: %s" % (b))

    def reset():
        self.shade.reset()
        self.base.reset()

    # Wake up the lamp and kick off the main loop
    def wake(self):
        self.shade.off()
        self.base.off()
 
        asyncio.create_task(self.shade.fade_to(self.shade.color,20))
        asyncio.create_task(self.base.fade_to(self.base.color,20))

        asyncio.run(self.main())
    
    # The main loop
    async def main(self):
        print("%s is awake!" % (self.name))

        while True:
            await asyncio.sleep_ms(50)
