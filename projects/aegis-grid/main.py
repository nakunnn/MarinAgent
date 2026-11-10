import csv
import io
import json

def csv_to_json(csv_text: str) -> str:
    reader = csv.DictReader(io.StringIO(csv_text.strip()))
    return json.dumps([row for row in reader], indent=2)

if __name__ == '__main__':
    data = "service,port,status\nhermes,8787,running\ncasaos,80,running"
    out = csv_to_json(data)
    print(out)
    assert "hermes" in out
