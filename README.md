# LearnAnything Clone (Django)

Учебный проект на Django — интерактивный справочник и карта знаний, вдохновленный [LearnAnything.xyz](https://learnanything.xyz/). Проект использует динамические маршруты и шаблоны, позволяющие управлять статьями и темами через базу данных без постоянного переписывания кода.

---

## 📋 Требования

* **Python:** 3.10+
* **Django:** 4.2+
* **Браузер:** Chrome / Edge / Firefox (подходит для работы на Chromebook)

---

## 🚀 Быстрый запуск

### Вариант 1: Запуск через GitHub Codespaces (Chromebook / Облако)

Этот способ подходит для работы прямо из браузера без установки Python на устройство.

1. **Создайте или откройте Codespace:**
   * Откройте репозиторий на GitHub.
   * Нажмите кнопку **Code** $\rightarrow$ вкладка **Codespaces** $\rightarrow$ **Create codespace on main**.

2. **Установите зависимости:**
   В терминале Codespaces выполните:
   ```bash
   pip install django
   ```

3. **Примените миграции:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Создайте учетную запись администратора:**
   ```bash
   python manage.py createsuperuser
   ```
   *(Заполните логин и пароль. Символы пароля при вводе скрыты).*

5. **Запустите сервер разработки:**
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

6. **Перейдите на сайт:**
   * Нажмите на всплывающее уведомление **Open in Browser** или перейдите по адресу вида:  
     `https://<ваш-codespace>-8000.app.github.dev/`
   * Панель управления доступна по адресу:  
     `https://<ваш-codespace>-8000.app.github.dev/admin/`

---

### Вариант 2: Локальный запуск на Windows

1. **Клонируйте репозиторий или скачайте код:**
   ```cmd
   git clone <URL_РЕПОЗИТОРИЯ>
   cd site
   ```

2. **Создайте и активируйте виртуальное окружение:**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Установите Django:**
   ```cmd
   pip install django
   ```

4. **Примените миграции:**
   ```cmd
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Создайте суперпользователя:**
   ```cmd
   python manage.py createsuperuser
   ```

6. **Запустите сервер:**
   ```cmd
   python manage.py runserver
   ```

7. **Откройте сайт в браузере:**
   * Главная страница: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   * Панель администратора: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🛠️ Структура проекта

```text
.
├── core/                # Главный модуль настроек Django (settings.py, urls.py)
├── main/                # Основное приложение (models.py, views.py, urls.py)
├── templates/           # HTML-шаблоны сайта
│   ├── base.html        # Базовый каркас
│   └── topic_detail.html# Универсальный шаблон страницы темы
├── manage.py            # Скрипт управления Django
└── README.md            # Документация проекта
```

---

## ❓ Частые ошибки и их решение

### 1. `ModuleNotFoundError: No module named 'django'`
Выполните команду повторной установки пакета в терминале:
```bash
pip install django
```

### 2. `CSRF verification failed (403)` при входе в админку в Codespaces
Убедитесь, что в файле `core/settings.py` указаны доверенные источники:
```python
CSRF_TRUSTED_ORIGINS = [
    'https://*.app.github.dev',
    'https://*.github.dev',
    'https://localhost:8000',
    'http://127.0.0.1:8000',
]
ALLOWED_HOSTS = ['*']
```

---

## 📝 Добавление новых страниц

Все новые страницы создаются через Панель администратора без редактирования Python-кода:

1. Перейдите в `/admin/`.
2. Выберите раздел **Topics** $\rightarrow$ **Add Topic**.
3. Заполните поле **Title** (название) и **Slug** (уникальный фрагмент URL, например: `python-basics`).
4. Сохраните запись. Страница станет доступна по адресу `/topic/python-basics/`.