from datetime import datetime

print("龍蝦開始工作")

now = datetime.now()

with open("report.txt","a",encoding="utf8") as f:
    f.write(f"{now}\n")
    f.write("龍蝦今天完成巡邏任務\n\n")

print("工作完成")
