### Step 1
放.env與docker-compose.yml同一層

```
docker-compose up -d --build
```

### Step 2
```
docker-compose exec app bash
python manage.py migrate
exit
```

### Step 3
網址： http://127.0.0.1:8002/home/
```
爬蟲api
[number: int , 0 <= number < 20, 0等於撈全部的新聞]
http://127.0.0.1:8002/api/news/crawler/?number={int}

新聞列表api
http://127.0.0.1:8002/api/news/

單一新聞內容
http://127.0.0.1:8002/api/news/{id}/
```
