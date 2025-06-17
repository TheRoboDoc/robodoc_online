import markdown

def render_markdown(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return markdown.markdown(f.read())