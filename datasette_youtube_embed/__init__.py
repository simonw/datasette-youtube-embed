from datasette import hookimpl
from urllib.parse import urlparse, parse_qsl
import markupsafe
import textwrap


@hookimpl
def render_cell(value):
    # Render https://www.youtube.com/watch?v=xyz as embed iframe
    if not isinstance(value, str):
        return
    stripped = value.strip()
    if "\n" in stripped or "youtube.com" not in stripped:
        # TODO: handle youtu.be short links
        return
    bits = urlparse(stripped)
    if (bits.hostname, bits.path) != ("www.youtube.com", "/watch"):
        return

    qs = dict(parse_qsl(bits.query))
    if "v" not in qs:
        return

    video_id = qs["v"]

    # We also care about start and end
    # TODO: handle t= as well (which can be 1m31s format)
    extra_bits = []
    try:
        start = int(qs.get("start"))
        extra_bits.append(f"start={start}")
    except (TypeError, ValueError):
        start = None
    try:
        end = int(qs.get("end"))
        extra_bits.append(f"end={end}")
    except (TypeError, ValueError):
        end = None

    extras = ""
    if extra_bits:
        extras = "&".join(extra_bits)

    return markupsafe.Markup(
        f'<lite-youtube videoid="{video_id}" params="{extras}" style="min-width: 200px"></lite-youtube>'
    )


@hookimpl
def extra_css_urls(columns):
    if columns:
        return ["/-/static-plugins/datasette_youtube_embed/lite-yt-embed.css"]


@hookimpl
def extra_js_urls(columns):
    if columns:
        return ["/-/static-plugins/datasette_youtube_embed/lite-yt-embed.js"]
