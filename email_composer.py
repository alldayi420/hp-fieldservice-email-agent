from datetime import datetime
from config import Config

def format_date(iso_string):
    try:
        dt = datetime.fromisoformat(iso_string.replace("Z", "+00:00"))
        return dt.strftime("%B %d, %Y at %I:%M %p")
    except:
        return iso_string

def compose_email(customer_name, work_order_number, summary, technician, completed_date):
    subject = f"Your HP Service Visit is Complete — Work Order #{work_order_number}"
    first_name = customer_name.split()[0] if customer_name else "Valued Customer"
    formatted_date = format_date(completed_date)
    html_body = f"""<!DOCTYPE html>
<html><body style="font-family:Arial,sans-serif;background:#f5f5f5;padding:20px;">
<table width="600" style="background:#fff;border-radius:8px;overflow:hidden;margin:auto;">
<tr><td style="background:#0096d6;padding:24px 40px;">
<span style="font-size:28px;font-weight:700;color:#fff;">hp</span>
<span style="font-size:13px;color:rgba(255,255,255,0.8);margin-left:12px;">Field Services</span>
</td></tr>
<tr><td style="padding:32px 40px;">
<h2 style="color:#1a1a1a;">Hi {first_name},</h2>
<p style="color:#555;">Your HP service visit has been completed successfully.</p>
<table width="100%" style="border:1px solid #e5e5e5;border-radius:6px;">
<tr><td style="background:#f8f8f8;padding:12px 20px;" colspan="2"><strong>Work Order Details</strong></td></tr>
<tr><td style="padding:12px 20px;color:#888;width:40%;">Work Order #</td><td style="padding:12px 20px;font-weight:600;">{work_order_number}</td></tr>
<tr><td style="padding:12px 20px;color:#888;">Technician</td><td style="padding:12px 20px;">{technician}</td></tr>
<tr><td style="padding:12px 20px;color:#888;">Completed</td><td style="padding:12px 20px;">{formatted_date}</td></tr>
<tr><td style="padding:12px 20px;color:#888;vertical-align:top;">Summary</td><td style="padding:12px 20px;">{summary or "Service completed successfully."}</td></tr>
</table>
<p style="color:#555;margin-top:24px;">Questions? Call <a href="tel:{Config.SUPPORT_PHONE}" style="color:#0096d6;">{Config.SUPPORT_PHONE}</a> or email <a href="mailto:{Config.SUPPORT_EMAIL}" style="color:#0096d6;">{Config.SUPPORT_EMAIL}</a></p>
</td></tr>
<tr><td style="background:#f8f8f8;padding:16px 40px;border-top:1px solid #e5e5e5;">
<p style="font-size:12px;color:#aaa;margin:0;">Automated notification from HP Field Services. Do not reply directly.<br>© {datetime.now().year} HP Inc.</p>
</td></tr>
</table></body></html>"""
    return subject, html_body
