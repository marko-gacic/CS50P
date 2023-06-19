from fpdf import FPDF

def generate_certificate():
    name = get_name()
    pdf = create_pdf()
    add_header(pdf)
    add_text(pdf, name)
    save_pdf(pdf)

def get_name():
    return input('Name: ').title()

def create_pdf():
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image('shirtificate.png', 8, 50, 190)
    return pdf

def add_header(pdf):
    pdf.set_font('Helvetica', 'B', size=40)
    pdf.text(50, 30, txt='CS50 Shirtificate')

def add_text(pdf, name):
    pdf.set_font('Helvetica', 'B', size=20)
    pdf.set_text_color(255)
    pdf.cell(190, 200, txt=f'{name} took CS50', align='C')

def save_pdf(pdf):
    pdf.output('shirtificate.pdf')

if __name__ == '__main__':
    generate_certificate()
