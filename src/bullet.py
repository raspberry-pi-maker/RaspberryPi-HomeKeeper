#!/usr/bin/env python
from pushbullet import Pushbullet

api_key = "your_access_token"
pb = Pushbullet(api_key)
push = pb.push_note("title", "MotionEye detects strange movement. Pls check the NAS")
