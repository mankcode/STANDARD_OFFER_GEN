from datetime import timedelta, datetime as d
import modules as m


id_object = m.Query(
    input("Wpisz nazwę kontaktu, dla którego chcesz stworzyć ofertę: "))
id_result = id_object.db(id_object.get_id_by_name)

company_name = m.Query(id_result)
company_name_result = company_name.db(company_name.get_company_name_by_id)

name = m.Query(id_result)
name_result = name.db(name.get_name_by_id)

tel = m.Query(id_result)
tel_result = tel.db(tel.get_tell_by_id)

zapytanie = m.Query(id_result)
tresc_zapytania = zapytanie.db(zapytanie.get_tresc_zapytania_by_id)


# Dane wejściowe do arkusza
id = id_result
date = d.now().strftime("%d-%m-%Y")
expiration = (d.now() + timedelta(days=7)).strftime("%d-%m-%Y")
company = company_name_result
name = name_result
tel = tel_result
product_number = str(input("Wpisz kod stołu: ")).lower()
product_name = ''
img_link = m.get_img_link(product_number)
top_size = m.get_top_size(product_number)

# lista wyposażenia dodatkowego przyporządkowana do stołu
item = m.get_accesories(product_number)
containers = m.add_container(item)

# podsumowanie oferty
table_price = m.count_total(item)
quantity = int(input("Wpisz ilość stołów: "))
discount = m.discount(quantity)
price_after_discount = m.dis_price(table_price, discount)
delivery_terms = ''
total_cost = str(float(price_after_discount * quantity))[0:8]
deadline = str(input("Wpisz termin realizacji: "))


f = open(f'{id}.html', 'w', encoding="utf-8")

html_template = f"""<!DOCTYPE html>
<html lang="pl">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Oferta {id}</title>
  </head>
  <body>
      <header>
        <img class="logo" src="grafiki/logo.png" />
        <span class="danera">
          <h1 class="ra">RA Construction Rafał Rozbicki</h1>
          <h2 class="ra">Wólka Kokosia 25, 05-307 Dobre</h2>
          <h2 class="ra">biuro@raconstruction.pl</h2>
          <h2 class="ra">Tel: 692 413 488</h2>        

      </header>
      <main>
          <section class="page_1">
            <span class="dane_ko">
                <p class="numer_oferty">
                    Numer oferty: {id}<br>
                    Data wystawienia: {date}<br>
                    Data ważności: {expiration}<br>
                </p>
                <p class="dane_firmy">
                    Oferta przygotowana dla: <br>                   
                    {company}<br>
                    {name} <br>
                    {tel} <br>
                </p>
            </span>
            <span class="nazwa_kod">
                <p>
                    <strong>{product_name}</strong><br>
                    <strong>Kod produktu:</strong> {product_number} <br>
                </p>
            </span>
            <div style="height: 50px;"></div>  
            <div>
                <img class="wizka_stolu" src="{img_link}" alt="stół do pakowania">
            </div>
            <div style="height: 130px;"></div>
      
          </section>

          <section class="page_2">
            <span class="blat">
                <p><b>Blat stołu - wymiary, materiały i wytrzymałość </b></p>
            </span>
            <span class="charakterystyka_blatu">
                <p style="text-align:center">Blat stołu oraz półki naszych stołów wykonujemy z płyty wiórowej o grubości 18 lub 25 mm. <br>
                Obrzeża płyty oklejamy okleiną ABS o grubości 2mm.</p>
            </span>
            <div >
                <img class="wymiar_blatu" src="{top_size}" alt="blat 120x70cm">             
                
            </div>
            <div style="height: 50px;"></div>        
          
            
            <div class="polki">
                <img style="height: 350px" src="grafiki/blat 18.jpg" alt="blat 18mm">
                <img style="height: 350px;" src="grafiki/blat 25.jpg" alt="blat 25mm">
            </div>
            <div style="height: 200px;"></div>           
                   
          </section>
          <section class="page_3">
            <span style="padding: 1px;">
                <p class="profile_konstrukcyjne"><b style="font-size: 26px">Profile konstrukcyjne,</b> <br>
                    których używamy do produkcji naszych stołów</p>
            </span>
            
            <div class="profile">
                <img class="profil" src="grafiki/profile/40 x 40.jpg" alt="30x18mm">
                <img class="profil" src="grafiki/profile/30 x 30 x 2.jpg" alt="30x30mm">
                <img class="profil" src="grafiki/profile/40 x 20 x 2.jpg" alt="40x20mm">
            </div>
            
            <div class="profile">
                <img class="profil" src="grafiki/profile/40 x 30 x 2.jpg" alt="40x30">
                
            </div>
            <span>
                <p class="profile_konstrukcyjne"><b style="font-size: 26px">Kolorystyka</b> 
                    </p>
            </span>
            <div class="profile">
                <img src="grafiki/kolorystyka/ral 7001.jpg" alt="ral7001">
                <img src="grafiki/kolorystyka/ral 7035.jpg" alt="ral7035">
            </div>
            <span class="profile">
                <p style="margin-left:-30px;"><b>Konstrukcja stalowa</b></p>
                <p><b>Blat stołu</b></p>
            </span>
            <div style="height: 50px;"></div>

          </section>
          <section class="page_4">
            <span style="padding: 1px;">
                <p class="profile_konstrukcyjne"><b style="font-size: 26px">Zestawienie elementów</b> </p>
            </span>
    
            {containers[0]}
            {containers[1]}
            {containers[2]}
            {containers[3]}
            {containers[4]}
            <div style="height: 50px;"></div>  
            {containers[5]}
            {containers[6]}
            {containers[7]}    
            {containers[8]}    
            {containers[9]}    
            {containers[10]}    
            {containers[11]}               

          
          
          <section class="page_6">
            <span style="padding: 1px;">
                <p class="profile_konstrukcyjne"><b style="font-size: 26px">Podsumowanie oferty</b> </p>
            </span>
            <span class="podsumowanie">
                <p style="margin-left: 30px;">Cena stołu: {table_price} PLN netto/szt.<br>
                    Ilość: {quantity} szt.<br>
                    Rabat: {discount} %<br>
                    Cena stołu po rabacie: {price_after_discount} PLN netto/szt.<br>
                    Forma dostawy: {delivery_terms}<br>
                    Łączny koszt zamówienia: {total_cost[:6]} PLN netto<br>
                    Termin realizacji: {deadline}<br>

                    Treść zapytania: {tresc_zapytania} <br>    
                </p>
            </span>
            <div style="height: 100px;"></div>            
          </section>
      </main>     
  </body>
</html>

"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()
