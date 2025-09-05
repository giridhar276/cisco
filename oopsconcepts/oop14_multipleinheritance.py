
class Phone:
    def call(self):
        print("Making a phone call...")

class Camera:
    def click(self):
        print("Taking a picture...")

class SmartPhone(Phone, Camera):
    def browse(self):
        print("Browsing internet...")

s = SmartPhone()
s.call()     # From Phone
s.click()    # From Camera
s.browse()   # Its own
