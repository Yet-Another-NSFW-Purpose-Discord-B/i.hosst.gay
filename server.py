import pathlib
import secrets
import aiohttp
import aiofiles
from quart import Quart, jsonify, send_from_directory, url_for, request, render_template
import random
import os

app = Quart(__name__)




@app.route("/")
async def home():
    return f"""
    {request.method}
    {request.url_rule}
    
    """

@app.route('/<filename>')
async def sendfile(filename=None):
    dir = "/root/yanpdb/nsfw_cdn/"
    p = pathlib.Path(dir)

    for f in p.rglob(filename):
        print(str(f.parent))
    
    return await send_from_directory(str(f.parent),filename)

app.run(debug=True, port=2031)