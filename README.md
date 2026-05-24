# HP Field Service — Automated Follow-Up Email Agent
Automatically emails customers when a work order is Completed in Dynamics 365 Field Service Mobile.

## Quick Start
pip install -r requirements.txt
python test_agent.py --preview-only
python agent.py

## Files
- agent.py — Main agent
- config.py — Your credentials
- email_composer.py — HTML email builder
- test_agent.py — Test with fake data
