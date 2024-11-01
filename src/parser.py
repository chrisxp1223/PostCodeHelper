import re
import pandas as pd

def parse_log(file_path):
    log_data = []
    with open(file_path, 'r') as file:
        for line in file:
            # 使用正則表達式匹配log的每個欄位
            match = re.match(r"(\S+)\s+(\S+)\s+(\d+)\s+(\d+)\(μs\)\s+(\d+)\(μs\)", line)
            if match:
                post_code, size, index, start_timestamp, duration = match.groups()
                log_data.append({
                    "POSTCode": post_code,
                    "Size": size,
                    "Index": int(index),
                    "Start_Timestamp": int(start_timestamp),
                    "Duration": int(duration)
                })
    # 使用pandas將log資料轉換成DataFrame格式，方便後續分析
    return pd.DataFrame(log_data)

# 測試解析功能
if __name__ == "__main__":
    df = parse_log("logs/sample_log.txt")
    # 設置顯示的最大行數為100（或其他數字），以便查看更多資料
    pd.set_option("display.max_rows", 100)
    print(df)