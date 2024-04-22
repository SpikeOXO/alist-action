import sys
import requests
import time

def check_api_status():
    print("alist starting......")
    time.sleep(30)  # 等待 3 秒
    print("alist starting......")
    while True:
        response = requests.post(
            "http://localhost:5244/api/fs/list",
            headers={
                "Content-Type": "application/json",
                "Authorization": "alist-cea0a14f-a00b-4be5-be8a-8534c7ad93b4cKYFaynqjncwQjZSc1hEohcoIZsraCUq4sbKl313lSazI0XEDrHSsvXOpw6ziKL7"
            },
            json={"path": "", "page": 1, "per_page": 0, "refresh": False}
        )
        if response.status_code == 200:
            print(response)
            return True
        else:
            print(response)
            print("alist starting......")
            time.sleep(5) 

# 调用函数

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "status":
        check_api_status()
    else:
        print("Usage: python test.py status")
