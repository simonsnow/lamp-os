# An example of a simple lamp on standard housing hardware with only basic behaviors enabled
# Lamp fades into a solid color and that's its thing for the night
from lamp_core.standard_lamp import StandardLamp

simple = StandardLamp(name="simple", base_color="#40B000", shade_color="#FFFFFF")
simple.wake()
