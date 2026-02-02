# 1. Configuration & Access
try:
    cust_list = _input.all("Customer Details")
    cust = cust_list[0].json if cust_list else {}
except:
    cust = {}

menu_items = _input.all("Proposed Menu")
services = _input.all("Other Services")
host_reqs = _input.all("Other Info")

# Logo URL
logo_url = "https://res.cloudinary.com/dwffrfajl/image/upload/v1770034621/Little_Jalebis_Logo_lmpaxo.svg"

# 2. HTML Construction
html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
  /* Import Google Fonts */
  @import url('https://fonts.googleapis.com/css2?family=Chilanka&family=Quicksand:wght@400;600;700&display=swap');

  @page {{
    margin: 15mm 15mm 15mm 15mm; /* Reduced margin as requested */
  }}
  
  body {{ 
    font-family: 'Quicksand', sans-serif; 
    color: #333; 
    line-height: 1.65;
    letter-spacing: 0.4px;
    margin: 0;
    background: white;
    padding-bottom: 30mm; /* reserve space for fixed footer to avoid content overlap */
  }} 

  /* FIXED FOOTER STYLING */
  .footer {{
    position: fixed;
    bottom: 0; /* sit at the bottom of page box; body reserves space so content won't overlap */
    left: 0;
    right: 0;
    text-align: center;
    font-size: 10px;
    color: #666;
    border-top: 1px solid #eee;
    padding-top: 8px;
    line-height: 1.4;
  }} 

  /* TABLE SPACER: Increased to reserve footer area and prevent overlap */
  .table-spacer {{
    height: 12mm;
    border: none !important;
  }}
  /* Prevent table rows and cells from breaking into footer area on PDF print */
  tr, td {{
    page-break-inside: avoid;
    break-inside: avoid;
    -webkit-column-break-inside: avoid;
  }}
  table {{
    page-break-inside: auto;
  }}

  @media print {{
    body {{ background: white; color: #333; }}
    h1, h2, h3 {{ color: #2D3E50 !important; }}
    .header-banner {{
      background: #2D3E50 !important;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}
    .footer {{
        position: fixed;
        bottom: 0;
    }}
    /* Force logo size for print to ensure PDF renders the larger logo */
    .main-logo {{ width: 200px !important; max-width: 200px !important; height: auto !important; }}
    .gallery-logo .main-logo {{ width: 200px !important; max-width: 200px !important; height: auto !important; }}
    tr {{ page-break-inside: avoid; }}
  }}

  h1, h2, h3 {{ 
    font-family: 'Chilanka', cursive; 
    color: #2D3E50; 
    margin-top: 15px;
  }}

  .logo-wrapper {{
    text-align: center;
    padding: 5px 0 15px 0;
  }}
  .main-logo {{
    max-width: 200px; /* increased 1.5x from 160px */
    height: auto;
  }}

  .full-page-section {{
    page-break-after: always;
    text-align: left;
    padding: 6mm 10mm;
  }}

  .full-page-section .main-logo {{
    max-width: 160px;
    height: auto;
  }}

  .intro-text {{
    font-size: 18px;
    text-align: left;
    margin: 0 auto;
    font-weight: 800;
    max-width: 100%;
    line-height: 2;
    letter-spacing: 1.8px;
    color: #333;
  }}

  .intro-text strong {{
    font-weight: 900;
    color: #F08C00;
  }}

  .intro-signoff {{
    margin-top: 12px;
    font-weight: 900;
    text-align: left;
  }}

  .header-banner {{ 
    background: #2D3E50; 
    color: white;
    padding: 15px 20px;
    border-radius: 8px;
    margin-bottom: 10px;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  .header-banner h1 {{ margin: 0; font-size: 24px; text-align: center; color: white !important; }}
  
  .header-details {{ 
    margin-top: 10px; 
    display: table;
    width: 100%;
    font-size: 13px; 
    border-top: 1px solid rgba(255,255,255,0.3);
    padding-top: 8px;
  }}

  .header-detail-row {{ display: table-row; }}
  .header-detail-row div {{
    display: table-cell;
    width: 50%;
    padding: 3px 0;
    color: white;
  }}
  
  h2 {{ border-bottom: 2px solid #2D3E50; padding-bottom: 3px; font-size: 18px; text-transform: uppercase; }}
  
  .data-table {{ 
    width: 100%; 
    border-collapse: collapse; 
    margin-top: 10px; 
    table-layout: fixed;
  }}
  
  .data-table th {{ background: #f8f9fa; padding: 8px; text-align: left; border: 1px solid #999; font-size: 12px; }}
  .data-table td {{ padding: 8px; border: 1px solid #ccc; vertical-align: top; font-size: 13px; word-wrap: break-word; }}
  
  .col-right {{ text-align: right; }}
  .total-row {{ font-weight: bold; background-color: #f8f9fa; color: #2D3E50; }}
  .description {{ font-size: 11px; color: #666; font-style: italic; display: block; }}
  .badge {{ font-size: 9px; padding: 2px 6px; border-radius: 3px; background: #D3D3D3; color: #333; font-weight: bold; display: inline-block; margin-left: 8px; border: 1px solid #CCCCCC; white-space: nowrap; }}
  .badge:empty {{ display: none; }}

  /* Gallery page styling */
  .gallery-section {{
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    /* Use explicit height for A4 printable area but reserve space for logo so content centers within remaining area */
    height: calc(297mm - 30mm - 30mm); /* subtract ~30mm for logo area */
    box-sizing: border-box;
    padding: 5mm 0;
    text-align: center;
  }}
  .gallery-logo .main-logo {{ max-width: 200px; height:auto; }}
  .gallery-content {{
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    width:100%;
  }}
  .gallery-heading {{
    font-size: 20px;
    color: #2D3E50;
    font-weight:700;
    margin: 10px 0 6px;
    text-align:center;
    letter-spacing: 1.6px;
    /* Remove default H2 underline for gallery heading */
    border-bottom: none !important;
    padding-bottom: 0 !important;
    text-decoration: none !important;
  }}
  .gallery-tagline {{
    font-size: 20px;
    color: #2D3E50;
    font-weight:600;
    margin-top: 12px;
    text-align:center;
    letter-spacing: 1px;
  }}
  .gallery-hr {{ border:0; border-top:2px solid #2D3E50; width:60%; margin: 8px auto 14px; }}
  .photo-grid td {{ padding:6px; vertical-align: top; }}
  .gallery-img {{ width:100%; height:150px; object-fit: cover; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); display:block; }}
  .data-table th {{ background: #f8f9fa; padding: 8px; text-align: left; border: 1px solid #999; font-size: 12px; line-height: 1.6; letter-spacing: 0.3px; }}
  .data-table td {{ padding: 8px; border: 1px solid #ccc; vertical-align: top; font-size: 13px; word-wrap: break-word; line-height: 1.6; letter-spacing: 0.3px; }}

  /* Page break header - repeats on every page */
  .print-header {{
    display: table-header-group;
  }}

  .page-container {{
    width: 100%;
    border-collapse: collapse;
  }}

</style>
</head>
<body>

<div class="footer">
    <strong>Little Jalebis - Kids Party House & Catering Co.</strong><br>
    (Unit of NC Hospitality Pvt Ltd) CIN : U55101DL2009PTC188581<br>
    Regd. Address : E 5 Kalindi Colony, Near New Friends Colony, New Delhi 110065<br>
    Party Venue : 17, Arjun Marg, DLF Phase-1, Gurgaon 122002<br>
    Website : www.littlejalebis.com Email : sales@littlejalebis.com
</div>

<div class="full-page-section">
  <div class="logo-wrapper">
    <img src="{logo_url}" class="main-logo" alt="Little Jalebis Logo">
  </div>
  <div class="intro-text">
    <p><strong>Welcome to Little Jalebis – Kids Party House & Catering Co.</strong></p>
    <p>Thank you for considering <strong>Little Jalebis</strong> for your child's celebration.</p>
    <p>This quote outlines our <strong>food and catering offerings</strong>, thoughtfully curated for kids' parties and family gatherings — whether hosted at your home, a venue of your choice, or at our kids' party house in DLF Phase 1, Gurgaon.</p>
    <p>At <strong>Little Jalebis</strong>, food is at the heart of every celebration. Our menus are designed keeping children in mind — kid-friendly, hygienic, and flavour-balanced — while being equally enjoyed by adults. With over <strong>40 years of hospitality expertise</strong>, we focus on consistent quality, generous portions, and smooth service, so hosting stays simple and stress-free for parents.</p>
    <p>All menus can be <strong>customised</strong> based on the age of the children, duration of the event, and your preferences. If you have any specific ideas or requests, we're always happy to tailor the food accordingly.</p>
    <p>We look forward to being a part of your celebration and creating a delightful food experience that both children and adults enjoy.</p>
    <div style="margin-top: 24px;">
      <p class="intro-signoff"><strong>Warm regards,<br>
      Team Little Jalebis<br>
      +91 8130964374</strong></p>
    </div>
  </div>
</div>

"""  # 2.5 PHOTO GALLERY (PAGE 2)
images = cust.get('ImageGrid') or []
# Handle serialized JSON strings (if passed as string)
try:
    if isinstance(images, str) and images.strip():
        import json as _json
        images = _json.loads(images)
except Exception:
    # leave as-is
    pass

# Normalize to list of urls
_image_urls = []
for it in (images or []):
    if isinstance(it, dict):
        url = it.get('url') or it.get('secure_url') or it.get('secureUrl') or it.get('src')
    else:
        url = str(it)
    if url: _image_urls.append(url)

if _image_urls:
    # keep up to 9 images and pad with empty strings
    _image_urls = _image_urls[:9]
    while len(_image_urls) < 9:
        _image_urls.append('')

    html += f"""
        <div style="page-break-before: always;">
          <div class="logo-wrapper">
            <img src="{logo_url}" class="main-logo" alt="Little Jalebis Logo">
          </div>
          <div class="gallery-section">
            <div class="gallery-content">
              <h2 class="gallery-heading">PHOTO GALLERY</h2>
              <hr class="gallery-hr" />
              <table class="photo-grid" style="width:820px; margin: 0 auto; border-collapse: collapse; table-layout: fixed;">
                <tbody>
    """
    for r in range(3):
        html += "        <tr>"
        for c in range(3):
            idx = r*3 + c
            url = _image_urls[idx]
            if url:
                html += f"<td style='width:33%; padding:4px;'><img src=\"{url}\" class=\"gallery-img\" alt=\"gallery image {idx}\"></td>"
            else:
                html += "<td style='width:33%; padding:4px;'></td>"
        html += "</tr>"
    html += """
                </tbody>
              </table>
              <div class="gallery-tagline">INDIA'S FIRST KIDS-CENTRIC CATERING COMPANY</div>
            </div>
          </div>
        </div>
    """

html += f"""
<table class="page-container">
  <thead class="print-header">
    <tr>
      <td>
        <div class="logo-wrapper">
          <img src="{logo_url}" class="main-logo" alt="Little Jalebis Logo">
        </div>
      </td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <div class="header-banner">
          <h1>EVENT QUOTATION</h1>
          <div class="header-details">
            <div class="header-detail-row">
              <div><strong>HOST:</strong> {cust.get('Host Name', 'N/A')}</div>
              <div><strong>MOBILE:</strong> {cust.get('Mobile No', 'N/A')}</div>
            </div>
            <div class="header-detail-row">
              <div><strong>DATE:</strong> {cust.get('Event Date', 'N/A')}</div>
              <div><strong>TIME:</strong> {cust.get('Time', 'N/A')}</div>
            </div>
            <div class="header-detail-row">
              <div><strong>LOCATION:</strong> {cust.get('Location', 'N/A')}</div>
              <div><strong>PAX:</strong> {cust.get('Pax', 'N/A')}</div>
            </div>
          </div>
        </div>

        <h2>PROPOSED MENU</h2>
"""

# 3. Process Menu Items
from collections import OrderedDict
categories = OrderedDict()
for item in menu_items:
    d = item.json
    if not d.get('Name') or str(d.get('Name')).strip() == "": continue
    cat = d.get('Category','Other')
    categories.setdefault(cat, []).append(d)

for cat, items in categories.items():
    is_live_station = "live station" in cat.lower()
    
    if is_live_station:
        colgroup = '<col style="width:50%" /><col style="width:12.5%" /><col style="width:12.5%" /><col style="width:12.5%" /><col style="width:12.5%" />'
        header_row = f"""
            <tr>
              <th style="background: #F6B27A; color: #2D3E50;">{cat.upper()}</th>
              <th style="text-align: center; background: #F6B27A; color: #2D3E50;">SETUP</th>
              <th style="text-align: center; background: #F6B27A; color: #2D3E50;">NO. OF PEOPLE</th>
              <th style="text-align: center; background: #F6B27A; color: #2D3E50;">RATE PER PERSON</th>
              <th style="text-align: center; background: #F6B27A; color: #2D3E50;">AMOUNT</th>
            </tr>"""
    else:
        colgroup = '<col style="width:55%" /><col style="width:10%" /><col style="width:10%" /><col style="width:12.5%" /><col style="width:12.5%" />'
        header_row = f"""
            <tr>
              <th style="background: #F6B27A; color: #2D3E50;">{cat.upper()}</th>
              <th style="text-align: center; background: #F6B27A; color: #2D3E50;">PORTION</th>
              <th style="text-align: center; background: #F6B27A; color: #2D3E50;">RATE</th>
              <th style="text-align: center; background: #F6B27A; color: #2D3E50;">AMOUNT</th>
              <th style="text-align: center; background: #F6B27A; color: #2D3E50;">PCS</th>
            </tr>"""
    
    html += f"""
        <table class="data-table" style="margin-top: 15px;">
          <tfoot><tr><td colspan="5" class="table-spacer"></td></tr></tfoot>
          <colgroup>
            {colgroup}
          </colgroup>
          <thead>
            {header_row}
          </thead>
          <tbody>
    """
    for d in items:
        rate_raw = d.get('Rate','')
        try:
            r_str = str(rate_raw).replace(',','').strip()
            r_val = float(r_str)
            rate_display = f"₹{int(r_val):,}" if r_val.is_integer() else f"₹{r_val:,.2f}"
        except:
            rate_display = rate_raw
        
        amount_raw = d.get('Amount','')
        try:
            a_str = str(amount_raw).replace(',','').strip()
            a_val = float(a_str)
            amount_display = f"₹{int(a_val):,}" if a_val == int(a_val) else f"₹{a_val:,.2f}"
        except:
            amount_display = amount_raw if amount_raw else ""

        if is_live_station:
            setup_raw = d.get('Setup','')
            try:
                s_str = str(setup_raw).replace(',','').strip()
                s_val = float(s_str)
                setup_display = f"₹{int(s_val):,}" if s_val.is_integer() else f"₹{s_val:,.2f}"
            except:
                setup_display = setup_raw
            no_of_people_raw = d.get('NoOfPeople','')
            no_of_people = 'NA' if not no_of_people_raw or str(no_of_people_raw).strip() == '0' or str(no_of_people_raw).strip() == '' else no_of_people_raw
            rate_display_final = 'NA' if not rate_raw or str(rate_raw).strip() == '0' or str(rate_raw).strip() == '' else rate_display
            html += f"""
            <tr>
              <td>
                <strong>{d.get('Name','')}</strong><span class='badge'>{d.get('Veg/Non Veg','').strip()}</span>
                <span class='description'>{d.get('Description','')}</span>
              </td>
              <td style="text-align: center;">{setup_display}</td>
              <td style="text-align: center;">{no_of_people}</td>
              <td style="text-align: center;">{rate_display_final}</td>
              <td style="text-align: center;">{amount_display}</td>
            </tr>"""
        else:
            portions = d.get('Portion','') if d.get('Portion','') not in (0,'0','') else ''
            html += f"""
            <tr>
              <td>
                <strong>{d.get('Name','')}</strong><span class='badge'>{d.get('Veg/Non Veg','').strip()}</span>
                <span class='description'>{d.get('Description','')}</span>
              </td>
              <td style="text-align: center;">{portions}</td>
              <td style="text-align: center;">{rate_display}</td>
              <td style="text-align: center;">{amount_display}</td>
              <td style="text-align: center;">{d.get('PcsDisplay') or d.get('Pcs','')} {d.get('Unit','')}</td>
            </tr>"""
    html += "</tbody></table>"

# 4. Other Services & Summary (PAGE 3)
html += f"""
        <div style="page-break-before: always;"></div>
        <div style="margin-top: 15px;">
          <h2>OTHER SERVICES & SUMMARY</h2>
          <table class='data-table'>
            <tfoot><tr><td colspan="5" class="table-spacer"></td></tr></tfoot>
            <tbody>
"""

for s in services:
    sd = s.json
    service_name = sd.get('Other Services', '')
    if not service_name or str(service_name).strip() == "": continue
    amount = sd.get('Amount', '')
    try:
        amt_str = str(amount).replace(',','').strip()
        amt_val = float(amt_str)
        amount_display = f"₹{int(amt_val):,}" if amt_val.is_integer() else f"₹{amt_val:,.2f}"
    except:
        amount_display = amount

    is_total = any(x in str(service_name).upper() for x in ["TOTAL", "SUBTOTAL", "GST"])
    row_class = "class='total-row'" if is_total else ""
    html += f"<tr {row_class}><td colspan='4'>{service_name}</td><td class='col-right'>{amount_display}</td></tr>"

html += "</tbody></table></div>" 

# 5. Host Requirements
if host_reqs:
    html += """
    <div style="page-break-inside: avoid; margin-top: 25px;">
        <h2>TO BE PROVIDED BY HOST</h2>
        <ul style="font-size: 13px;">"""
    for h in host_reqs:
        req = h.json.get('TO BE PROVIDED BY HOST')
        qty_req = h.json.get('QUANTITY', '')
        if req and str(req).strip() != "": 
            html += f"<li style='margin-bottom: 4px;'><strong>{req}</strong>: {qty_req}</li>"
    html += "</ul></div>"

html += "</td></tr></tbody></table>"

# Link to master menu (PDF-Compatible Horizontal Layout)
html += """
    <div style="margin: 20px 0; text-align: center; page-break-inside: avoid;">
      <div style="display: inline-block; background-color: #F6B27A; padding: 10px 20px; border-radius: 8px; width: 85%;">
        <span style="font-weight: 900; color: #2D3E50; font-size: 16px; text-transform: uppercase; vertical-align: middle;">
            Visit Master Menu
        </span>
        <br/>
        <a href="https://littlejalebis.com/master-menu.html" style="color: #2D3E50; text-decoration: none; font-weight: 900; font-size: 16px; margin-left: 8px; vertical-align: middle;">
            🍫 www.littlejalebis.com/master-menu 🍫
        </a>
      </div>
    </div>
"""

# 6. Final Page (PAGE 4)
html += f"""
    <div class="last-page" style="page-break-before: always; padding-top: 15px;">
      <div class="logo-wrapper">
        <img src="{logo_url}" class="main-logo" alt="Little Jalebis Logo">
      </div>
      <h3 style="text-decoration: underline; margin-bottom: 15px; margin-top: 15px;">Please Note :</h3>
      <ul class="note-list" style="list-style-type: disc; padding-left: 20px; font-size: 14px;">
        <li style="margin-bottom: 10px;"><strong>No Minimum Guarantee:</strong> We do not require any minimum guarantee of people. However, our minimum order value for catering is ₹ 20,000 + GST.</li>
        <li style="margin-bottom: 10px;"><strong>Portion Size:</strong> 1 portion of a main course dish serves 3–4 adults or 4–5 kids.</li>
        <li style="margin-bottom: 10px;"><strong>Event Duration:</strong> Service duration is 4 hours from the guest invite time.</li>
        <li style="margin-bottom: 10px;"><strong>Kitchen Access:</strong> If kitchen access is not available, an additional charge of ₹3,000 will apply for stove, cylinder, and other equipment.</li>
        <li style="margin-bottom: 10px;"><strong>Menu Finalization:</strong> To ensure a flawless experience, please confirm the menu 4–5 days prior to the event. No changes can be accommodated after this.</li>
        <li style="margin-bottom: 10px;"><strong>Nanny Boxes:</strong> Available on request. Please connect with us for details.</li>
        <li style="margin-bottom: 10px;"><strong>Guest Count Updates:</strong> Kindly inform us of any increase in guest count at least 4–5 days prior.</li>
        <li style="margin-bottom: 10px;"><strong>Booking Policy:</strong> All bookings are subject to availability at the time of confirmation and require a non-refundable 50% advance payment.</li>
        <li style="margin-bottom: 10px;"><strong>Add-On Services:</strong> Options such as sanitised toys and theme-aligned play areas can be arranged on request by our sister company. Please connect with us for details.</li>
      </ul>

      <div style="text-align: center; margin-top: 110px;">
          <p style="font-weight: bold; color: #D4813E; font-size: 16px; letter-spacing: 1px;">FOLLOW US @LITTLEJALEBIS</p>
          <!-- Instagram QR code added below the icon -->
          <div style="margin-top: 10px;">
            <img src="https://res.cloudinary.com/dwffrfajl/image/upload/v1768128519/qr_xvsuyp.png" alt="Instagram QR code" style="height: 200px; display: inline-block;">
          </div>
      </div>
    </div>
  </body>
</html>
"""

return [{"html_content": html}]