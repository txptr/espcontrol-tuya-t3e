#!/usr/bin/env python3
"""Build www.js for standalone external device.

Usage:
    python3 scripts/build_www.py

Generates: docs/public/webserver/<slug>/www.js
"""
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEVICE_CONFIG = ROOT / "device-config.json"
WWW_SOURCE_LOCAL = ROOT / "src" / "webserver" / "entry.js"
WWW_OUTPUT_DIR = ROOT / "docs" / "public" / "webserver"
WWW_SOURCE_GITHUB = "https://raw.githubusercontent.com/jtenniswood/espcontrol/main/src/webserver/entry.js"

def load_device_config():
    """Load device configuration."""
    with open(DEVICE_CONFIG) as f:
        return json.load(f)

def load_espcontrol_template():
    """Load entry.js template from espcontrol repo."""
    # Try local first
    if WWW_SOURCE_LOCAL.exists():
        print(f"Loading template from {WWW_SOURCE_LOCAL.relative_to(ROOT)}")
        return WWW_SOURCE_LOCAL.read_text()

    # Fall back to GitHub
    print(f"Fetching template from {WWW_SOURCE_GITHUB}")
    try:
        with urllib.request.urlopen(WWW_SOURCE_GITHUB) as response:
            return response.read().decode()
    except Exception as e:
        raise RuntimeError(f"Failed to fetch template from GitHub: {e}")

def build_web_config(device_config):
    """Extract web UI configuration from device config."""
    web = device_config["web"]
    cfg = {
        "slots": device_config["slots"],
        "cols": device_config["layout"]["cols"],
        "rows": device_config["layout"]["rows"],
        "screenSize": device_config["public"]["screenSize"],
        "dragMode": web["dragMode"],
        "dragAnimation": web["dragAnimation"],
        "screen": web["screen"],
        "topbar": web["topbar"],
        "grid": web["grid"],
        "btn": web["btn"],
        "emptyCell": web.get("emptyCell", {}),
        "sensorBadge": web.get("sensorBadge", {}),
        "subpageBadge": web.get("subpageBadge", {}),
    }

    # Add rotation if enabled
    if device_config["rotation"]["enabled"]:
        cfg["rotationOptions"] = device_config["rotation"]["options"]

    return cfg

def replace_device_config(source_text, slug, cfg):
    """Replace __DEVICE_CONFIG__ markers in entry.js."""
    config_json = json.dumps(cfg, separators=(",", ":"))
    replacement = f'var DEVICE_ID = "{slug}";\nvar CFG = {config_json};'

    pattern = r'(^[^\n]*__DEVICE_CONFIG_START__[^\n]*\n)(.*?)(^[^\n]*__DEVICE_CONFIG_END__[^\n]*$)'
    result = re.sub(
        pattern,
        r"\1" + replacement + "\n" + r"\3",
        source_text,
        flags=re.MULTILINE | re.DOTALL
    )

    if result == source_text:
        raise ValueError("DEVICE_CONFIG markers not found in entry.js")

    return result

def minify_js(text):
    """Minify JavaScript with esbuild if available, else return as-is."""
    try:
        result = subprocess.run(
            ["esbuild", "--minify", "--target=es2020"],
            input=text,
            capture_output=True,
            text=True,
            timeout=30,
            check=False
        )
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"⚠️  esbuild failed: {result.stderr}")
            return text
    except FileNotFoundError:
        print("⚠️  esbuild not found; skipping minification (install with: npm install -g esbuild)")
        return text
    except subprocess.TimeoutExpired:
        print("⚠️  esbuild timeout; skipping minification")
        return text

def main():
    try:
        device_config = load_device_config()
        slug = device_config["slug"]

        print(f"Building www.js for {slug}...")

        source_text = load_espcontrol_template()
        web_cfg = build_web_config(device_config)
        source_text = replace_device_config(source_text, slug, web_cfg)
        source_text = minify_js(source_text)

        output_path = WWW_OUTPUT_DIR / slug / "www.js"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(source_text)

        print(f"✓ Generated: {output_path.relative_to(ROOT)}")
        print(f"  Size: {len(source_text)} bytes")
        return 0
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
