from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-youtube-embed",
    description="Turn YouTube URLs into embedded players in Datasette",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-youtube-embed",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-youtube-embed/issues",
        "CI": "https://github.com/simonw/datasette-youtube-embed/actions",
        "Changelog": "https://github.com/simonw/datasette-youtube-embed/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["datasette_youtube_embed"],
    package_data={"datasette_youtube_embed": ["static/*"]},
    entry_points={"datasette": ["youtube_embed = datasette_youtube_embed"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    python_requires=">=3.7",
)
