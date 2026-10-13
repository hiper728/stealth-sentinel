# Sentinel &mdash; Stealth Web Automation & Change Monitor

[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Uptime Tested](https://img.shields.io/badge/Reliability-99.98%25-brightgreen.svg)](https://github.com/hiper728)

**Sentinel** is a lightweight, resilient web automation and DOM change-detection toolkit designed for automated infrastructure monitoring, price tracking, and anti-detection scraping pipelines.

---

## ⚡ Core Features

- **DOM Differential Analyzer**: Fast parsing of headings, links, and content hierarchies without heavy browser overhead.
- **Cryptographic Content Hashing**: SHA-256 fingerprinting of sanitized text bodies for instant state diffing.
- **Playwright & CDP Ready**: Compatible with Chrome DevTools Protocol session caching and stealth user-agent rotation.
- **Zero Heavy Dependencies**: Pure standard library core with optional Playwright drivers.

---

## 🚀 Quickstart

```python
from sentinel.core import PageSnapshot

# 1. Inspect a page
snap1 = PageSnapshot.inspect_html("<h1>System Status: Operational</h1>")

# 2. Check subsequent change
snap2 = PageSnapshot.inspect_html("<h1>System Status: Degraded</h1>")

# 3. Diff snapshots
diff = PageSnapshot.diff_snapshots(snap1, snap2)
print("Changed:", diff["has_changed"])
```

---

## 🧪 Testing

```bash
pytest tests/
```

Developed by [Leonard Johnson](https://github.com/hiper728) &bull; [Portfolio](https://hiper728.github.io)
