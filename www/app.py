import logging
import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


def index(request):
    print('get request.....')
    return web.Response(body=b'<h1 style="color:red">hello world!</h1>', content_type='text/html')


async def init(para_loop):
    app = web.Application(loop=para_loop)
    app.router.add_route('GET', '/', index)
    app_runner = web.AppRunner(app)
    srv = await para_loop.create_server(app_runner.app.make_handler(), '127.0.0.1', 8888)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(init(event_loop))
event_loop.run_forever()
