from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 16)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

def main():
    name = input("Name: ")
    create_shirtificate(name)

def create_shirtificate(name):
    pdf = PDF()
    pdf.add_page()
    pdf.image("./shirtificate.png", x=10, y=80, w=190)  # Adjust position and size as needed
    pdf.set_y(150)  # Adjust vertical position for name text
    pdf.set_font("Arial", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, name, 0, 1, "C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
