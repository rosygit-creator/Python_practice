
from enum import Enum

import logging
import unittest
import time
import threading

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Microwave:

    # different modes in microwave
    modes = {"cook": {"duration": 10}, "grill":{"duration": 7}, "defrost":{"duration": 5}, "popcorn": {"duration": 3}, "default": {"duration": 1}}

    def __init__(self, mode=None, door_closed=True):
        # initialize attributes
        self.mode=mode
        self.running=False # stores the start/stop state of the microwave
        self.door_closed=door_closed # stores the door open/close state of the microwave
        if self.mode:
            self.duration = Microwave.modes[self.mode]["duration"]
            self._duration_lock = threading.Lock()
        

    def open_door(self):
        self.door_closed=False
        self.running=False

    def close_door(self):
        self.door_closed = True

    # add duration for microwave
    def add_duration(self, duration):
        with self._duration_lock:
            self.duration += duration
            logging.info("Microwave will run for additional {} secs".format(duration))

    # start button
    def start(self):
        if not self.door_closed:
            print("Door is open: cannot start the microwave")
            return

        if not self.mode:
            self.mode = "default"
            self.duration = Microwave.modes["default"]["duration"]
        
        self.running=True

        while True:
            with self._duration_lock:
                if not (self.duration > 0 and self.door_closed and self.running):
                    break
                logging.info("Microwave started in {} mode with {} secs remaining".format(self.mode, self.duration))
                time.sleep(1)
                self.duration -= 1

        self.running=False


    # stop button
    def stop(self):
        if not self.running:
            print("Microwave stopped")
            return

        self.running=False
        print("Microwave stopped")


# testcases for the microwave implementation
class TestMicrowave(unittest.TestCase):
    def setUp(self):
        print(f"\nRunning test: {self._testMethodName}")

    # default mode
    def test_default_mode(self): 
        self.mw = Microwave("default")
        self.mw.start()
        del self.mw
    
    # test cook mode
    def test_cook_mode(self):
        self.mw = Microwave("cook")
        self.mw.start()
        del self.mw
    
    # test grill mode
    def test_grill_mode(self):
        self.mw = Microwave("grill")
        self.mw.start()
        del self.mw

    # test defrost mode
    def test_defrost_mode(self):
        self.mw = Microwave("defrost")
        self.mw.start()
        del self.mw

    # test popcorn mode
    def test_popcorn_mode(self):
        self.mw = Microwave("popcorn")
        self.mw.start()
        del self.mw

    # test adding duration in between while one of the modes is initialized
    def test_add_duration(self):
        self.mw = Microwave("cook")
        timer = threading.Timer(4.0, self.mw.add_duration, args=(5,))
        timer.start()
        self.mw.start()
        del self.mw