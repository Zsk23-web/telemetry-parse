import csv
import json

def main():
    # 读取前1000行csv
    result_list = []
    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            if idx >= 1000:
                break
            result_list.append(row)

    # 计算指标，这里假设字段：height高度, speed速度, power电量
    heights = []
    speeds = []
    power = []
    for item in result_list:
        try:
            heights.append(float(item["height"]))
            speeds.append(float(item["speed"]))
            power.append(float(item["power"]))
        except Exception:
            continue

    if heights:
        avg_height = sum(heights) / len(heights)
        max_speed = max(speeds)
        min_power = min(power)
    else:
        avg_height = 0
        max_speed = 0
        min_power = 0

    output = {
        "count": len(result_list),
        "avg_height": avg_height,
        "max_speed": max_speed,
        "min_power": min_power
    }

    # 写入result.json
    with open("result.json", "w", encoding="utf-8") as out_f:
        json.dump(output, out_f, ensure_ascii=False, indent=2)
    print("处理完成，结果已保存到 result.json")


if __name__ == "__main__":
    main()
