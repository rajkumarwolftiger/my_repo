from datetime import datetime
x = True
while x != True:
    with open("daily_log.txt", "a") as f:
        f.write(f"Committed at: {datetime.utcnow().isoformat()}Z\n")
