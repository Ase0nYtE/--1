class TV:
    def on(self):
        print("TV is turned on")

    def off(self):
        print("TV is turned off")

    def set_channel(self, channel: str):
        print(f"TV switched to channel: {channel}")


class AudioSystem:
    def on(self):
        print("Audio system is turned on")

    def off(self):
        print("Audio system is turned off")

    def set_volume(self, level: int):
        print(f"Volume set to {level}%")


class DVDPlayer:
    def on(self):
        print("DVD player is turned on")

    def off(self):
        print("DVD player is turned off")

    def play(self, movie: str):
        print(f"Playing movie: {movie}")

    def pause(self):
        print("Playback paused")

    def stop(self):
        print("Playback stopped")


class GameConsole:
    def on(self):
        print("Game console is turned on")

    def off(self):
        print("Game console is turned off")

    def start_game(self, game: str):
        print(f"Starting game: {game}")


class HomeTheaterFacade:
    def __init__(self):
        self.tv = TV()
        self.audio = AudioSystem()
        self.dvd = DVDPlayer()
        self.console = GameConsole()

    def watch_movie(self, movie: str):
        print("=== Movie Mode ===")
        self.tv.on()
        self.audio.on()
        self.audio.set_volume(40)
        self.dvd.on()
        self.dvd.play(movie)
        print("Enjoy your movie!\n")

    def end_movie(self):
        print("=== Ending Movie Mode ===")
        self.dvd.stop()
        self.dvd.off()
        self.audio.off()
        self.tv.off()
        print("System turned off.\n")

    def listen_to_music(self):
        print("=== Music Mode ===")
        self.tv.on()
        self.tv.set_channel("Music Channel")
        self.audio.on()
        self.audio.set_volume(55)
        print("Music is playing. Enjoy!\n")

    def play_game(self, game: str):
        print("=== Game Mode ===")
        self.tv.on()
        self.audio.on()
        self.audio.set_volume(60)
        self.console.on()
        self.console.start_game(game)
        print("Have fun playing!\n")

    def shutdown(self):
        print("=== Full System Shutdown ===")
        self.console.off()
        self.dvd.off()
        self.audio.off()
        self.tv.off()
        print("All devices are turned off.\n")

    def set_volume(self, level: int):
        self.audio.set_volume(level)


if __name__ == "__main__":
    home = HomeTheaterFacade()

    home.watch_movie("Interstellar")
    home.set_volume(50)

    home.listen_to_music()

    home.play_game("Cyberpunk 2077")

    home.end_movie()
    home.shutdown()