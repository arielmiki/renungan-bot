from model import Devotion

DEFAULT_TEMPLATE = """
*{title}*
_{author}_

[{passage}]({passage_url})
"""

class DefaultView:
    def get_markdown(self, devotion: Devotion):
        params = {
            "title": devotion.title,
            "author": devotion.author,
            "passage": devotion.passage,
            "passage_url": devotion.pasage_url,
            "content": devotion.content_md,
            "source": devotion.source
        }

        return DEFAULT_TEMPLATE.format(**params)