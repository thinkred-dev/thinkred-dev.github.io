#!/usr/bin/env python3
"""Post-build: fill each page's CSP <meta> with sha256 hashes of its inline scripts.

Usage: python3 scripts/csp_hashes.py public
Fails (exit 1) if any HTML page has an inline event handler (onclick= etc.),
because those can't be allowed by a hash without weakening the policy.
"""
import base64, hashlib, pathlib, re, sys

PLACEHOLDER = "'__CSP_SCRIPT_HASHES__'"
SCRIPT_RE = re.compile(r"<script(?P<attrs>[^>]*)>(?P<body>.*?)</script>", re.S | re.I)
HANDLER_RE = re.compile(r"<[^>]+\son[a-z]+\s*=", re.I)

def inline_hashes(html: str) -> list[str]:
    hashes = []
    for m in SCRIPT_RE.finditer(html):
        attrs = m.group("attrs").lower()
        if "src=" in attrs or "application/ld+json" in attrs:
            continue                      # external files / JSON-LD data blocks
        digest = hashlib.sha256(m.group("body").encode()).digest()
        h = f"'sha256-{base64.b64encode(digest).decode()}'"
        if h not in hashes:
            hashes.append(h)
    return hashes

def main(root: str) -> int:
    pages = errors = 0
    for path in pathlib.Path(root).rglob("*.html"):
        html = path.read_text(encoding="utf-8")
        if HANDLER_RE.search(html):
            print(f"ERROR inline event handler in {path}")
            errors += 1
        if PLACEHOLDER not in html:
            continue
        hashes = inline_hashes(html)
        path.write_text(html.replace(PLACEHOLDER, " ".join(hashes) if hashes else ""), encoding="utf-8")
        pages += 1
    leftover = [p for p in pathlib.Path(root).rglob("*.html") if PLACEHOLDER in p.read_text(encoding="utf-8")]
    print(f"CSP hashes written to {pages} pages")
    if leftover or errors:
        print(f"FAILED: {len(leftover)} pages still have the placeholder, {errors} pages with inline handlers")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "public"))
