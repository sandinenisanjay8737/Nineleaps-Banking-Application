import time,sys

class Loading:
    animation = ["■□□□□□□□□□","■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□", "■■■■■■□□□□",
                "■■■■■■■□□□", "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■"]

    def processing(self):
        print()
        for i in range(len(self.animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + self.animation[i % len(self.animation)])
            sys.stdout.flush()
        print()


