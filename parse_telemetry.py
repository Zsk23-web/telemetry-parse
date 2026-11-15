import csv
import json

FILENAME = "telemetry_sample.csv"
MAX_ROWS = 1000

def main():
    rows = []
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            if idx >= MAX_ROWS:
                break
            rows.append(row)

    alts, speeds, bats = [], [], []
    for item in rows:
        try:
            alts.append(float(item["alt_m"]))
            speeds.append(float(item["speed_mps"]))
            bats.append(float(item["battery_pct"]))
        except (ValueError, TypeError):
            continue

    output = {
        "count": len(rows),
        "avg_alt_m": round(sum(alts) / len(alts), 2) if alts else 0,
        "max_speed_mps": max(speeds) if speeds else 0,
        "min_battery_pct": min(bats) if bats else 0
    }

    with open("result.json", "w", encoding="utf-8") as out_f:
        json.dump(output, out_f, ensure_ascii=False, indent=2)
    print("处理完成，结果已保存到 result.json")
    print(output)

if __name__ == "__main__":
    main()
