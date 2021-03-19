# docker_tpos
Сервис-1. База данных (какая именно - не имеет значения). Сервис запускается, ожидает входящих соединений на своем порту. можно использовать готовый контейнер из https://hub.docker.com/.
Сервис-2. Контейнер со скриптом для наполнения базы. Сервис запускается, подключается по порту к базе данных (можно с помощью нативного клиента к базе) и заполняет базу набором данных. Набор данных представлен CSV-файлом из 5 строк. В каждой строке 2 поля: текст и число (данные могут быть любые). Сервис-2 стартует после старта сервиса-1 и завершается (убивается контейнер) после выполнения.
Сервис-3. Контейнер с демоном отдающим из базы эти данные по http-запросу. Демон умеет принимать http запрос, соединяется с контейнером базы через порт базы, делает запрос, получает ответ, отдает данные в http ответе. Для реализации REST API по умолчанию можно использовать flask. В README или в комментариях в Dockerfile нужно указать, по какому порту должен подключиться пользователь чтоб получить данные.