from django.db import models
# Create your models here.



class Bat(models.Model):
    """Летучая мышь с её описаниями"""
    id = models.AutoField(primary_key=True)
    # Номер
    number = models.CharField(max_length=20, default='Номер мыши')
    # Имя
    name = models.CharField(max_length=20, default='Имя мыши')
    # Пол
    SEX = [('M', 'Мужской'),
           ('F', 'Женский')
           ]
    sex = models.CharField(max_length=20, choices=SEX, default='M')
    # Кольцо
    ring = models.CharField(max_length=20, default='Номер кольца')

    # Тип летучей мыши

    PN = 'Прудовая ночница'
    VN = 'Водяная ночница'
    NONA = 'Ночница Наттерера'
    YN = 'Усатая ночница'
    BY = 'Бурый ушан'
    Y = 'Ушан'
    MV = 'Малая вечерница'
    RV = 'Рыжая вечерница'
    GV = 'Гигантская вечерница'
    NEKA = 'Нетопырь-карлик'
    NEKY = 'Нетопырь Куля'
    NN = 'Нетопырь Натузиус'
    SK = 'Северный кожанок'
    DK = 'Двухцветный кожан'
    PK = 'Поздний кожан'
    NB = 'Ночница Брандта'
    BATSPECIES = [(PN, 'Прудовая ночница'),
                (VN, 'Водяная ночница'),
                (NONA, 'Ночница Наттерера'),
                (YN, 'Усатая ночница'),
                (BY, 'Бурый ушан'),
                (Y, 'Ушан'),
                (MV, 'Малая вечерница'),
                (RV, 'Рыжая вечерница'),
                (GV, 'Гигантская вечерница'),
                (NEKA, 'Нетопырь-карлик'),
                (NEKY, 'Нетопырь Куля'),
                (NN, 'Нетопырь Натузиус'),
                (SK, 'Северный кожанок'),
                (DK, 'Двухцветный кожан'),
                (PK, 'Поздний кожан'),
                (NB, 'Ночница Брандта')
                ]
    batspecies = models.CharField(max_length=25, choices=BATSPECIES, default=DK)
    # Дата создания модели
    date_added = models.DateTimeField(auto_now_add=True)
    # Фото
    foto = models.ImageField(upload_to='Chiroptera/images/', default='Chiroptera/images/None/no-img.jpg')

    def __str__(self):
        return self.number



class LinkBatEat(models.Model):
    """Данные о кормлении и весе мыщи"""
    id = models.AutoField(primary_key=True)
    bat = models.ForeignKey(Bat, on_delete=models.CASCADE)
    # Вес до кормления
    before_feeding = models.FloatField(default=10.5)
    # Вес после кормления"""
    after_feeding = models.FloatField(default=10.5)
    # Еда летучей мыши
    A = "Мучник"
    B = 'Сверчки'
    C = 'Тараканы'
    MENU = [(A, "Мучник"),
            (B, 'Сверчки'),
            (C, 'Тараканы')
            ]
    menu = models.CharField(max_length=20, choices=MENU, default=A)
    value = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    ULTRAVIOLET = [('Y', 'Да'),
                   ('N', 'Нет')
                    ]
    ultraviolet = models.CharField(max_length=20, choices=ULTRAVIOLET, default='N')

    def Eat_data(self):
        return self.date_added

    def __str__(self):
        return f"{self.date_added}"


class BatHealing(models.Model):
    """Коментарий к лечению если требуется"""
    id = models.AutoField(primary_key=True)
    bat_id = models.ForeignKey(Bat, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    def __str__(self):
        return self.text


class Status(models.Model):
    """Статус летучей мыши"""
    id = models.AutoField(primary_key=True)
    bat_id = models.ForeignKey(Bat, on_delete=models.CASCADE)
    NEW = 'Прибыл'
    S = 'В спячке'
    MNOM = 'Откорм'
    X = "Выпущен"
    PROB = 'В разлеточнике'
    DAN = "Больна"
    BATSTATUS = [(NEW, 'Прибыла'),
                 (S, 'В спячке'),
                 (MNOM, 'Откорм'),
                 (X, "Выпущенна"),
                 (PROB, 'В разлеточнике'),
                 (DAN, "Больна")
                 ]
    batstatus = models.CharField(max_length=20, choices=BATSTATUS, default=NEW)
    date_added = models.DateTimeField(auto_now_add=True)

    def Status_data(self):
        return self.date_added


class LincStatusBat(models.Model):
    """Основная таблица связей """
    id = models.AutoField(primary_key=True)
    bat_id = models.ForeignKey(Bat, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    status_data = Status.date_added
    eat_data = LinkBatEat.date_added


