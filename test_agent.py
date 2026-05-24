import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from email_composer import compose_email
from config import Config

FAKE_WORK_ORDERS = [
    {
        "work_order_number": "WO-2024-00142",
        "customer_name": "Riverside Medical Center",
        "technician": "James Carter",
        "summary": "Replaced faulty power supply on HP LaserJet Pro MFP. Full diagnostic complete.",
        "completed_date": "2024-11-15T14:30:00Z"
    }
]

def preview_only():
    wo = FAKE_WORK_ORDERS[0]
    _, html = compose_email(wo["customer_name"], wo["work_order_number"],
                            wo["summary"], wo["technician"], wo["completed_date"])
    path = os.path.join(os.path.dirname(__file__), "email_preview.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"\n✅ Preview saved to: {path}\n")
    print("Copy that path and open it in your browser!\n")

if __name__ == "__main__":
    preview_only()
