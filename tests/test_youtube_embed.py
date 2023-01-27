from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "url,expected",
    (
        ("Not a URL", "Not a URL"),
        (
            "https://www.youtube.com/watch?v=xyz",
            '<lite-youtube videoid="xyz" params="" style="min-width: 200px"></lite-youtube>',
        ),
        (
            "https://www.youtube.com/watch?v=xyz&start=10",
            '<lite-youtube videoid="xyz" params="start=10" style="min-width: 200px"></lite-youtube>',
        ),
        (
            "https://www.youtube.com/watch?v=xyz&start=10&end=20",
            '<lite-youtube videoid="xyz" params="start=10&end=20" style="min-width: 200px"></lite-youtube>',
        ),
    ),
)
async def test_youtube_embed(url, expected):
    datasette = Datasette(memory=True)
    response = await datasette.client.get(
        "/_memory",
        params={
            "sql": "select :url as u",
            "url": url,
        },
    )
    assert response.status_code == 200
    # <td class="col-u"><lite-youtube videoid="xyz" params=""></lite-youtube></td>
    html = response.text.split('<td class="col-u">')[1].split("</td>")[0]
    assert html == expected
