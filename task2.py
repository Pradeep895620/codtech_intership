import pandas as pd
from fpdf import FPDF

# --- STEP 1: GENERATE SAMPLE DATA ---
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Projects_Completed': [12, 15, 7, 20, 11],
    'Efficiency_Score': [88, 92, 75, 98, 85]
}
df = pd.DataFrame(data)
# FIXED: Converted description to actual method
df.to_csv('internship_data.csv', index=False)

# --- STEP 2: READ AND ANALYZE DATA ---
raw_data = pd.read_csv('internship_data.csv')
# FIXED: Defined variables correctly
total_projects = raw_data['Projects_Completed'].sum()
avg_efficiency = raw_data['Efficiency_Score'].mean()
threshold = 80 # Added missing threshold variable
top_performer = raw_data.loc[raw_data['Efficiency_Score'].idxmax()]['Employee']

# --- STEP 3: GENERATE FORMATTED PDF ---
class Report(FPDF):
    def header(self):
        # FIXED: Corrected methods for color and rect
        self.set_fill_color(211, 211, 211) 
        self.rect(0, 0, 210, 40, 'F')
        self.set_font('Arial', 'B', 20)
        self.cell(0, 20, 'CODTECH INTERNSHIP REPORT', ln=True, align='C')
        # FIXED: Font size set to 10
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, 'Task 2: Automated Report Generation', ln=True, align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

# Initialize PDF
pdf = Report()
pdf.add_page()

# Adding Analysis Section
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, "1. Executive Summary", ln=True)
pdf.set_font('Arial', '', 12)
# FIXED: Corrected string formatting and added missing closing parenthesis
pdf.multi_cell(0, 10, f"Based on the analysis of 'internship_data.csv', the team has completed a total of {total_projects} projects. "
                     f"Fifty percent of labs fall below {threshold}% efficiency, with an average result of {avg_efficiency:.2f}%. "
                     f"The top-performing employee for this period is {top_performer}.")
pdf.ln(10)

# Data Table
pdf.set_font('Arial', 'B', 12)
pdf.cell(60, 10, "Employee Name", border=1)
pdf.cell(60, 10, "Projects Done", border=1)
pdf.cell(60, 10, "Efficiency %", border=1, ln=True)

pdf.set_font('Arial', '', 12)
for index, row in raw_data.iterrows():
    pdf.cell(60, 10, str(row['Employee']), border=1)
    pdf.cell(60, 10, str(row['Projects_Completed']), border=1)
    pdf.cell(60, 10, str(row['Efficiency_Score']), border=1, ln=True)

# Save the file
pdf.output("Automated_Report_Output.pdf")
print("Report ready. File saved as Automated_Report_Output.pdf")
