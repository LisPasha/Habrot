FROM adoptopenjdk/openjdk11:ubi
ARG JAR_FILE=target/*.jar
ENV BOT_NAME=test.habrot_bot
ENV BOT_TOKEN=2042894858:AAER1_1b0cE4v2CdmJm2fyQFFD8QjnBiwlM
ENV BOT_DB_USERNAME=htb_db_user
ENV BOT_DB_PASSWORD=htb_db_password
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-Dspring.datasource.password=${BOT_DB_PASSWORD}", "-Dbot.username=${BOT_NAME}", "-Dbot.token=${BOT_TOKEN}", "-Dspring.datasource.username=${BOT_DB_USERNAME}", "-jar", "/app.jar"]