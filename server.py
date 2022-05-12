import pathlib
import secrets
import aiohttp
import aiofiles
from quart import Quart, jsonify, send_from_directory, url_for, request, render_template
import random
import os
import quart.flask_patch    
import logging

app = Quart(__name__)



@app.route("/")
async def home():
    return f"""
    {request.method}
    {request.url_rule}
    
    """


@app.route('/<filename>')
async def sendfile(filename=None):
    dir = "/mnt/volume_nyc1_02/images/"
    p = pathlib.Path(dir)
    for f in p.rglob(filename):
        pass
    
    print(filename)
    print(str(f.parent))

    return await send_from_directory(str(f.parent),filename)    

@app.route('/check', methods=['POST'])
async def uptime_check():
    return "Checked!"

if __name__ == "__main__":
    app.run(debug=True, port=2031)