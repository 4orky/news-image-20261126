# Entry shim for the 26 November 2026 news-image bounty: it places a finished 1024-pixel front-page PNG at the location make.fun expects, checking the bytes before and after the copy so a truncated file can never slip through silently.
# The picture itself lives beside this file as entry.png and was painted beforehand by render.py; this shim needs nothing beyond the Python standard library and touches no network at all.
import hashlib as _hashlib
import os as _os
import struct as _struct
import sys as _sys
from pathlib import Path as _Path
_BASE=_Path(__file__).resolve().parent
_INCOMING=_BASE/"entry.png"
_DESTINATION=_Path(_os.environ.get("MAKEFUN_OUTPUT_DIR","/output"))/"entry.png"
_CEILING_BYTES=1048576
_CEILING_EDGE=1024
def _digest(_blob):
    return _hashlib.sha256(_blob).hexdigest()
def _inspect(_blob):
    if len(_blob)>_CEILING_BYTES:
        raise SystemExit(f"entry.png holds {len(_blob)} bytes, above the 1048576-byte ceiling")
    if _blob[:8]!=b"\x89PNG\r\n\x1a\n" or _blob[12:16]!=b"IHDR":
        raise SystemExit("entry.png does not start with a PNG signature and IHDR chunk")
    _wide,_tall=_struct.unpack(">II",_blob[16:24])
    if _wide>_CEILING_EDGE or _tall>_CEILING_EDGE:
        raise SystemExit(f"entry.png measures {_wide}x{_tall}, above the 1024x1024 ceiling")
    return _wide,_tall
def _place():
    if not _INCOMING.is_file():
        raise SystemExit("entry.png is absent from this repository, nothing to place")
    _payload=_INCOMING.read_bytes()
    _wide,_tall=_inspect(_payload)
    _DESTINATION.parent.mkdir(parents=True,exist_ok=True)
    _DESTINATION.write_bytes(_payload)
    _back=_DESTINATION.read_bytes()
    if _digest(_back)!=_digest(_payload):
        raise SystemExit("the bytes read back from the destination do not match entry.png")
    print(f"placed {_DESTINATION} ({len(_payload)} bytes, {_wide}x{_tall}, sha256 {_digest(_payload)})")
_place()
