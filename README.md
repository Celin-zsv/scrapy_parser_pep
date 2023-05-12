[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=30&pause=1000&color=F71329&multiline=true&width=435&lines=+scrapy_parser_pep)](https://git.io/typing-svg)  
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=20&pause=1000&color=1D39F7&multiline=true&width=435&lines=+scrapy_parser_pep)](https://git.io/typing-svg)  
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=15&duration=2000&pause=1000&color=1FBB30F6&multiline=true&width=435&lines=+scrapy_parser_pep)](https://git.io/typing-svg)    
[![Typing SVG](https://img.shields.io/badge/scrapy_parser_pep-sprint--19%20ver.2-red)](https://git.io/typing-svg)

### Проект: асинхронный парсер PEP. Спринт-19, ver.2, Зеленковский Сергей  
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTujwu6HtzvrpKw44xso5zi1iYZvFeDtWzr4_FO5En6DQ&s)
#### Содержание
1. Описание проекта
2. Установка
3. Запуск
***
### 1. *Описание проекта*


Parameter  | Value
-------------|:-------------
Наименование проекта  | scrapy_parser_pep
Назначение проекта | создать парсер документов PEP на базе фреймворка Scrapy (PEP - Python Enhancement Proposals)
Tech Stack. Client. OS | Windows, Linux, MacOS
GitHub | https://github.com/Celin-zsv/scrapy_parser_pep
Author | Sergei Zelenkovskii, svzelenkovskii@gmail.com  

### 2. *Установка*




2.1. клонировать репозиторий
```
cd dev
git clone  https://github.com/Celin-zsv/scrapy_parser_pep
```
2.2. создать и активировать виртуальное окружение:
```
  # Windows
python -m venv env
. env/Scripts/activate
  # Unix / MacOS
python3 -m venv env
source venv/bin/activate
```
2.3. обновить менеджер пакетов pip, установить зависимости requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. *Запуск*

3.1. ввести команду: старт проекта
```
scrapy startproject pep_parse .
```
3.2. ввести команду: создать паука
```
scrapy genspider pep peps.python.org
```
3.3. ввести команду: запустить паука
```
scrapy crawl pep
```
3.4. вывод результата <запуска паука>:
* файл_1:

Parameter  | Value
-------------|:-------------
Директория  | /results
Наименование файла   | pep_ДатаВремя.csv, пример: pep_2023-05-11T18-04-02.csv
Формат файла   | csv
Состав полей   | number,name,status 
Описание полей  | 1)number - номер PEP; 2) name - наименование PEP; 3)status - статус PEP;
Структура файла  | Первая запись - шапка; Каждая запись - один документ PEP;

* файл_2:

Parameter  | Value
-------------|:-------------
Директория  | /results
Наименование файла   | status_summary_ДатаВремя.csv, пример: status_summary_2023-05-11_21-04-31.csv
Формат файла   | csv
Состав полей   | Status,Quantity
Описание полей  | 1)Status - уникальный статус документов PEP; 2) Quantity - количество документов PEP, которые имеют данный статус;
Структура файла  | Первая запись - шапка; Последняя запись - ИТОГО количество документов PEP; Каждая запись - уникальный статус документов PEP;


@zsv
