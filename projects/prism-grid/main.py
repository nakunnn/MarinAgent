def format_table(headers: list[str], rows: list[list[str]]) -> str:
    cols = len(headers)
    widths = [len(h) for h in headers]
    for r in rows:
        for i in range(cols):
            widths[i] = max(widths[i], len(str(r[i])))
    header_str = "| " + " | ".join(h.ljust(widths[i]) for i, h in enumerate(headers)) + " |"
    sep_str = "|-" + "-|-".join("-" * widths[i] for i in range(cols)) + "-|"
    row_strs = ["| " + " | ".join(str(r[i]).ljust(widths[i]) for i in range(cols)) + " |" for r in rows]
    return "\n".join([header_str, sep_str] + row_strs)

if __name__ == '__main__':
    h = ["Service", "Node", "Port"]
    d = [["Performa", "Server Eks", "5511"], ["Nextcloud", "Server In", "8080"]]
    tbl = format_table(h, d)
    print(tbl)
    assert "Performa" in tbl
