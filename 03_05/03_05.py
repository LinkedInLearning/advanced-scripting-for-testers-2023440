import matplotlib.pyplot as plt
from fpdf import FPDF

test_results = [
    {"test": "Login Test", "status": "Pass"},
    {"test": "Signup Test", "status": "Fail"},
    {"test": "Checkout Test", "status": "Pass"},
    {"test": "Reset Password", "status": "Pass"},
    {"test": "Search Products", "status": "Fail"},
]

pdf = FPDF()
pdf.add_page()

pdf.set_font("Helvetica", style="B", size=16)

pdf.cell(0, None, "Test Report")

pdf.ln(10)
pdf.set_font(size=12)
pass_counts = 3
fail_counts = 2

labels = ["Pass", "Fail"]
values = [pass_counts, fail_counts]
colors = ["green", "red"]
img_name = "chart.png"

plt.bar(labels, values, color=colors)
plt.title("Test Result Summary")
plt.savefig(img_name)
plt.close()
pdf.image(img_name, x=10, y=None, w=100)
pdf.ln(10)

pdf.set_fill_color(230, 230, 230)
pdf.set_font(style="B")
pdf.cell(60, None, "Test Name", border=1, fill=True)
pdf.cell(60, None, "Status", border=1, fill=True)
pdf.ln()

pdf.set_font(style="")
for result in test_results:
    pdf.cell(60, None, result["test"], border=1)
    pdf.cell(60, None, result["status"], border=1)
    if result["status"] == "Fail":
        pdf.set_text_color(255, 0, 0)
    else:
        pdf.set_text_color(0, 128, 0)
    pdf.set_text_color(0, 0, 0)
    pdf.ln()

pdf.output("test_report.pdf")
