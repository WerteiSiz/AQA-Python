# AQA Python — UI-тесты для saucedemo

Краткая инструкция от студента — что это и как запустить :) 

Это небольшой набор UI-тестов на Python + Playwright для проверки авторизации
на https://www.saucedemo.com. Тесты написаны с применением паттерна Page Object
и собирают результаты в Allure.

Требования
- Python 3.10
- Playwright
- Docker (опционально, для запуска в контейнере)

Структура проекта
- `requirements.txt`: зависимости
- `README.md`: инструкция (это файл)
- `pytest.ini`: базовая конфигурация pytest
- `conftest.py`: фикстуры (например, `base_url`)
- `pages/` — Page Object(s):
	- `login_page.py` — класс `LoginPage` с методами открытия страницы и логина
- `tests/` — тесты pytest:
	- `test_login.py` — 5 тест-кейсов для разных сценариев логина
- `Dockerfile` — образ для запуска тестов в контейнере
- `allure-results/` — папка, куда пишутся результаты при запуске

Быстрая установка (локально)

1) Создать виртуальное окружение и активировать его (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Установить зависимости и браузеры Playwright:

```powershell
python -m pip install -r requirements.txt
python -m playwright install
```

Запуск тестов

Запустить весь набор и собрать результаты для Allure:

```powershell
pytest --alluredir=allure-results
```

Запустить один тест или паттерн (например, только performance_glitch_user):

```powershell
pytest -k performance_glitch_user --alluredir=allure-results
```

Генерация и просмотр отчёта Allure (локально)

Если у вас установлен `allure` (commandline):

```powershell
allure serve allure-results
```

Или сгенерировать статический отчёт и открыть его:

```powershell
allure generate allure-results -o allure-report --clean
allure open -h 0.0.0.0 -p 8080 allure-report
```

Запуск в Docker

Если хотите запустить тесты в изолированном контейнере (Docker должен быть
запущен):

```powershell
docker build -t aqa-python .
docker run --rm -v ${PWD}:/app -v ${PWD}\\allure-results:/allure-results aqa-python
```

Примечания и советы
- Тесты используют Playwright-fixture `page` от `pytest-playwright`.
- Все результаты тестов попадают в папку `allure-results` — её можно
	пробросить из контейнера на хост и затем смотреть отчет локально.
- Если что-то не запускается — пришлите вывод ошибки, помогу быстро разобраться.

Если хотите, могу:
- запустить Allure-отчёт локально и показать, или
- подсказать, как настроить CI (GitHub Actions/GitLab CI) для автозапуска.

Удачи — и да, небольшие баги в логике тестов можно быстро поправить :) 
