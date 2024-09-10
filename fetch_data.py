import requests
import os
import json
from datetime import datetime
import pytz
import time

# 获取环境变量
access_token = os.getenv('FB_ACCESS_TOKEN')
url = os.getenv('URL')
one = os.getenv('ONE')
three = os.getenv('THREE')

# 设置请求参数
params1 = {
    'fields': 'business_discovery.username(' + one + '){followers_count,username}',
    'access_token': access_token
}
params2 = {
    'fields': 'business_discovery.username(' + three + '){followers_count,username}',
    'access_token': access_token
}

# 设置时区和时间格式
korea_timezone = pytz.timezone('Asia/Seoul')

def fetch_and_write_data(username, params, filename,formatted_time):
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json().get("business_discovery")
            followers_count = data.get('followers_count', "未知粉丝数")
            with open(filename, 'a') as file:
                file.write(f"{username},{followers_count},{formatted_time}\\n")
        else:
            print(f"请求失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"发生错误: {e}")

for _ in range(1):
    # 获取当前时间
    time_now = datetime.now(korea_timezone)
    formatted_time = time_now.strftime('%Y-%m-%d %H:%M:%S')
    fetch_and_write_data('1', params1, 'output_1.txt',formatted_time)
    fetch_and_write_data('3', params2, 'output_3.txt',formatted_time)
    time.sleep(60)
