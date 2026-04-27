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

## Expected Functionality

### Core: Burp Suite Integration

All tools exposed by PortSwigger's official MCP extension, grouped by prefix.

> **Edition note:** Tools marked 🔒 require **Burp Suite Professional**. All others work with the free **Community Edition**.

| Prefix | Tool | Description | Edition |
|--------|------|-------------|---------|
| `request_*` | `request_http1` | Issue an HTTP/1.1 request and return the response | Community |
| `request_*` | `request_http2` | Issue an HTTP/2 request and return the response | Community |
| `repeater_*` | `repeater_new_tab` | Create a new Repeater tab with a specified request | Community |
| `intruder_*` | `intruder_send` | Send a request to Intruder | Community |
| `proxy_*` | `proxy_http_history` | Read proxy HTTP history (paginated) | Community |
| `proxy_*` | `proxy_http_history_regex` | Read proxy HTTP history filtered by regex (paginated) | Community |
| `proxy_*` | `proxy_websocket_history` | Read proxy WebSocket history (paginated) | Community |
| `proxy_*` | `proxy_websocket_history_regex` | Read proxy WebSocket history filtered by regex (paginated) | Community |
| `intercept_*` | `intercept_set_state` | Enable or disable Proxy Intercept | Community |
| `config_*` | `config_project_export` | Export project-level configuration as JSON | Community |
| `config_*` | `config_user_export` | Export user-level configuration as JSON | Community |
| `config_*` | `config_project_import` | Import/merge project-level configuration from JSON | Community |
| `config_*` | `config_user_import` | Import/merge user-level configuration from JSON | Community |
| `engine_*` | `engine_task_state` | Pause or resume Burp's task execution engine | Community |
| `editor_*` | `editor_get_active` | Read the currently active message editor | Community |
| `editor_*` | `editor_set_active` | Write to the currently active message editor | Community |
| `util_*` | `util_url_encode` / `util_url_decode` | URL encoding/decoding | Community |
| `util_*` | `util_base64_encode` / `util_base64_decode` | Base64 encoding/decoding | Community |
| `util_*` | `util_random_string` | Generate a random string | Community |
| `scanner_*` | `scanner_issues` | Retrieve scanner findings | 🔒 Professional |
| `collaborator_*` | `collaborator_payload` | Generate an OOB payload | 🔒 Professional |
| `collaborator_*` | `collaborator_poll` | Poll for OOB interactions | 🔒 Professional |

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
