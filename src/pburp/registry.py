"""Tool registry mapping upstream Burp names to pburp exposed names."""

TOOL_REGISTRY: dict[str, dict[str, str]] = {
    # --- Community ---
    "send_http1_request": {"our_name": "community_request_http1", "tier": "community"},
    "send_http2_request": {"our_name": "community_request_http2", "tier": "community"},
    "create_repeater_tab": {"our_name": "community_repeater_new_tab", "tier": "community"},
    "send_to_intruder": {"our_name": "community_intruder_send", "tier": "community"},
    "url_encode": {"our_name": "community_util_url_encode", "tier": "community"},
    "url_decode": {"our_name": "community_util_url_decode", "tier": "community"},
    "base64_encode": {"our_name": "community_util_base64_encode", "tier": "community"},
    "base64_decode": {"our_name": "community_util_base64_decode", "tier": "community"},
    "generate_random_string": {"our_name": "community_util_random_string", "tier": "community"},
    "output_project_options": {"our_name": "community_config_project_export", "tier": "community"},
    "output_user_options": {"our_name": "community_config_user_export", "tier": "community"},
    "set_project_options": {"our_name": "community_config_project_import", "tier": "community"},
    "set_user_options": {"our_name": "community_config_user_import", "tier": "community"},
    "get_proxy_http_history": {"our_name": "community_proxy_http_history", "tier": "community"},
    "get_proxy_http_history_regex": {
        "our_name": "community_proxy_http_history_regex",
        "tier": "community",
    },
    "get_proxy_websocket_history": {
        "our_name": "community_proxy_websocket_history",
        "tier": "community",
    },
    "get_proxy_websocket_history_regex": {
        "our_name": "community_proxy_websocket_history_regex",
        "tier": "community",
    },
    "set_task_execution_engine_state": {
        "our_name": "community_engine_task_state",
        "tier": "community",
    },
    "set_proxy_intercept_state": {"our_name": "community_intercept_set_state", "tier": "community"},
    "get_active_editor_contents": {"our_name": "community_editor_get_active", "tier": "community"},
    "set_active_editor_contents": {"our_name": "community_editor_set_active", "tier": "community"},
    # --- Professional (upstream names verified against portswigger/mcp-server Tools.kt) ---
    "get_scanner_issues": {"our_name": "pro_scanner_issues", "tier": "pro"},
    "generate_collaborator_payload": {"our_name": "pro_collaborator_payload", "tier": "pro"},
    "get_collaborator_interactions": {"our_name": "pro_collaborator_poll", "tier": "pro"},
}
