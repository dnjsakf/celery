import time
import random
import requests
import codecs
import asyncio

from celery import Celery
from urllib.parse import urlparse

# redis://:password@hostname:port/db_number
BROKER_URL = 'redis://localhost:3001'
CELERY_RESULT_BACKEND = 'redis://localhost:3001'

app = Celery('addTask', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)

@app.task 
def add(x, y):
    sum = x + y
    
    print( f'{ x } + { y } = { sum }' )

    # time.sleep( random.randint(1, 2) )
    
    return sum
    
    
@app.task
def addWithChain(x, y, z=0):
    '''
        chainning => x에 이전에 처리된 결과값 저장
    '''
    sum = x + y + z
    print( f'{ x } + { y } + { z } = { sum }' )
    
    # time.sleep( random.randint(1, 2) )
    
    return sum
    
@app.task
def request( prevUrl, nextUrl=None ):
    
    url = prevUrl if nextUrl == None else nextUrl

    parsedUrl = urlparse( url )
    res = requests.get( url )
    
    filename = parsedUrl.netloc.replace('www.', '').replace('.com','')
    
    delay( 3, filename, res.text )
    
    return (filename, len(res.text) )
    
async def delay( num, filename, text ): 
    await asyncio.sleep( num )
    
    with codecs.open( f'./{filename}.html', 'w', encoding='utf-8' ) as writor:
        delay( 3 )
        writor.write( text )
        
    print('hi')
    
@app.task
def callback( total ):
    from pprint import pprint
    pprint( f'total = { total }' )
    return total