from urllib.parse import parse_qs, urlencode

def parse_url_query(query_str: str) -> dict:
    return {k: v[0] if len(v) == 1 else v for k, v in parse_qs(query_str).items()}

if __name__ == '__main__':
    q = "status=active&tag=system&limit=50"
    parsed = parse_url_query(q)
    print("Parsed Query:", parsed)
    assert parsed["status"] == "active"
