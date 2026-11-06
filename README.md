# thinkred.dev

Source for **[Think Red](https://thinkred.dev)**: red team tradecraft, explained, and how defenders catch it.

Built with [Hugo](https://gohugo.io) and the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme (pinned as a submodule), with a custom dark/red theme in `assets/css/extended/`. Deployed to GitHub Pages by GitHub Actions.

## Local development

```bash
git clone --recurse-submodules <repo-url>
hugo server -D          # http://localhost:1313, drafts included
```

New content uses the archetypes in `archetypes/`:

```bash
hugo new content blog/my-post.md
hugo new content labs/my-lab.md
hugo new content papers/my-paper.md
hugo new content tools/my-tool.md
hugo new content notes/my-note.md
```

## Production build

```bash
hugo --gc --minify
python3 scripts/csp_hashes.py public   # fills per-page CSP script hashes
```

## Security

- GitHub Actions pinned to commit SHAs, least-privilege permissions, checksum-verified Hugo binary
- Strict Content-Security-Policy (`<meta>`), with inline scripts allowed only by per-page sha256 hash
- No third-party scripts, fonts, trackers, or analytics
- `/.well-known/security.txt` (RFC 9116)
- Signed commits; `.githooks/pre-push` enforces identity, signatures, and main-only publishing

Report issues to the contact in [security.txt](https://thinkred.dev/.well-known/security.txt).

## License

Content © Think Red, all rights reserved unless stated otherwise. Code in `scripts/` and `.githooks/` is MIT-licensed.
