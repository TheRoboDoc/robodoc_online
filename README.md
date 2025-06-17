# RoboDoc Terminal Node

A retro CRT-themed personal website for **The RoboDoc**.
Built with Flask, Markdown, and terminal aesthetic rituals.

## Features

-  CRT-style UI with glowing green terminal text
-  Content served from `content/` folder using Markdown
-  Auto-generated navigation with indentation-aware hierarchy
-  Animated "loading in_" intro + typewriter effect
-  Session-aware animation (only on first visit)

##  Folder Structure

```

robodoc\_online/
├── app.py
├── nav.py, routes.py, render.py
├── content/              # Markdown content structure
├── static/
│   ├── css/style.css     # CRT styling
│   ├── js/nav.js         # Loader and typewriter logic
│   ├── img/              # Logo, favicon, etc.
│   └── fonts/            # BigBlueTerminal or other .ttf
├── templates/
│   ├── base.html
│   └── 404.html
├── requirements.txt
└── README.md

```

## Running Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Requirements

* Python 3.12+
* Flask
* Markdown

## Live Site

[https://robodoc.online](https://robodoc.online)

> May your scrollwheel never desync.
> May your packets remain pure.
