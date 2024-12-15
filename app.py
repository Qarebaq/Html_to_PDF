from flask import Flask, render_template, request, send_file
import pdfkit
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    product_names = request.form.getlist('product_name[]')
    product_essentials = request.form.getlist('Wesentliche[]')
    product_Recommendations = request.form.getlist('Empfehlung[]')
    product_Contributions = request.form.getlist('Beitrag[]')
    product_interests = request.form.getlist('Rente[]')
    name = request.form['name']
    gender = request.form['gender']
    age = request.form['age']
    year = request.form['year']
    german1=request.form['german1']
    german2=request.form['german2']
    german3=request.form['german3']
    german4=request.form['german4']
    german5=request.form['german5']
    german6=request.form['german6']
    german7=request.form['german7']
    german8=request.form['german8']
    

    product_rows = ""
    for product_names, product_essentials, product_Recommendations,product_Contributions,product_interests in zip(product_names, product_essentials, product_Recommendations,product_Contributions,product_interests):
        product_rows += f"""
        <tr>
            <td>{product_names}</td>      
            <td>{product_Recommendations}</td>
            <td>{product_essentials}</td>
            <td>{product_Contributions}€</td>
            <td>{product_interests}€</td>


        </tr>
        """

    html_content = f"""
    <html>
    <head>
    <meta charset="UTF-8"><title>{name}</title>
    <style>
    body {{
        font-family: Arial, sans-serif;
        margin: 20px;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
    }}
    table, th, td {{
        border: 1px solid black;
    }}
    th, td {{
        padding: 10px;
        text-align: left;
    }}
    </style>
    </head>
    <body>
        <h1>Information for {name}</h1>
        <p>Gender: {gender}</p>
        <p>Age: {age}</p>
        <p>Year: {year}</p>
        <p>{german1}</p>
        <p>{german2}</p>
        <p>{german3}</p>
        <p>{german4}</p>
        <p>{german5}</p>
        <p>{german6}</p>
        <p>{german7}</p>
        <p>{german8}</p>
        <p>{test}</p>

        <h2>Products</h2>
        <table>
            <thead>
                <tr>
                    <th>Produkt(Unternehmen)</th>
                    <th>Empfehlung</th>
                    <th>Wesentliche Leistungsmerkmale</th>
                    <th>mtl.Beitrag</th>
                    <th>BU-Rente</th>
                </tr>
            </thead>
            <tbody>
                {product_rows}
            </tbody>
        </table>
    </body>
    </html>
    """

    os.makedirs("pdf", exist_ok=True)
    pdf_path = f"pdf/{name}.pdf"

    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
    pdfkit.from_string(html_content, pdf_path, configuration=config)

    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
