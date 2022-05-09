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

@app.route("/search/<filename>")
async def search(filename):
    dir = "/mnt/volume_nyc1_02/images/"
    p = pathlib.Path(dir)


    for f in p.rglob(filename):
        print(str(f.parent))

    if f.parent == pathlib.Path("/mnt/volume_nyc1_02/images/hentai"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/hentai", image=f"https://i.thino.pics/{filename}", dir=f"{str(os.path.join(f.parent, filename))}", status=200, filename=filename)

    if f.parent == pathlib.Path("/mnt/volume_nyc1_02/images/helltakerpics"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/helltaker", image=f"https://i.thino.pics/{filename}", dir=f"{str(os.path.join(f.parent, filename))}", status=200, filename=filename)

    if f.parent == pathlib.Path("/mnt/volume_nyc1_02/images/neko"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/neko", image=f"https://i.thino.pics/{filename}", dir=f"{str(os.path.join(f.parent, filename))}", status=200, filename=filename)

    if f.parent == pathlib.Path("/mnt/volume_nyc1_02/images/tomboy"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/tomboy", image=f"https://i.thino.pics/{filename}", dir=f"{str(os.path.join(f.parent, filename))}", status=200, filename=filename)

    if f.parent == pathlib.Path("/mnt/volume_nyc1_02/images/femboy"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/femboy", image=f"https://i.thino.pics/{filename}", dir=f"{str(os.path.join(f.parent, filename))}", status=200, filename=filename)
    
    if f.parent == pathlib.Path("/mnt/volume_nyc1_02/images/thighs"):
        print(filename)
        print(str(f.parent))
        return jsonify(url="https://thino.pics/api/v1/thighs", image=f"https://i.thino.pics/{filename}", dir=f"{str(os.path.join(f.parent, filename))}", status=200, filename=filename)


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