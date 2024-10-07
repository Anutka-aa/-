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
        user_exist = False
        for user in self.users:
            if user['nickname'] == nickname:
                user_exist = True
                print(f'Пользователь {nickname} уже существует')
                break
            if not user_exist:
                new_user = {'nickname' = nickname, 'password' = password, 'age' = age}
                self.users.append(new_user)
                self.current_user = new_user


    def log_out(self):
        self.current_user = None
        print('Пользователь разлогинен')

    def add(self, *videos):
        for video in videos:
            video_exists = False
            for v in self.videos:
                if v['name'] == video.name:
                    video_exists = True
                    break
            if not video_exists:
                self.videos.append({'name': video.name})
                print(f'Видео {video.name} добавлено')

    def get_videos(self, search_word):
        search_word = search_word.lower()
        result = []
        for title, description in self.videos.items():
            if search_word in description.lower():
                result.append(title)
        return result

    def watch_video(self, video_title):
        if video_title in self.videos:
            self.current_video = video_title
            self.current_time = 0
            print(f"Смотрю {video_title} с {self.current_time} секунды")
        else:
            print("Видео не найдено")
