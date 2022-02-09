# RT_MIC_TASK
## Используемые библиотеки 


```
pip install pytest
```
```
pip install selenium
```
```
pip install pytest-html
```
Установите все используемые библиотеки так:

```
pip install -r requirements.txt
```
# Команды для запуска через pytest основных тестов .mark
---
Запуск будет осуществляется через фреймворк pytest, для запуска обеих тестов используйте:
```
pytest -v -s --tb=line --language=en -m all_test
```
Для запуска первого теста используйте:
```
pytest -v -s --tb=line --language=en -m search_in_yandex
```
Для запуска второго теста используйте:
```
pytest -v -s --tb=line --language=en -m yandex_images
```

## Для получения простого отчёта используйте
---
Отчёт будет в файле "report.html"
```
pytest --html=report.html --self-contained-html
```


## Информация о прошедших тестах
---
Логи находятся в папке seleniumlogs
