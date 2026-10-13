import hashlib
import html.parser
import re
import time
from typing import Dict, List, Any

class DOMParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings: List[Dict[str, str]] = []
        self.links: List[str] = []
        self._cur_tag = None

    def handle_starttag(self, tag: str, attrs: list):
        attr_map = dict(attrs)
        if tag in ("h1", "h2", "h3"):
            self._cur_tag = tag
        elif tag == "a" and "href" in attr_map:
            self.links.append(attr_map["href"])

    def handle_endtag(self, tag: str):
        if tag == self._cur_tag:
            self._cur_tag = None

    def handle_data(self, data: str):
        text = data.strip()
        if text and self._cur_tag:
            self.headings.append({"tag": self._cur_tag, "text": text})

class PageSnapshot:
    @staticmethod
    def inspect_html(html_content: str, url: str = "local") -> Dict[str, Any]:
        parser = DOMParser()
        parser.feed(html_content)
        clean = re.sub(r"<[^>]+>", " ", html_content)
        clean = re.sub(r"\s+", " ", clean).strip()
        h = hashlib.sha256(clean.encode("utf-8")).hexdigest()
        return {
            "url": url,
            "content_hash": h,
            "headings_count": len(parser.headings),
            "headings": parser.headings,
            "links_count": len(parser.links),
            "links": parser.links,
            "text_length": len(clean),
        }

    @staticmethod
    def diff_snapshots(snap_a: Dict[str, Any], snap_b: Dict[str, Any]) -> Dict[str, Any]:
        changed = snap_a["content_hash"] != snap_b["content_hash"]
        return {
            "has_changed": changed,
            "hash_before": snap_a["content_hash"],
            "hash_after": snap_b["content_hash"],
            "length_delta": snap_b["text_length"] - snap_a["text_length"],
        }
