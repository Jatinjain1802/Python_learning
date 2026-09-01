from typing_extensions import override
class wsp1():
    def send_message(self):
        print("single tick")

class wsp2(wsp1):
    def send_message(self):
        super().send_message()
        print("double tick")
    def send_audio(self):
        print("send audio msg")
        
class wsp3(wsp2):
    def send_message(self):
        super().send_message()
        print("Blue tick")
    def send_audio(self):
        super().send_audio()
        print("5 minutes audio")
    def send_video(self):
        print("send video")
        
class final_version(wsp3):
    @override
    def final_version(self):
        super().send_message()
        super().send_audio()
        super().send_video()
        print("latest version")

w=final_version()
w.final_version()



        