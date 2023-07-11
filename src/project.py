[tool.poetry]
name = "youtube-analytics-project"
version = "0.1.0"
description = ""
authors = ["Alexandr Abramov <alexandr.abramovvv@yandex.ru>"]
readme = "README.md"
packages = [{include = "youtube_analytics_project"}]

[tool.poetry.dependencies]
python = "^3.11"


[tool.poetry.group.dev.dependencies]
google-api-python-client = "^2.80.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
