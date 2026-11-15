"""Static integrity checks for Monopolises' six public research pages.

Run with: python3 -m unittest discover -s tests -v
No third-party packages or network connection required.
"""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import unittest
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ROUTES = ("/", "/thesis/", "/methodology/", "/sources/", "/research/", "/about/")
DOMAIN = "https://monopolises.com"
GITHUB_PREFIX = "https://github.com/Sohadot/Monopolises/"


def route_file(route):
    return ROOT / (route.lstrip("/") + "index.html")


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.canonicals = []
        self.descriptions = []
        self.titles = []
        self.language = None
        self.main_count = 0
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.language = attrs.get("lang")
        if tag == "main":
            self.main_count += 1
        if tag == "title":
            self.in_title = True
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href"))
        if tag == "meta" and attrs.get("name") == "description":
            self.descriptions.append(attrs.get("content", ""))

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.titles.append(data)


class PublicReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {}
        for route in ROUTES:
            parser = PageParser()
            content = route_file(route).read_text(encoding="utf-8")
            parser.feed(content)
            cls.pages[route] = (parser, content)

    def test_unique_canonical_and_descriptions(self):
        descriptions = set()
        for route, (page, _) in self.pages.items():
            with self.subTest(route=route):
                self.assertEqual(page.canonicals, [DOMAIN + route])
                self.assertEqual(len(page.descriptions), 1)
                self.assertGreaterEqual(len(page.descriptions[0]), 70)
                descriptions.add(page.descriptions[0])
                self.assertTrue("".join(page.titles).strip())
                self.assertEqual(page.language, "en")
                self.assertEqual(page.main_count, 1)
                self.assertIn("main", page.ids)
        self.assertEqual(len(descriptions), len(ROUTES))

    def test_local_links_and_research_evidence(self):
        for route, (page, _) in self.pages.items():
            for link in page.links:
                with self.subTest(route=route, link=link):
                    parsed = urlsplit(link)
                    if link.startswith("#"):
                        self.assertIn(parsed.fragment, page.ids)
                    elif link.startswith("/"):
                        target = ROOT / parsed.path.lstrip("/")
                        if parsed.path.endswith("/"):
                            target /= "index.html"
                        self.assertTrue(target.is_file(), f"Missing public route: {link}")
                    elif link.startswith(GITHUB_PREFIX + "blob/main/"):
                        target = ROOT / link.split("/blob/main/", 1)[1]
                        self.assertTrue(target.is_file(), f"Missing canonical document: {link}")
                    elif link.startswith(GITHUB_PREFIX + "tree/main/"):
                        target = ROOT / link.split("/tree/main/", 1)[1]
                        self.assertTrue(target.is_dir(), f"Missing canonical directory: {link}")

    def test_cases_and_research_provenance(self):
        text = self.pages["/research/"][1]
        for case in ("S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"):
            self.assertIn(f"MON-G1-{case}.md", text)
        self.assertIn("Reviewer-sensitive", text)
        self.assertIn("no_evidenced_control_layer", text)
        self.assertIn("Gate 0 closed FAIL", text)
        for _, content in self.pages.values():
            self.assertNotIn("No successor category thesis is currently ratified", content)

    def test_sitemap_and_llms_consistency(self):
        sitemap = ET.parse(ROOT / "sitemap.xml")
        namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        urls = []
        for url in sitemap.findall("sm:url", namespace):
            urls.append(url.findtext("sm:loc", namespaces=namespace))
            self.assertEqual(url.findtext("sm:lastmod", namespaces=namespace), "2026-11-15")
        self.assertEqual(set(urls), {DOMAIN + route for route in ROUTES})
        self.assertEqual(len(urls), len(ROUTES))
        llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
        for url in urls:
            self.assertIn(url, llms)
        self.assertIn("DEC-008", llms)


if __name__ == "__main__":
    unittest.main()
