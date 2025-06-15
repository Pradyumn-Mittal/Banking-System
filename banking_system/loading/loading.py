import multiprocessing
import time


class Loading:
    def __init__(self) -> None:
        self.message = ''
        self.speed = 0.1

        self.process = multiprocessing.Process(
            target=self.spin,
            args=(),
            name="spinner"
        )

    def spin(self):
        spinner = ['-', '\\', '|', '/']
        n = 0
        while True:
            print(f'\r{self.message}{spinner[n]}', end='')
            n += 1
            if n >= len(spinner):
                n = 0
            time.sleep(self.speed)

    def start(self):
        print()
        self.process.start()

    def stop(self):
        if not self.process.is_alive():
            print("Loading not working...")
        else:
            self.process.terminate()
            print()

    def loading_anim(self, message, delay):
        self.message = message
        self.start()
        time.sleep(delay)
        self.stop()
