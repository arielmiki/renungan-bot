import requests
import re
import markdownify
from model import Devotion

ODB_URL_TEMPLATE = "https://api.experience.odb.org/devotionals/v2?site_id={}&status=publish&on={}"
ODB_LANG_TO_SITE_MAP = {
    "en": 1,
    "id": 3
}
ODB_SOURCE_NAME = "Our Daily Bread"

class ODBFetcher:
    def get_devotion(self, lang, date) -> Devotion:
        url = ODB_URL_TEMPLATE.format(ODB_LANG_TO_SITE_MAP.get(lang, 1), date.strftime("%m-%d-%Y"))
        r_json =  requests.get(url).json()
        return Devotion(
            r_json[0]["title"], 
            self.__convert_content_to_markdown(r_json[0]["content"]), 
            r_json[0]["passage_reference"], 
            r_json[0]["passage_url"],
            r_json[0]["author_name"], 
            ODB_SOURCE_NAME,
            r_json[0]["insights"],
            r_json[0]["date"])

    def __convert_content_to_markdown(self, content):
        md =  markdownify.markdownify(content, heading_style="ATX", strong_em_symbol="_")
        return re.sub(r'\n\s*\n', '\n\n', md)
    

