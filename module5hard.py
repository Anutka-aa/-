class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


 class Video:
     def __init__(self, title, duration, time_now = 0, adult_mode = False):
         self.titlke = title
         self.duration = duration
         self.time_now = time_now
         self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password ):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return
        print('Такого пользователя не существует')

    def register(self, nickname, password, age):
        if nickname in self.users:
            raise ValueError("Пользователь с таким ником уже существует.")
        self.users[nickname] = User(nickname, password, age)
        print(f"Пользователь {nickname} успешно зарегистрирован.")


    def log_out(self, nickname):
        if nickname not in self.users:
            raise ValueError("Пользователь не найден.")

        print(f"Пользователь {nickname} успешно вышел из системы.")

    def add(self, title, description, adult_mode):
        video = Video(title, description, adult_mode)
        self.videos.append(video)
        print(f"Видео {title} успешно добавлено.")

     def get_videos(self):
        return [
            (video.title, video.description)
            for video in self.videos
            if not video.adult_mode or (video.adult_mode and any(user.adult_mode for user in self.users.values()))
        ]

    def watch_video(self, nickname, title):
        user = self.users.get(nickname)
        if not user:
            raise ValueError("Пользователь не найден.")

        for video in self.videos:
            if video.title.lower() == title.lower():
                if video.adult_mode and not user.adult_mode and user.age < 18:
                    raise ValueError("Доступ запрещен: это видео предназначено для взрослых.")
                video.time_now += 1  # Увеличение времени просмотра
                return f"Вы смотрите видео: {video.title} - {video.description} на секунде {video.time_now}"

        raise ValueError("Видео не найдено.")
