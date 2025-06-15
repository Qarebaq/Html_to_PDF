import matplotlib
matplotlib.use('Agg')  # استفاده از backend بدون نیاز به رابط کاربری
import math
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template, request, send_file, jsonify,session
import pdfkit
import os
import base64

app = Flask(__name__)


# تابع برای تولید نمودار و ذخیره آن به عنوان تصویر
#   jahr = 67 - int(age) + int(year)
    
    # بررسی شرایط سنی و جنسیتی
#    if int(age) < 30 and gender == "male":
#        result = "43%"
##    elif 30 <= int(age) < 40 and gender == "male":
 #       result = "41%"
 #   elif 40 <= int(age) < 50 and gender == "male":
 #       result = "39%"
 #   elif gender == "male":
 #       result = "38%"
 #   elif int(age) < 30 and gender == "female":
 #       result = "38%"
 #   elif 30 <= int(age) < 40 and gender == "female":
 #       result = "37%"
 #   elif 40 <= int(age) < 50 and gender == "female":
 #       result = "35%"   
 #   elif gender == "female":
 #       result = "38%"

  #  resultOfSecondChart_12 = float(Versorgungsziel) * 1.015 ** (67 - int(age))
  #  vNetto = float(Versorgung) + float(Vorsorge) - float(steuern)
 #   valueOfTopChart = resultOfSecondChart_12 - vNetto
  #  input3_25 = float(Steuern_und_Sozialabgaben_bei_Berufsunfähigkeit)
  #  hNetto = float(hBrutto) - input3_25
  #  input1_26 = float(Einkunfte_aus_privater_Vorsorge)

    # داده‌های نمونه برای نمودار (این داده‌ها را با داده‌های واقعی خود جایگزین کنید)
   # labels = ['', '', '']
  #  values = [Versorgungsziel, resultOfSecondChart_12, vNetto]

  #  fig, ax = plt.subplots()
  #  ax.bar(labels, values)
   # ax.set_title('Stupid Chart')
# star_1 = 0
# star_2 = 0
# star_3 = 0
# star_4 = 0
# star_5 = 0
# star_6 =0
# star_7= 0
# star_8= 0

@app.route('/')
def home():
    return render_template('index.html')

#rating1 = "0"
#@app.route('/submit5-rating1', methods=['POST'])
#def submit5_rating1():
#    global rating1
#    data = request.get_json()
#    print(data)
#    rating1 = data
    
  #  return jsonify(success=True)




#rating1 = int(rating1)
#rating2 = int(rating2)
#rating3 = int(rating3)
#rating4 = int(rating4)
#rating5 = int(rating5)
#rating6 = int(rating6)
#rating7 = int(rating7)
#rating8 = int(rating8)
#setare1 = rating1


#@app.route('/star1_5', methods=['POST'])
#def star1():
 #   data = request.get_json()
  #  star_1 = int(data)
   # return jsonify(success=True)


#@app.route('/star2_5', methods=['POST'])
#def star2():
 #   data = request.get_json()
  #  star_2 = int(data)
   # return jsonify(success=True)


#@app.route('/star1_5', methods=['POST'])
#def star1():
 #   data = request.get_json()
  #  star_1 = int(data)
   # return jsonify(success=True)






# تعداد اونها رو به صورت ولیو بگیر
@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
   #سیستم ادبل ها که جمع بشن و اینا اینجان حواست باشه  

    name = request.form['name']
    gender = request.form['gender']
    age = request.form['age']
    # german20 = request.form['german20']
    # german21 = request.form['german21']
    # german22 = request.form['german22']




    year = request.form['year']

    # -- Page 25 ending


    #y = float(versorgungsziel) - float(versorgung)
    
    analysezum = request.form['analysezum']
    ansprechpartner = request.form['ansprechpartner']
    telefon = request.form['telefon']
#    if resultOfStars == 3:
#        star1 = "★"*int(resultOfStars)
#starter Page 8



    # تولید نمودار

    html_content = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{name}</title>
        <style>

        body {{
            font-family: Verdana,Tahoma ;
            margin: 20px;
            
        }}
        table {{
         display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            border-collapse: collapse;
        }}
        table, th, td {{
            border: 1px solid black;
        }}
             th {{
            border: none;
        }}
        th, td {{
            padding: 10px;
            text-align: left;
        }}
        .header{{
        color: #412973;
        text-align: left;
        }}
        .icon{{
            width:7%;
            float: left;
 

        }}
        .miniH{{
            margin-left:76px;
                margin-top:36px;
        }}
         td img {{
            width: 290px;


            height: auto;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
        }}
        .neveshteh {{
            background-color: #7863A6;
            display: flex;
       
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    border-bottom-left-radius: 8px;
    border-bottom-right-radius: 8px;


            align-items: center;
            text-align: center;
            }}
        .neveshteh p{{
        text-align: center;
        color: white;
         font-family: Verdana,Tahoma;
         
        }}
        .page5table {{
            border: none;
            border:white solid;
            text-align: center;

        
        }}
        .page5table td{{
                  border: none;
            border:white solid;
           

        }}






  .paga {{
        padding: 20px;
        border: none;
        text-align: center;
        max-width: fit-content;
        margin-left: auto;
        margin-right: auto;
    }}
    .paga td {{
        padding: 20px;
        border: none;
        text-align: center;
        white-space: nowrap;
        vertical-align: middle;

        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;


    }}
    .paga img {{
        width: 130px; 
        
    }}
    .numPage{{
    
        color:#412973;



    }}




        .rate {{
    float: left;
    height: 26px;
    padding: 0 10px;
        position: absolute;
}}
.rate:not(:checked) > input {{
    position:absolute;
    top:-9999px;
}}
.rate:not(:checked) > label {{
    float:right;
    width:1em;
    overflow:hidden;
    white-space:nowrap;
    cursor:pointer;
    font-size:30px;
    color:#ccc;
}}
.rate:not(:checked) > label:before {{
    content: '★ ';
}}
.rate > input:checked ~ label {{
    color: #ffc700;    
}}
.rate:not(:checked) > label:hover,
.rate:not(:checked) > label:hover ~ label {{
    color: #deb217;  
}}
.rate > input:checked + label:hover,
.rate > input:checked + label:hover ~ label,
.rate > input:checked ~ label:hover,
.rate > input:checked ~ label:hover ~ label,
.rate > label:hover ~ input:checked ~ label {{
    color: #c59b08;
}}
    .content {{
        page-break-before: always; 
    }}
footer{{

         flex-shrink: 0;
        padding: 10px 0;
            text-align: center;
            font-size: 12px;
            color: #777;
            margin-top: 40px;
}}
.chartimg1{{
            max-width: fit-content;
            margin-left: auto;
            margin-right: auto;
                        display: flex;
            justify-content: center;
}}
.chartimg2{{

    width:550px;
                        }}
.start{{
            color: #412973;
            text-align: center;
            font-size: 65px;
}}
.page8table td{{
    border: none;

}}
.page8table {{
    border: none;

}}
.page8table tr{{

      border-bottom: 1px solid #ddd; 
}}
.gogooli{{
color: gold;
font-size: 30px;
text-align: center;
}}
.page22t{{
    border: none;
}}

        .page-break {{
            page-break-before: always; 
        }}


        </style>
    </head>
    <body>
    <div class="content">
<br>
<br>
<br>

 



<h1 class="start"><strong>Mein persönlicher Finanzplan</strong></h1>
<br>
<br>
<br>
<br>
<br>


<table class="page5table">
    <tr>
        <td><strong>Für: </strong></td>
        <td><strong>{name}</strong></td>
    </tr>
    <br>
    <br>
    <br>

    <tr>
    <td>
        <strong>Analyse zum:</strong>
    </td>

    <td>
            <strong> {analysezum}</strong>
    </td>
    </tr>
        <br>
    <br>
    <br>


    <tr>
    <td>
       <strong> Ansprechpartner: </strong>
    </td>
    <td>
            <strong>{ansprechpartner}</strong>
    </td>
    </tr>
        <br>
    <br>
    <br>


    <tr>
        <td>
            <strong>Telefon</strong>
        </td>
        <td>
            <strong>{telefon}</strong>
       
        </td>
    </tr>
        <br>
    <br>


</table>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>






<div class="page-break"></div>











<div style="max-width: fit-content; margin-left: auto; margin-right: auto;">
    <table class="paga">
        <tr>
            <td><h3 class="numPage">Seite 2 von 10</h3></td>
            <td><h1 text-align="center" style="margin-left:73px;" class="header">Ihr Finanzplan - so individuell wie Sie</h1></td>
        </tr>
    </table>
</div>









        <hr style="border: none; height: 1px; background-color: #412973;">
        <h2 class="miniH">Ihre persönlichen Ziele</h2>
        <br>
        <p>
Ein altes Sprichwort sagt "Meistens bringt es mehr, einen halben Tag über die finanzielle Zukunft nachzudenken, als einen Monat dafür zu arbeiten." Dabei gilt: Je früher Sie die wichtigen Themen anpacken, desto besser. Ihre Ziele gestalten sich wie folgt.
</p>
<br>
    <table class="page5table">
        <tr>
            <td>

</div>

    </body>
    </html>
    """

    # ایجاد دایرکتوری PDF در صورت عدم وجود
    os.makedirs("pdf", exist_ok=True)
    pdf_path = f"/Users/amirsmac/Desktop/htmlToPDF42/pdf/{name}.pdf"
    options = {
        "enable-local-file-access": None
    }
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
    pdfkit.from_string(html_content, pdf_path, configuration=config, options=options)

    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
