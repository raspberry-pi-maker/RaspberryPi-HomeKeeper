#!/usr/bin/env python
from pushetta import Pushetta
    
API_KEY="your_key"
CHANNEL_NAME="HomeKeeper"
p=Pushetta(API_KEY)
p.pushMessage(CHANNEL_NAME, "Hello World From MotionEye")


