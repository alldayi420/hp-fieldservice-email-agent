import time, logging
from email_composer import compose_email

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

FAKE_WORK_ORDERS = [
    {"id": "WO-2024-00891", "customer_name": "Riverside Medical Center", "customer_email": "facilities@riversidemedical.com", "technician": "Jason Szymarek", "summary": "Replaced failed fuser assembly on HP LaserJet Enterprise M607. Full diagnostic and calibration complete.", "completed_date": "2024-11-15T14:30:00Z", "product": "HP LaserJet Enterprise M607"},
    {"id": "WO-2024-00892", "customer_name": "Greenfield Law Associates", "customer_email": "office@greenfieldlaw.com", "technician": "Jason Szymarek", "summary": "Resolved paper jam and replaced worn feed rollers on HP OfficeJet Pro 9015. Firmware updated.", "completed_date": "2024-11-15T16:00:00Z", "product": "HP OfficeJet Pro 9015"},
    {"id": "WO-2024-00893", "customer_name": "Summit Financial Group", "customer_email": "it@summitfinancial.com", "technician": "Jason Szymarek", "summary": "Replaced defective ink delivery system on HP DesignJet T650. Color calibration passed.", "completed_date": "2024-11-15T17:15:00Z", "product": "HP DesignJet T650"}
]

def run_demo():
    print("\n" + "="*60)
    print("  HP FIELD SERVICE — FOLLOW-UP EMAIL AGENT")
    print("  DEMO MODE — Simulating Live Dynamics 365 Connection")
    print("="*60 + "\n")
    log.info("Connecting to Microsoft Azure...")
    time.sleep(1.5)
    log.info("✅ Authenticated with Dynamics 365 Field Service")
    time.sleep(0.5)
    print()
    log.info("Querying Dynamics 365 for completed work orders...")
    time.sleep(2)
    log.info(f"✅ Found {len(FAKE_WORK_ORDERS)} completed work orders pending follow-up")
    print()
    sent_count = 0
    for i, wo in enumerate(FAKE_WORK_ORDERS, 1):
        print("─"*60)
        log.info(f"Processing Work Order {i}/{len(FAKE_WORK_ORDERS)}: {wo['id']}")
        log.info(f"   Product: {wo['product']}")
        time.sleep(0.5)
        log.info(f"   Fetching customer: {wo['customer_name']}")
        time.sleep(0.8)
        subject, html_body = compose_email(wo["customer_name"], wo["id"], wo["summary"], wo["technician"], wo["completed_date"])
        log.info(f"   Email composed: '{subject}'")
        time.sleep(0.5)
        filename = f"demo_email_{wo['id'].replace('-','_')}.html"
        with open(filename, "w") as f:
            f.write(html_body)
        log.info(f"   Sending to: {wo['customer_email']}")
        time.sleep(1.2)
        log.info(f"   ✅ Email sent! Preview saved: {filename}")
        time.sleep(0.5)
        log.info(f"   💾 Marked {wo['id']} complete in Dynamics 365")
        sent_count += 1
        print()
    print("="*60)
    print(f"  ✅ DEMO COMPLETE — {sent_count} emails sent automatically")
    print(f"  ⏱️  Zero manual effort by the technician")
    print(f"  💡 In production: runs every 30 min on HP's existing stack")
    print("="*60 + "\n")

if __name__ == "__main__":
    run_demo()
