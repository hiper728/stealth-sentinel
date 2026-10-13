from sentinel.core import PageSnapshot

def test_html_parsing():
    html = "<html><body><h1>Header 1</h1><a href='https://example.com'>Link</a></body></html>"
    snap = PageSnapshot.inspect_html(html)
    assert snap["headings_count"] == 1
    assert snap["links_count"] == 1
    assert len(snap["content_hash"]) == 64

def test_diff_snapshots():
    s1 = PageSnapshot.inspect_html("<h1>Alpha</h1>")
    s2 = PageSnapshot.inspect_html("<h1>Beta</h1>")
    diff = PageSnapshot.diff_snapshots(s1, s2)
    assert diff["has_changed"] is True
