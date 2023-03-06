import pdfkit
from flask import Flask ,send_file
app = Flask(__name__,template_folder ='template')
@app.route("/html_tab",methods=["POST","GET"])
def html_pdf():
    options = {
        'page-size': 'Letter',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm'
    }
    path_to_wkhtmltopdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
    import pdfkit #convert html to pdf v1
    

    path = path_to_wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=path)
    html_file ='C:\\Users\\mukeshkannan.d\\Desktop\\PDF\\index.html'
    pdf = 'C:\\Users\\mukeshkannan.d\\Desktop\\PDF\\output.pdf'

    pdfkit.from_url(html_file, pdf, configuration=config,options={"enable-local-file-access": "","page-size":'A4'})
    #      'page-size': 'A4',
    #      'margin-top': '0.25in',
    #      'margin-right': '0.25in',
    #      'margin-bottom': '0.25in',
    #      'margin-left': '0.25in',
    #      'encoding': "UTF-8",
    #      'custom-header' : [
    #         ('Accept-Encoding', 'gzip')
    #      ],
    #      'no-outline': None})

    return send_file(pdf,download_name='file.pdf')

if __name__ == '__main__':
	app.run(debug=True) 