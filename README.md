# Telegram бот

Этот бот предоставляет информацию о приемной комиссии МПГУ. Ознакомиться с ним можно [здесь](https://t.me/kd_mpgu_bot)
## Доступные команды:
* start - запуск бота
* help - помощь
* priem_com - информация о приемной комиссии
* website - электронные ресурсы ВУЗа
* student - информация для бакалавриатов
* aspirant - информация для аспирантов
* magistr информация для магистров
* zachislenya - приказы о зачислении студентов

## Установка 
Проверьте установлен ли Docker
```bash
docker version
```
Если Docker отсутствует, установите его.
Клонируйте рипозиторий на свое устройство:
```bash
git clonehttps://github.com/Tenrai-chi/mpgu_bot.git
```
Перейдите в папку omg внутри проекта
```bash
cd mpgu_bot
```
Теперь вы можете создать образ. Вместо docker_bot можете указать свое собственное имя образа.
```bash
docker build . --tag docker_bot
```
Запустите контейнер на основе созданного образа.
```bash
docker run -p 8000:8000  docker_bot
```
