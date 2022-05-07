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

@app.route("/search/<filename>")
async def search(filename):
    dir = "/root/yanpdb/nsfw_cdn/"
    p = pathlib.Path(dir)
        
    for f in p.rglob(filename):
        print(str(f.parent))

    if f.parent == pathlib.Path("/root/yanpdb/nsfw_cdn/images/hentai"):
        return jsonify(url="https://thino.pics/api/v1/hentai", image=f"https://i.thino.pics/{filename}")

    if f.parent == pathlib.Path("/root/yanpdb/nsfw_cdn/images/helltakerpics"):
        return jsonify(url="https://thino.pics/api/v1/helltaker", image=f"https://i.thino.pics/{filename}")




@app.route('/<filename>')
async def sendfile(filename=None):
    dir = "/root/yanpdb/nsfw_cdn/"
    p = pathlib.Path(dir)

    for f in p.rglob(filename):
        print(str(f.parent))
    
    return await send_from_directory(str(f.parent),filename)

app.run(debug=True, port=2031)