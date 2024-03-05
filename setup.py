import setuptools

with open("README.md", "r", encoding= 'utf-8') as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "text_summarizer"
USER_NAME = "zacharias1219"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "rickoshade1891@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)