import random

from celery import chain, chord
from addTask import add, addWithChain, request, callback

tasks = []
urls = [
    'http://114.202.130.191:9093/'
    , 'https://www.youtube.com'
    , 'https://superuser.com/questions/683021/how-to-get-the-command-that-invoked-a-task-with-tasklist'
    , 'https://www.ygosu.com'
    , 'https://www.naver.com/'
    , 'https://www.google.com/'
    , 'https://github.com/'
]

for url in urls:
    print( url )

    # x = int(random.randint(1, 10))
    # y = int(random.randint(1, 10))
    # args = ( x, y )
    
    # print( args )
    
    # Normal
    # task = add.apply_async( args ) # = add.delay( x, y )
    # tasks.append( task )

    # Chainning
    # task = addWithChain.subtask( args ) # = addWithChain.s( x, y )
    # tasks.append( task )
    
    # Chord
    # task = add.s( x, y ) # = addWithChain.subtask( args )
    # tasks.append( task )
    
    # Request
    
    # import requests
    # from pprint import pprint
    
    # response = requests.get(url)
    # pprint( ( url, len(response.text) ) )
    
    task = request.s( url )
    # task = request.delay( url )
    tasks.append( task )
    
# result = chain( tasks )()
# result = tasks
# print( result )
'''
do_chain_tasks = chain(add.s(1, 1), add.s(10), add.s(100))
do_chain_tasks()
'''

result = chord( tasks )
result( callback.s( ) ) # = callback.subtask( )
