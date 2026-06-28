def export(data):
    lines=["# 3D Print Analysis",""]
    for k,v in data.items():
        lines.append(f"- **{k}**: {v}")
    return "\n".join(lines)
