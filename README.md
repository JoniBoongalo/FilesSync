### 1.0 Цель проекта
Создать сихронизатор. Он сихронизирует общие данные в двух разных местах, путем переодической проверки измененных данных. 
Совместимость : Linux, Windows, android

### 2.0 Описание системы
Система состоит из следующих основных функциональных блоков:
1. *перетаскивание файлов*
2. ==проверка==
3. логгирование ( история действий программы)
4. **конфиг ( в нем хранятся paths )**
5. интерфейс взаимодействия


#### 2.1 Перетаскивание файлов
- умеет перетаскивать папки, файлы
- умеет делать грубое перетаскивание (изменяет уже существующие данные)

#### 2.2 Проверка
Этот модуль умеет делать:
- проверка пути а и б ( проверки есть ли доступ к ним)
- проверка файлов ( изменились ли файлы в точке б в сравнении с точкой а)
- 


#### 2.4 конфиг
В конфиге хранятся:
 - Определия машрутов
 - частота сихронизации
- перемменые интерфейса
