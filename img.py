from weasyprint import HTML

# Set the path to your HTML file
html_file = 'path/to/your/file.html'

# Set the path to the output PDF file
pdf_file = 'path/to/your/output.pdf'

# Set the PDF options, such as page size and margins
pdf_options = {
    'page-size': 'A4',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm'
    }

# Convert the HTML file to a PDF file using WeasyPrint
HTML(html_file).write_pdf(pdf_file, stylesheets=['path/to/your/bootstrap.css'], pdf_version='1.7', **pdf_options)
