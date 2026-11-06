import requests
import csv
import base64
print("🌐 Processing live cloud fetch...")
secret_url = "aHR0cHM6Ly9qc29ucGxhY2Vob2xkZXIudHlwaWNvZGUuY29tL3Bvc3Rz"
real_url = base64.b64decode(secret_url).decode("utf-8")
res = requests.get(real_url, timeout=10)
data = res.json()
print("✅ Net connect OK!")
p1 = data[0]
p2 = data[1]
p3 = data[2]
f = open("live_audit_report.csv", mode="w", newline="", encoding="utf-8-sig")
w = csv.writer(f)
w.writerow(["ID", "Live Title", "Word Count"])
w.writerow([p1["id"], p1["title"], len(p1["body"].split())])
w.writerow([p2["id"], p2["title"], len(p2["body"].split())])
w.writerow([p3["id"], p3["title"], len(p3["body"].split())])
f.close()
print("📊 Complete! File created: live_audit_report.csv")
