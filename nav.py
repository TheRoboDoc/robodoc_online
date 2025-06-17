import os

def build_nav(content_dir: str, active_path: str = "") -> list[tuple[str, str, int]]:
    nav = []

    def walk(current_path: str, depth=0):
        if depth == 0:
            root_content = os.path.join(content_dir, "content.md")

            if os.path.isfile(root_content):
                nav.append(("home", "/", 0))

        for entry in sorted(os.listdir(current_path)):
            full_path = os.path.join(current_path, entry)

            rel_path = os.path.relpath(full_path, content_dir)

            url_path = "/" + rel_path.replace(os.sep, "/")

            if os.path.isdir(full_path):
                content_file = os.path.join(full_path, "content.md")

                if os.path.isfile(content_file):
                    label = entry

                    show = (
                        depth == 0 or
                        active_path == url_path or
                        active_path.startswith(url_path + "/") or
                        url_path.startswith(active_path + "/")
                    )

                    if show:
                        nav.append((label, url_path, depth))

                if active_path.startswith(url_path) or url_path.startswith(active_path):
                    walk(full_path, depth + 1)

    walk(content_dir)

    return nav
