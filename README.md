# krausen-cam

streaming app for fermentation chamber cameras

## Getting Started

- Start App

  - The app should start simply using `docker-compose up`
  - To run the app in the background `docker-compose up -d`
  - To rebuild the app `docker-compose --build`
  - If you have any issue around entrypoint.sh not being executable, use `chmod +x server/src/entrypoint.sh from root`

- Connect to python server application console

  - ensure that the containers are running using the above start commands

  - enter the following in your terminal at the root of the application

  ```console
  docker-compose exec server-service flask shell
  ```

- Connect to the postgres database

  - ensure that the containers are running using the above start commands

  - get a fresh database with the imported sqlAlchemy models by running

  ```console
  docker-compose exec server-service python manage.py recreate_db
  ```

  - enter the following in your terminal at the root of the application to connect to the postgres container (db services)

  ```console
  docker-compose exec db psql -U postgres
  ```

  - once in the console to connect to dev database enter the following

  ```console
  \c dev
  ```

  - If you are just booting the app up and have run all the above you should at least see the users table, check by listing the tables

  ```console
  \dt
  ```

  you should see

  ```console
   List of relations
   Schema | Name  | Type  |  Owner
   --------+-------+-------+----------
   public | users | table | postgres
   (1 row)
  ```
