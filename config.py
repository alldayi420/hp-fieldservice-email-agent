import os

class Config:
    CLIENT_ID = os.getenv("FS_CLIENT_ID", "YOUR_AZURE_APP_CLIENT_ID")
    CLIENT_SECRET = os.getenv("FS_CLIENT_SECRET", "YOUR_AZURE_APP_CLIENT_SECRET")
    TENANT_ID = os.getenv("FS_TENANT_ID", "YOUR_AZURE_TENANT_ID")
    DYNAMICS_ORG = os.getenv("FS_DYNAMICS_ORG", "YOUR_ORG_NAME")
    SENDER_EMAIL = os.getenv("FS_SENDER_EMAIL", "fieldservice@yourcompany.com")
    CHECK_INTERVAL_MINUTES = int(os.getenv("FS_CHECK_INTERVAL", "30"))
    SURVEY_URL = os.getenv("FS_SURVEY_URL", "")
    SUPPORT_PHONE = os.getenv("FS_SUPPORT_PHONE", "1-800-HP-SUPPORT")
    SUPPORT_EMAIL = os.getenv("FS_SUPPORT_EMAIL", "support@hp.com")
