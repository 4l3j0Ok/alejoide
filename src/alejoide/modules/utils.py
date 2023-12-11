def hex_to_rgba(hex: str, transparency: float = 1.0) -> str:
    hex = hex.lstrip("#")
    hlen = len(hex)
    return f"rgba({int(hex[hlen - 6:hlen - 4], 16)}, {int(hex[hlen - 4:hlen - 2], 16)}, {int(hex[hlen - 2:hlen], 16)}, {transparency})"