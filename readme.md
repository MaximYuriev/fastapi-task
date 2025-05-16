# Запуск проекта
1) Предварительно следует подготовить базу данных с помощью [парсера](https://github.com/MaximYuriev/db_wm_2)
2) Установить все зависимости проекта:
    ```commandline
    poetry install
    ```
3) Создать .env файл по примеру из .env.example:
   ```
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=pswd
    POSTGRES_DB=db_name
    
    REDIS_HOST=localhost
    REDIS_PORT=6379
    ```
4) Запустить redis в докере:
    ```commandline
    docker compose --file docker/cache.yml up --build  
    ```
5) Запустить проект:
    ```commandline
    uvicorn --factory src.main:create_app
    ```