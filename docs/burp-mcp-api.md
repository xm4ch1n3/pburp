# Burp Suite MCP API (server v1.1.2)

Captured 2026-05-06 against Burp Suite Community Edition.
Upstream: https://github.com/PortSwigger/mcp-server (`Tools.kt`).

Tool `description` and `inputSchema` are forwarded from upstream `tools/list` at
runtime; only the tool `name` is rewritten via the mapping below.

## Transport

- `http://127.0.0.1:9876/`  (root path; `/sse` also accepted by the extension)
- Legacy SSE transport: GET `/` for events, POST `/?sessionId=…` for requests
- POST returns `202 Accepted`; JSON-RPC reply arrives via SSE `event: message`
- Server: `burp-suite` 1.1.2, protocol `2024-11-05`
- Capabilities: `tools.listChanged: false`; `resources/list` → `-32601`
- Reconnect = re-run `initialize` → `notifications/initialized`; new `sessionId` issued

## Tool mapping

Source of truth for the rename table is `src/pburp/registry.py`.

### Community (21)

| Category   | Upstream                              | pburp                                       | Required args                                              |
|------------|---------------------------------------|---------------------------------------------|------------------------------------------------------------|
| Request    | `send_http1_request`                  | `community_request_http1`                   | content, targetHostname, targetPort:int, usesHttps:bool    |
| Request    | `send_http2_request`                  | `community_request_http2`                   | headers, pseudoHeaders, requestBody, target*, usesHttps    |
| Repeater   | `create_repeater_tab`                 | `community_repeater_new_tab`                | content, target*, usesHttps  (opt: tabName)                |
| Intruder   | `send_to_intruder`                    | `community_intruder_send`                   | content, target*, usesHttps  (opt: tabName)                |
| Util       | `url_encode`                          | `community_util_url_encode`                 | content                                                    |
| Util       | `url_decode`                          | `community_util_url_decode`                 | content                                                    |
| Util       | `base64_encode`                       | `community_util_base64_encode`              | content                                                    |
| Util       | `base64_decode`                       | `community_util_base64_decode`              | content                                                    |
| Util       | `generate_random_string`              | `community_util_random_string`              | characterSet, length:int                                   |
| Config     | `output_project_options`              | `community_config_project_export`           | —                                                          |
| Config     | `output_user_options`                 | `community_config_user_export`              | —                                                          |
| Config     | `set_project_options`                 | `community_config_project_import`           | json                                                       |
| Config     | `set_user_options`                    | `community_config_user_import`              | json                                                       |
| Proxy      | `get_proxy_http_history`              | `community_proxy_http_history`              | count:int, offset:int                                      |
| Proxy      | `get_proxy_http_history_regex`        | `community_proxy_http_history_regex`        | count:int, offset:int, regex                               |
| Proxy      | `get_proxy_websocket_history`         | `community_proxy_websocket_history`         | count:int, offset:int                                      |
| Proxy      | `get_proxy_websocket_history_regex`   | `community_proxy_websocket_history_regex`   | count:int, offset:int, regex                               |
| Engine     | `set_task_execution_engine_state`     | `community_engine_task_state`               | running:bool                                               |
| Intercept  | `set_proxy_intercept_state`           | `community_intercept_set_state`             | intercepting:bool                                          |
| Editor     | `get_active_editor_contents`          | `community_editor_get_active`               | —                                                          |
| Editor     | `set_active_editor_contents`          | `community_editor_set_active`               | text                                                       |

### Professional (3) — registered only when Burp edition is Professional

| Category     | Upstream                          | pburp                        | Args                            |
|--------------|-----------------------------------|------------------------------|---------------------------------|
| Scanner      | `get_scanner_issues`              | `pro_scanner_issues`         | count:int, offset:int           |
| Collaborator | `generate_collaborator_payload`   | `pro_collaborator_payload`   | customData:string? (optional)   |
| Collaborator | `get_collaborator_interactions`   | `pro_collaborator_poll`      | payloadId:string? (optional)    |
