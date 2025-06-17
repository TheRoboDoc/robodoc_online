from flask import render_template, abort
from nav import build_nav
from render import render_markdown

import os

CONTENT_DIR = "content"

def register_routes(app):
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_page(path):
        target_path = os.path.join(CONTENT_DIR, path, "content.md")

        if not os.path.isfile(target_path):
            abort(404)

        content_html = render_markdown(target_path)

        nav = build_nav(CONTENT_DIR, "/" + path.strip("/"))

        return render_template("base.html", title=path or "Home", content=content_html, nav=nav)