# Rickuu deployment

Fork of https://github.com/zizifn/edgetunnel. Upstream source and GPL-2.0 license are preserved.

- Worker: `opencode-edgetunnel` in the Cloudflare account containing `rickuu.com`.
- Build: `python3 scripts/prepare-worker.py`.
- Deploy: `npx wrangler deploy --config wrangler.rickuu.toml`.
- Required runtime secret: `UUID`. Never commit it, proxy credentials or Cloudflare tokens.
- `/healthz` reports liveness; subscription/configuration pages are disabled.
- Optional `PROXYIP` is operator-supplied; no third-party relay is configured by default.

GitHub Actions merges upstream every six hours. Overlay preparation and JavaScript syntax must pass before pushing. A changed upstream shape stops synchronization for review. Cloudflare Git integration deploys pushes to `main` when connected.

Cloudflare Workers blocks outbound TCP sockets to Cloudflare IPs. A successful health check does not establish OpenCode connectivity. Verify the actual upstream before switching production proxy configuration.
