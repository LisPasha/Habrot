#!/bin/bash

# Подготовка нашего jar
mvn clean
mvn package

# Убеждаймся что docker-compose останолен
docker-compose stop

# Добавляем переменные окружения (с именем и токеном нашего бота)
export BOT_NAME=$1
export BOT_TOKEN=$2
export BOT_DB_USERNAME='prod_jrtb_db_user'
export BOT_DB_PASSWORD='Pap9L9VVUkNYj99GCUCC3mJkb'
# Начинаем новое развертывание
docker-compose up --build -d