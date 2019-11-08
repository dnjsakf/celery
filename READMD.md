
# 1. install - Redis on windows
https://github.com/microsoftarchive/redis/releases

# 2. run redis-server
$ redis-server redis.windows.conf --port=3001

# 3. run celery 
$ celery worker --app tasks --loglevel=info
or
$ celery -A tasks worker --loglevel=info