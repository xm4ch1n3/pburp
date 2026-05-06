<div align="center">
<pre>
>>=========================================<<
||██████╗ ██████╗ ██╗   ██╗██████╗ ██████╗ ||
||██╔══██╗██╔══██╗██║   ██║██╔══██╗██╔══██╗||
||██████╔╝██████╔╝██║   ██║██████╔╝██████╔╝||
||██╔═══╝ ██╔══██╗██║   ██║██╔══██╗██╔═══╝ ||
||██║     ██████╔╝╚██████╔╝██║  ██║██║     ||
||╚═╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝     ||
>>=========================================<<
</pre>
  <strong>Intercept everything at agent speed.</strong>
  <br><br>
</div>


A Python MCP server wrapping PortSwigger's [official](https://github.com/portswigger/mcp-server) Burp Suite MCP extension, with some extras layered on top that might expand as workflows demand.
All respect goes to the architects.

> **Status: WIP**

---

## Install

### Prerequisites
- Burp Suite (Community or Professional) with PortSwigger's
  [MCP Server extension](https://github.com/PortSwigger/mcp-server) loaded and enabled.
  Default endpoint: `http://127.0.0.1:9876`.
- [`uv`](https://docs.astral.sh/uv/) on `PATH`.

### Clone & sync

```bash
git clone https://github.com/xm4ch1n3/pburp.git
cd pburp
uv sync
```

### Configure your agent host

Replace `<path-to-pburp>` with the absolute path to your clone.

#### opencode (`~/.config/opencode/opencode.json`)

Add this block under `mcp`:

```json
"pburp": {
  "type": "local",
  "command": ["uv", "run", "--quiet", "--project", "<path-to-pburp>", "mcp-pburp"],
  "environment": { "BURP_MCP_URL": "http://127.0.0.1:9876" },
  "enabled": true,
  "timeout": 300000
}
```

### Verify

```bash
opencode mcp list
```

`pburp` should report as connected. If startup fails with a registry-drift error,
Burp isn't running or the MCP extension isn't enabled — start Burp, then re-run.

---

## Expected Functionality

### Core: Burp Suite Integration

All tools exposed by PortSwigger's official MCP extension, surfaced under `community_*` / `pro_*` prefixes. Tool descriptions and JSON input schemas are forwarded verbatim from upstream `tools/list` at runtime; only the tool `name` is rewritten by pburp. See [`docs/burp-mcp-api.md`](./docs/burp-mcp-api.md) for the upstream-to-pburp mapping.

> **Edition note:** Tools marked 🔒 require **Burp Suite Professional**. All others work with the free **Community Edition**.

| Tool | Description | Edition |
|------|-------------|---------|
| `community_request_http1` | Issue an HTTP/1.1 request and return the response | Community |
| `community_request_http2` | Issue an HTTP/2 request and return the response | Community |
| `community_repeater_new_tab` | Create a new Repeater tab with a specified request | Community |
| `community_intruder_send` | Send a request to Intruder | Community |
| `community_proxy_http_history` | Read proxy HTTP history (paginated) | Community |
| `community_proxy_http_history_regex` | Read proxy HTTP history filtered by regex (paginated) | Community |
| `community_proxy_websocket_history` | Read proxy WebSocket history (paginated) | Community |
| `community_proxy_websocket_history_regex` | Read proxy WebSocket history filtered by regex (paginated) | Community |
| `community_intercept_set_state` | Enable or disable Proxy Intercept | Community |
| `community_config_project_export` | Export project-level configuration as JSON | Community |
| `community_config_user_export` | Export user-level configuration as JSON | Community |
| `community_config_project_import` | Import/merge project-level configuration from JSON | Community |
| `community_config_user_import` | Import/merge user-level configuration from JSON | Community |
| `community_engine_task_state` | Pause or resume Burp's task execution engine | Community |
| `community_editor_get_active` | Read the currently active message editor | Community |
| `community_editor_set_active` | Write to the currently active message editor | Community |
| `community_util_url_encode` / `community_util_url_decode` | URL encoding/decoding | Community |
| `community_util_base64_encode` / `community_util_base64_decode` | Base64 encoding/decoding | Community |
| `community_util_random_string` | Generate a random string | Community |
| `pro_scanner_issues` | Retrieve scanner findings | 🔒 Professional |
| `pro_collaborator_payload` | Generate an OOB payload | 🔒 Professional |
| `pro_collaborator_poll` | Poll for OOB interactions | 🔒 Professional |

### Python Extras (Augment Layer)

Custom tools that don't exist in Burp but make AI-driven workflows smoother:

| Tool | Description |
|------|-------------|
| `extract_jwt` | Decode and analyze JWT tokens from traffic |
| `find_secrets` | Regex-scan history for API keys, tokens, credentials |
| `diff_responses` | Compare two responses from proxy history |
| `extract_params` | Parse a request into structured parameters |
| `generate_wordlist` | Build a wordlist from observed paths/params/values |

---

## License

See [LICENSE](./LICENSE).
