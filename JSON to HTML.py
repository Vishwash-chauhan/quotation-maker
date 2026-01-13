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
logo_url = "https://littlejalebis.com/wp-content/uploads/2025/04/LJ_Logo_M-2.svg"

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
  }} 

  /* FIXED FOOTER STYLING */
  .footer {{
    position: fixed;
    bottom: -10mm; /* Adjusted to sit tightly at the bottom within 15mm margin */
    left: 0;
    right: 0;
    text-align: center;
    font-size: 10px;
    color: #666;
    border-top: 1px solid #eee;
    padding-top: 8px;
    line-height: 1.4;
  }}

  /* TABLE SPACER: Reduced to 10mm to minimize gap between table and footer */
  .table-spacer {{
    height: 10mm;
    border: none !important;
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
    max-width: 160px;
    height: auto;
  }}

  .full-page-section {{
    page-break-after: always;
    text-align: center;
    padding: 5mm;
  }}

  .intro-text {{
    font-size: 23px;
    text-align: left;
    margin: 0 auto;
    font-weight: 800;
    max-width: 90%;
    line-height: 2.5;
    letter-spacing: 1.2px;
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
  .gallery-logo .main-logo {{ max-width: 160px; height:auto; }}
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

</style>
</head>
<body>

<div class="footer">
    <strong>Little Jalebis – Kids Catering & Delivery Co. (Unit of NC Hospitality Pvt Ltd)</strong><br>
    CIN : U55101DL2009PTC188581 | E 5 Kalindi Colony, New Delhi 110065<br>
    Website : www.littlejalebis.com | Email : sales@littlejalebis.com
</div>

<div class="full-page-section">
  <div class="logo-wrapper">
    <img src="{logo_url}" class="main-logo" alt="Little Jalebis Logo">
  </div>
  <div class="intro-text">
    <p>Hello from Little Jalebis - Kids Catering & Delivery Co., India's first catering company designed exclusively for kids, serving all of Delhi NCR.</p>
    <p>With over 40 years of hospitality expertise, we're here to make your celebration stress-free and memorable, whether it's a cozy gathering of 10 kids or a lively bash with 200 guests!</p>
    <p>Our specially curated menu is ready for you to explore.</p>
    <p>Looking forward to helping make your little one's celebration extra special!</p>
    <div style="margin-top: 40px;">
      <p>Warm Regards,<br>
      Team Little Jalebis<br>
      +91 8130964374</p>
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
<table class="page-container" style="width: 100%;">
  <tfoot><tr><td class="table-spacer"></td></tr></tfoot>
  <tbody>
    <tr>
      <td>
        <div class="logo-wrapper">
          <img src="{logo_url}" class="main-logo" alt="Little Jalebis Logo">
        </div>

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
    html += f"""
        <table class="data-table" style="margin-top: 15px;">
          <tfoot><tr><td colspan="5" class="table-spacer"></td></tr></tfoot>
          <colgroup>
            <col style="width:55%" /><col style="width:10%" /><col style="width:10%" /><col style="width:12.5%" /><col style="width:12.5%" />
          </colgroup>
          <thead>
            <tr>
              <th style="background: #F6B27A; color: #2D3E50;">{cat.upper()}</th>
              <th style="text-align: center; background: #F6B27A; color: #2D3E50;">PCS</th>
              <th style="text-align: center; background: #F6B27A; color: #2D3E50;">PORTION</th>
              <th style="text-align: center; background: #F6B27A; color: #2D3E50;">RATE</th>
              <th style="text-align: center; background: #F6B27A; color: #2D3E50;">AMOUNT</th>
            </tr>
          </thead>
          <tbody>
    """
    for d in items:
        portions = d.get('Portion','') if d.get('Portion','') not in (0,'0','') else ''
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

        html += f"""
            <tr>
              <td>
                <strong>{d.get('Name','')}</strong><span class='badge'>{d.get('Veg/Non Veg','').strip()}</span>
                <span class='description'>{d.get('Description','')}</span>
              </td>
              <td style="text-align: center;">{d.get('Pcs','')}</td>
              <td style="text-align: center;">{portions}</td>
              <td style="text-align: center;">{rate_display}</td>
              <td style="text-align: center;">{amount_display}</td>
            </tr>"""
    html += "</tbody></table>"

# 4. Other Services & Summary (PAGE 3)
html += f"""
        <div style="page-break-before: always;"></div>
        <div class="logo-wrapper">
          <img src="{logo_url}" class="main-logo" alt="Little Jalebis Logo">
        </div>
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

# 6. Final Page (PAGE 4)
html += f"""
    <div class="last-page" style="page-break-before: always; padding-top: 15px;">
      <div class="logo-wrapper">
        <img src="{logo_url}" class="main-logo" alt="Little Jalebis Logo">
      </div>
      <h3 style="text-decoration: underline; margin-bottom: 15px;">Please Note :</h3>
      <ul class="note-list" style="list-style-type: disc; padding-left: 20px; font-size: 14px;">
        <li style="margin-bottom: 10px;">We half-prepare snacks at our facility and finish them at your venue for maximum freshness. Main course is fully prepared in our kitchen ready to be served.</li>
        <li style="margin-bottom: 10px;">We do not require any minimum guarantees.</li>
        <li style="margin-bottom: 10px;">1 Portion of main course dish is sufficient for 3-4 Adults or 4-5 Kids.</li>
        <li style="margin-bottom: 10px;">In case kitchen access is not available, then additional charge of Rs 3000 will be applicable for stove with cylinder & other equipment.</li>
        <li style="margin-bottom: 10px;">To help us give you a flawless experience, we request for no changes in the menu 4-5 days prior to the event.</li>
        <li style="margin-bottom: 10px;">We also provide nanny boxes. Kindly connect with us for details.</li>
        <li style="margin-bottom: 10px;">Please let us know if there is an increase in the number of expected guests minimum 4-5 days prior.</li>
        <li style="margin-bottom: 10px;">All bookings are subject to availability at the time of confirmation with a non-refundable 50% advance payment.</li>
      </ul>

      <div style="text-align: center; margin-top: 40px;">
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