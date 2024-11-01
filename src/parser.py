import re
import pandas as pd

# POST Code定義字典
POST_CODE_DEFINITIONS = {
    "EA00E0FC": "Abl0Begin",
    "EA00E0B1": "ABL 1 Initialization",
    "EA00E098": "GNB internal debug code",
    "EA00E0B7": "ABL 1 End",
    "EA00E001": "Memory structure initialization (Public interface)",
    # 根據需求擴充此字典
}

def parse_log(file_path):
    log_data = []
    with open(file_path, 'r') as file:
        for line in file:
            # 使用正則表達式匹配log的每個欄位
            match = re.match(r"(\S+)\s+(\S+)\s+(\d+)\s+(\d+)\(μs\)\s+(\d+)\(μs\)", line)
            if match:
                post_code, size, index, start_timestamp, duration = match.groups()

                # 根據POST Code查找定義，若未找到則回傳"Undefined"
                post_code_define = POST_CODE_DEFINITIONS.get(post_code, "Undefined")
                
                log_data.append({
                    "POSTCode": post_code,
                    "Size": size,
                    "Index": int(index),
                    "Start_Timestamp": int(start_timestamp),
                    "Duration": int(duration),
                    "POST_Code Define": post_code_define
                })
    
    # 將log資料轉換成DataFrame格式，方便後續分析
    return pd.DataFrame(log_data)

# 測試解析功能
if __name__ == "__main__":
    df = parse_log("logs/sample_log.txt")
    # 設置顯示的最大行數為100（或其他數字），以便查看更多資料
    pd.set_option("display.max_rows", 100)
    print(df)