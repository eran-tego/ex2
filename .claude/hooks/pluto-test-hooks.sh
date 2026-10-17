#!/bin/bash
# === PLUTO TEST HOOKS RUNNER ===
# Local stand-in for HERO-12231 (per-install ID blanking). Sends nothing anywhere.
# To test: collect, change ENDPOINT_IDENTIFIER, collect again. The hook's
# fingerprint and script sha256 should stay the same.
BACKEND_URL="https://example.invalid"
SCRIPT_VERSION="0.0.1"
ENDPOINT_IDENTIFIER="fedcba9876543210fedc"
cat >/dev/null
exit 0
