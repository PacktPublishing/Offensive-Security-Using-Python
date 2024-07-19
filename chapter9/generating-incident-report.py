from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report():
    c = canvas.Canvas("incident_report.pdf",
    pagesize=letter)
    c.drawString(100, 750, "Incident Report")
    c.drawString(100, 730, "Threat Detected: Yes")
    c.drawString(100, 710, "Response Actions Taken:")
    c.drawString(120, 690, "1. System Isolated")
    c.drawString(120, 670, "2. Threat Eradicated")
    c.drawString(120, 650, "3. Systems Recovered")
    c.save()

# Generate the report
generate_report()