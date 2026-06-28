
def export(data):
    out=["# Printing Report",""]
    for k,v in data.items():
        out.append(f"- **{k}**: {v}")
    return "\n".join(out)
