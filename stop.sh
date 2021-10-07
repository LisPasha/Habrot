#!/bin/bash

# Убеждаймся, что docker-compose остановлен.
docker-compose stop

# Убеждаймся,  что старое приложение не будет развернуто снова.
mvn clean