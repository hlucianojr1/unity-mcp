"""
Configuration settings for the MCP for Unity Server.
This file contains all configurable parameters for the server.
"""

from dataclasses import dataclass

@dataclass
class ServerConfig:
    """Main configuration class for the MCP server."""
    
    # Network settings
    unity_host: str = "localhost"
    unity_port: int = 6400
    mcp_port: int = 6500
    
    # Connection settings
    connection_timeout: float = 10.0  # short initial timeout; retries use shorter timeouts
    handshake_timeout: float = 10.0  # timeout for Unity handshake negotiation
    buffer_size: int = 16 * 1024 * 1024  # 16MB buffer
    # Framed receive behavior
    framed_receive_timeout: float = 10.0  # max seconds to wait while consuming heartbeats only
    max_heartbeat_frames: int = 16       # cap heartbeat frames consumed before giving up
    
    # Logging settings
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Server settings
    max_retries: int = 10
    retry_delay: float = 0.25
    retry_timeout: float = 1.0  # short timeout during retry bursts
    # Backoff hint returned to clients when Unity is reloading (milliseconds)
    reload_retry_ms: int = 250
    # Number of polite retries when Unity reports reloading
    # 40 × 250ms ≈ 10s default window
    reload_max_retries: int = 40
    
    # Telemetry settings
    telemetry_enabled: bool = True
    # Align with telemetry.py default Cloud Run endpoint
    telemetry_endpoint: str = "https://api-prod.coplay.dev/telemetry/events"

# Create a global config instance
config = ServerConfig() 