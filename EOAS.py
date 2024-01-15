import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QTextEdit, QGroupBox, QStackedWidget, QMessageBox
import mysql.connector          

class OnboardingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        # Инициализация подключения к базе данных
        self.db_connection = mysql.connector.connect(
            host='192.168.1.53',
            port = 3306, 
            user='person',
            password='12131415wwwqwe',
            database='onboarding_db'  
        )
        self.db_cursor = self.db_connection.cursor()

    def init_ui(self):
        # Создаем виджеты
        label = QLabel('Добро пожаловать в программу онбординга и адаптации сотрудников!')
        company_button = QPushButton('О компании')
        guide_button = QPushButton('Руководства и инструкции')
        training_button = QPushButton('Обучающие материалы')
        feedback_button = QPushButton('Форма обратной связи')

        # Настраиваем стиль
        self.setStyleSheet(
            """
            QWidget {
        background-color: #2c3e50;  /* Темно-синий фон */
        color: #ecf0f1;  /* Светлый текст */
        font-family: Arial, sans-serif;
        }
        QPushButton {
            margin: 5px;
            padding: 10px;
            background-color: #3498db;  /* Цвет кнопок - синий */
            color: white;
            border: none;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #2980b9;  /* Цвет кнопок при наведении - темно-синий */
        }
        
        QLabel {
            font-size: 16px;    
            margin-bottom: 10px;
        }
        QGroupBox {
            margin-top: 10px;
            border: 2px solid #3498db;  /* Граница группы - синий */
            border-radius: 5px;
            padding: 5px;
        }
        QLineEdit, QTextEdit {
            padding: 5px;
            margin-bottom: 10px;
            border: 1px solid #95a5a6;
            border-radius: 5px;
            background-color: #ecf0f1;
            color: #2c3e50;
        }
        QPushButton#submit_button {
            background-color: #2ecc71;  /* Цвет кнопки отправить - зеленый */
        }
        QPushButton#submit_button:hover {
            background-color: #27ae60;  /* Цвет кнопки отправить при наведении - темно-зеленый */
        }
            """
        )

        # Настраиваем макет
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(company_button)
        layout.addWidget(guide_button)
        layout.addWidget(training_button)
        layout.addWidget(feedback_button)

        # Создаем виджет для отображения контента
        self.stacked_widget = QStackedWidget()

        # Добавляем виджеты для каждой категории
        self.create_company_info_widget()
        self.create_guides_widget()
        self.create_training_materials_widget()
        self.create_feedback_form_widget()

        # Добавляем виджеты к QStackedWidget
        self.stacked_widget.addWidget(self.company_info_widget)
        self.stacked_widget.addWidget(self.guides_widget)
        self.stacked_widget.addWidget(self.training_materials_widget)
        self.stacked_widget.addWidget(self.feedback_form_widget)

        # Назначаем обработчики событий кнопкам
        company_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        guide_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        training_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        feedback_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))

        # Настраиваем главное окно
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

        self.setWindowTitle('Сервис онбординга и адаптации сотрудников')
        self.show()

    def create_company_info_widget(self):
        self.company_info_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Информация о компании будет здесь.'))
        self.company_info_widget.setLayout(layout)

    def create_guides_widget(self):
        self.guides_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Руководства и инструкции будут здесь.'))
        self.guides_widget.setLayout(layout)

    def create_training_materials_widget(self):
        self.training_materials_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Обучающие материалы будут здесь.'))
        self.training_materials_widget.setLayout(layout)

    def create_feedback_form_widget(self):
        self.feedback_form_widget = QWidget()
        layout = QFormLayout()
        self.name_input = QLineEdit()
        self.position_input = QLineEdit()  # Добавлено поле для ввода должности
        self.phone_input = QLineEdit()  # Добавлено поле для ввода телефона
        self.feedback_input = QTextEdit()
        group_box = QGroupBox('Выберите уровень удовлетворенности:')
        group_box_layout = QVBoxLayout()
        group_box_layout.addWidget(QPushButton('Низкий', clicked=self.set_low_satisfaction))
        group_box_layout.addWidget(QPushButton('Средний', clicked=self.set_medium_satisfaction))
        group_box_layout.addWidget(QPushButton('Высокий', clicked=self.set_high_satisfaction))
        group_box.setLayout(group_box_layout)
        submit_button = QPushButton('Отправить', objectName='submit_button', clicked=self.submit_feedback)
        layout.addRow('Имя:', self.name_input)
        layout.addRow('Должность:', self.position_input)
        layout.addRow('Телефон:', self.phone_input)
        layout.addRow('Отзыв:', self.feedback_input)
        layout.addWidget(group_box)
        layout.addWidget(submit_button)
        self.feedback_form_widget.setLayout(layout) 


    def set_low_satisfaction(self):
        self.satisfaction_level = 'Низкий'

    def set_medium_satisfaction(self):
        self.satisfaction_level = 'Средний'

    def set_high_satisfaction(self):
        self.satisfaction_level = 'Высокий'

    def submit_feedback(self):
        name = self.name_input.text().strip()
        position = self.position_input.text().strip()
        phone = self.phone_input.text().strip()
        feedback = self.feedback_input.toPlainText().strip()

        if not (name and position and phone and feedback):
            QMessageBox.warning(self, 'Ошибка', 'Заполните все поля формы обратной связи')
            return

        if not hasattr(self, 'satisfaction_level'):
            QMessageBox.warning(self, 'Ошибка', 'Выберите уровень удовлетворенности')
            return

        QMessageBox.information(self, 'Отправлено', 'Ваш отзыв успешно отправлен!')
        print(f'Имя: {name}\nДолжность: {position}\nТелефон: {phone}\nОтзыв: {feedback}\nУровень удовлетворенности: {self.satisfaction_level}')

        # Вставка данных в базу данных
        insert_query = (
            "INSERT INTO feedback (name, position, phone, feedback, satisfaction_level) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        data = (name, position, phone, feedback, self.satisfaction_level)
        self.db_cursor.execute(insert_query, data)
        self.db_connection.commit()

    def create_training_materials_widget(self):
        self.training_materials_widget = QWidget()
        layout = QVBoxLayout()

        text_materials = QTextEdit()
        text_materials.setPlainText(
            """
    Раздел 1: Основы Дизайна

    1.1 Введение в Графический Дизайн

    - Понимание истории графического дизайна и его влияния на веб-пространство.
    - Роль графического дизайнера в создании эффективных визуальных решений.
    - Принципы композиции:
    - Изучение основных принципов композиции, включая баланс, контраст, иерархию и повторение.
    - Как эффективно применять эти принципы в дизайне веб-страниц.

    1.2 Работа с Adobe Creative Suite

    - Глубокое погружение в Photoshop для редактирования изображений и создания визуальных элементов для веба.
    - Применение фильтров, настройка цветовой гаммы и улучшение качества графики.
    - Illustrator:
    - Создание векторной графики и логотипов с использованием Illustrator.
    - Изучение инструментов рисования, работы с шейдерами и текстовыми элементами.
    - XD (Experience Design):
    - Проектирование пользовательских интерфейсов (UI) и прототипирование с помощью Adobe XD.
    - Интеграция дизайна и просмотр проектов в рамках единого инструментария.

    Раздел 2: Дизайн веб-Интерфейсов

    2.1 Принципы UX/UI Дизайна

    - Обзор ключевых понятий, связанных с пользовательским опытом (UX) и интерфейсным дизайном (UI).
    - Как эти принципы влияют на восприятие и взаимодействие пользователей с веб-проектами.
    - Принципы Доступности:
    - Знакомство с принципами создания доступных и инклюзивных интерфейсов.
    - Практические советы по улучшению UX для всех пользователей.

    2.2 Работа с Инструментами Прототипирования

    - Использование инструментов для создания интерактивных прототипов (например, Adobe XD).
    - Эффективное представление дизайн-концепций заказчикам и команде.
    - Тестирование и Оптимизация:
    - Как проводить тестирование прототипов с участием заказчиков и конечных пользователей.
    - Применение обратной связи для оптимизации интерфейсов и повышения удовлетворенности пользователей.

    Раздел 3: Конструкторы Сайтов

    3.1 Знакомство с WordPress

    - Основы установки и настройки WordPress.
    - Работа с плагинами и темами для кастомизации внешнего вида сайта.
    - Создание Содержания:
    - Процесс создания и редактирования контента в WordPress.
    - Оптимизация изображений и использование медиа-файлов.
    - Оптимизация для Производительности:
    - Работа с кэшированием и оптимизация загрузки страниц.
    - Применение базовых SEO-приемов для улучшения видимости сайта.

    3.2 Работа с Wix и Squarespace

    - Проектирование на Конструкторах:
    - Создание дизайна сайтов с использованием инструментов Wix и Squarespace.
    - Как эффективно использовать встроенные шаблоны и элементы.
    - Интеграции и Дополнительные Функции:
    - Интеграция сторонних сервисов и приложений.
    - Работа с дополнительными функциями, такими как онлайн-магазины или бронирование.
    - Оптимизация для Мобильных Устройств:
    - Гарантированное корректное отображение на мобильных устройствах.
    - Тестирование и оптимизация мобильного интерфейса.

    Раздел 4: Процесс Работы над Проектами

    4.1 Получение и Понимание Задач

    - Системы Управления Задачами:
    - Эффективное использование систем управления задачами, таких как Jira или Trello.
    - Как оформлять и принимать задачи для дизайн-процесса.
    - Как проводить анализ брифов заказчика.
    - Определение основных требований и целей проекта.

    4.2 Коллективное Творчество

    - Организация брейнштормов для создания креативных концепций.
    - Как эффективно высказывать и поддерживать свои идеи.
    - Использование облачных платформ для совместной работы, таких как Google Workspace или Microsoft Teams.
    - Обмен идеями и обратной связью в режиме реального времени.

    Раздел 5: Обратная Связь и Улучшение Процессов

    5.1 Обзор и Оценка Проектов

    - Как определять критерии оценки проектов.
    - Регулярные обзоры для выявления успешных моментов и областей для улучшения.
    - Как использовать обратную связь для коррекции и улучшения дизайна.
    - Совместное обсуждение результатов и предложения по оптимизации.

    5.2 Персональное Развитие

    - Способы оценки собственного профессионального роста.
    - Взаимодействие с руководством для определения новых целей.
    - Регулярное участие в вебинарах, мастер-классах и обучающих курсах.
    - Как применять новые навыки в повседневной практике.

    Раздел 6: Взаимодействие с Заказчиками

    6.1 Профессиональная Коммуникация

    - Развитие навыков профессиональной коммуникации с заказчиками и коллегами.
    - Использование четких терминов и языка для понимания неспециалистов.
    - Как адаптировать технические термины для широкой аудитории.
    - Подготовка и предоставление информации о проекте в доступной форме.

    6.2 Предоставление Концепций

    - Подготовка презентаций и концепций для заказчиков.
    - Интеграция обратной связи заказчиков в дизайн-процесс для улучшения конечного продукта.

            """
        )
        text_materials.setReadOnly(True)

        layout.addWidget(QLabel('Обучающие материалы:'))
        layout.addWidget(text_materials)
        self.training_materials_widget.setLayout(layout)
        

    def create_company_info_widget(self):
        self.company_info_widget = QWidget()
        layout = QVBoxLayout()

        text_company_info = QTextEdit()
        text_company_info.setPlainText(
            """
WebCraft Innovations — ведущая компания в сфере дизайна и конструкторства веб-сайтов. Основанная на страсти к инновациям и креативному подходу к каждому проекту, компания ставит своей целью предоставление клиентам выдающихся веб-решений.

WebCraft Innovations специализируется в создании интуитивно понятных и стильных веб-интерфейсов. Команда дизайнеров стремится к тому, чтобы каждый проект отражал уникальный стиль и ценности клиента.

Компания предоставляет полный цикл услуг по разработке и конструкторству веб-сайтов. От простых лендингов до масштабных корпоративных порталов, WebCraft Innovations обеспечивает высококачественные технические решения.

Специалисты WebCraft Innovations также уделяют внимание оптимизации веб-сайтов для максимальной видимости в поисковых системах. Это включает в себя как техническую SEO, так и контент-стратегии для привлечения аудитории.

Компания активно следит за последними тенденциями в веб-дизайне и внедряет инновационные технологии для создания современных и уникальных проектов.

Принципы Работы:

Каждый проект рассматривается как возможность внедрить новые идеи и инновационные подходы.

WebCraft Innovations стремится к полному удовлетворению потребностей клиентов, предлагая персонализированные решения.

Высокий уровень квалификации сотрудников и строгое соблюдение стандартов качества являются основой деятельности компании.

Команда:
WebCraft Innovations объединяет команда талантливых дизайнеров, разработчиков, маркетологов и специалистов по SEO, обеспечивая всеобъемлющий подход к проектам.

Процесс Работы:

В начале проекта проводится тщательная консультация с клиентом для определения целей и требований.

Команда WebCraft Innovations приступает к созданию уникального дизайна и разработке функциональности в соответствии с концепцией.

Все веб-проекты проходят тщательное тестирование, и проводится оптимизация для максимальной производительности.

После успешного завершения проекта компания обеспечивает полный цикл поддержки и обслуживания.

Клиенты и Проекты:
WebCraft Innovations с гордостью предоставляет портфолио успешных проектов для различных клиентов — от стартапов до крупных компаний.

WebCraft Innovations — это не просто компания, а творческое пространство, где каждый проект становится уникальным и воплощает в себе лучшие традиции веб-дизайна и разработки.
            """
        )
        text_company_info.setReadOnly(True)

        layout.addWidget(QLabel('Информация о компании:'))
        layout.addWidget(text_company_info)
        self.company_info_widget.setLayout(layout)

    def create_guides_widget(self):
        self.guides_widget = QWidget()
        layout = QVBoxLayout()

        text_guides = QTextEdit()
        text_guides.setPlainText(
            """
            
Добро пожаловать в WebCraft Innovations! Мы ценим ваш вклад в наше креативное сообщество. Чтобы облегчить вам старт и интеграцию в нашу компанию, мы предоставляем сервис онбординга и адаптации. Этот гид поможет вам успешно использовать наши ресурсы и получить максимальную выгоду от вашего опыта работы с нами.

1. Регистрация и Вход в Систему
1.1 Регистрация в Системе:

После получения приглашения, пройдите процесс регистрации в системе онбординга.

1.2 Вход в Систему:

Используйте вашу корпоративную почту и временный пароль для входа в систему.

2. Знакомство с Компанией
2.1 Профиль Компании:

Посетите раздел "О Компании", чтобы узнать о целях, миссии и ключевых проектах WebCraft Innovations.

2.2 Культура и Значения:

Ознакомьтесь с культурой компании и нашими ценностями, чтобы лучше понимать коллектив и вкладывать себя в общую атмосферу.

3. Обучающие Материалы
3.1 Курсы и Материалы:

Посетите раздел "Обучение" для доступа к обучающим материалам по вашей области работы.

3.2 Профессиональное Развитие:

Изучите возможности профессионального развития и планы обучения, чтобы постоянно совершенствоваться.

4. Онбординг и Адаптация
4.1 Онбординг:

Следуйте шагам в разделе "Онбординг", чтобы успешно проходить этапы адаптации.

4.2 Менторство:

Определите своего ментора и используйте возможности консультации для лучшего понимания процессов и задач.

5. Отправка Обратной Связи
5.1 Форма Обратной Связи:

Используйте раздел "Обратная Связь" для выражения своих мыслей, предложений и вопросов.

5.2 Регулярные Сессии:

Участвуйте в регулярных сессиях обратной связи для повышения эффективности коммуникации и совершенствования процессов.

6. Дополнительные Ресурсы
6.1 Библиотека Ресурсов:

Воспользуйтесь библиотекой полезных ресурсов и инструкций для решения технических вопросов.

6.2 Форум и Обсуждения:

Присоединитесь к форумам и обсуждениям, чтобы делиться опытом и получать помощь от коллег.
Спасибо за выбор WebCraft Innovations! Мы уверены, что ваш вклад в наш коллектив будет ценным, и этот сервис поможет вам полноценно интегрироваться в нашу креативную обстановку. Если у вас есть вопросы, не стесняйтесь обращаться к HR-специалисту или руководству компании. Удачи в вашей новой роли!
            """
        )
        text_guides.setReadOnly(True)

        layout.addWidget(QLabel('Руководства и инструкции:'))
        layout.addWidget(text_guides)
        self.guides_widget.setLayout(layout)
        

    def __del__(self):
        # Закрытие соединения с базой данных при закрытии приложения
        if self.db_connection.is_connected():
            self.db_cursor.close()
            self.db_connection.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OnboardingApp()
    sys.exit(app.exec())
