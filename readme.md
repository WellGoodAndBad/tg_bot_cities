#### TG BOT

##### docker-compose build
##### docker-compose up


вставить в .env файл переменные:
 - MONGO_INITDB_ROOT_USERNAME
 - MONGO_INITDB_ROOT_PASSWORD
 - MONGO_INITDB_DATABASE
 - TG_TOKEN
 - TG_BOT_PORT

бот принимает команды:
 - /start_parser - запускает сбор данных
 - /city <название_города> - название города не зависит от регистра
 - если отправить боту сообщение, по отправленному тексту бот будет пытаться найти город, в случае успеха, вернет города