# An example of a simple lamp on standard housing hardware with all basic behaviors enabled
from lamp_core.standard_lamp import StandardLamp
from lamp_core.behaviour import Behaviour
from behaviours.lamp_fade_in import LampFadeIn
import uasyncio as asyncio

config = {
    "base":  { "pin": 12 },
    "shade": { "pin": 13 }
}

simple = StandardLamp("empress", "068f13", "c10ff7", config)
simple.wake()
