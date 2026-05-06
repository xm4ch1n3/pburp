"""pburp MCP server — proxies upstream Burp MCP and renames tools."""

from __future__ import annotations

import asyncio
import os

from dotenv import load_dotenv
from fastmcp import Client
from fastmcp.client.transports import SSETransport
from fastmcp.server import create_proxy
from fastmcp.server.transforms import ToolTransform
from fastmcp.tools.tool_transform import ToolTransformConfig

from pburp.registry import TOOL_REGISTRY

load_dotenv()
BURP_MCP_URL = os.environ["BURP_MCP_URL"]


# NOTE: Burp's official MCP extension speaks the legacy SSE transport (GET /
# yields an `endpoint` event, JSON-RPC POSTs go to /?sessionId=...). FastMCP's
# `Client` would otherwise infer Streamable-HTTP from a bare URL and fail with
# 400 on POST. Always pin SSETransport for upstream connections.
def burp_client() -> Client:
    return Client(SSETransport(BURP_MCP_URL))


mcp = create_proxy(burp_client(), name="pburp")
mcp.add_transform(
    ToolTransform(
        {
            upstream: ToolTransformConfig(name=meta["our_name"])
            for upstream, meta in TOOL_REGISTRY.items()
        }
    )
)


# --- Python extras (Augment Layer) ---
# TODO: implement; stubs below capture the intended surface area. Uncomment the
# `@mcp.tool(...)` decorator and replace the body once the function is real.


# @mcp.tool(description="Decode and analyze JWT tokens from observed traffic")
def extract_jwt(token: str) -> dict:
    raise NotImplementedError


# @mcp.tool(description="Regex-scan proxy history for API keys, tokens, and credentials")
def find_secrets(patterns: list[str] | None = None) -> list[dict]:
    raise NotImplementedError


# @mcp.tool(description="Compare two responses from proxy history and return a unified diff")
def diff_responses(history_id_a: int, history_id_b: int) -> str:
    raise NotImplementedError


# @mcp.tool(description="Parse a raw HTTP request into structured query/body/header parameters")
def extract_params(request: str) -> dict:
    raise NotImplementedError


# @mcp.tool(
#     description="Build a wordlist from observed paths, parameter names, and values in proxy history"
# )
def generate_wordlist(scope: str = "all") -> list[str]:
    raise NotImplementedError


async def check_registry_drift() -> None:
    """Fail fast if upstream tools and TOOL_REGISTRY don't match.

    Community-tier tools must be present upstream; Pro-tier tools are optional
    (only exposed when running against a Burp Suite Professional license).
    Any upstream tool not in the registry is treated as drift.
    """
    async with burp_client() as client:
        upstream = {t.name for t in await client.list_tools()}
    required = {name for name, meta in TOOL_REGISTRY.items() if meta["tier"] == "community"}
    if missing := required - upstream:
        raise RuntimeError(f"Community tools in registry but not upstream: {sorted(missing)}")
    if unknown := upstream - set(TOOL_REGISTRY):
        raise RuntimeError(f"Upstream tools not in registry: {sorted(unknown)}")


def main() -> None:
    asyncio.run(check_registry_drift())
    mcp.run()


if __name__ == "__main__":
    main()
