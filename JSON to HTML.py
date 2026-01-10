# 1. Configuration & Access
logo_url = "https://littlejalebis.com/wp-content/uploads/2025/04/LJ_Logo_M-2.svg"
collage_url = "https://vyaapaarniti.com/uploads/1767344535323-Screenshot%202026-01-02%20142942.png" 

try:
    cust_list = _input.all("Customer Details")
    cust = cust_list[0].json if cust_list else {}
except:
    cust = {}

menu_items = _input.all("Proposed Menu")
services = _input.all("Other Services")
host_reqs = _input.all("Other Info")

# 2. HTML Construction
html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
  /* Import Google Fonts - Quicksand for body, Chilanka for playful headings */
  @import url('https://fonts.googleapis.com/css2?family=Chilanka&family=Quicksand:wght@400;600;700&display=swap');

  @page {{
    /* Margin: Top, Right, Bottom, Left. */
    margin: 10mm 15mm 20mm 15mm; 
  }}
  
  body {{ 
    font-family: 'Quicksand', sans-serif; 
    color: #333; 
    line-height: 1.4;
    margin: 0;
    background: white;
  }}

  @media print {{
    body {{
      background: white;
      color: #333;
    }}
    h1, h2, h3 {{
      color: #2D3E50 !important;
    }}
    .header-banner {{
      background: #2D3E50 !important;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}
    .header-details div {{
      color: white !important;
    }}
  }}

  h1, h2, h3 {{ 
    font-family: 'Chilanka', cursive; 
    color: #2D3E50; 
    margin-top: 20px;
  }}

  /* REUSABLE PAGE BREAK CLASS */
  .full-page-section {{
    page-break-after: always;
    text-align: center;
    padding: 10mm 5mm;
  }}

  /* INTRO TEXT STYLING */
  .intro-text {{
    font-size: 18px;
    text-align: left;
    margin: 0 auto;
    max-width: 85%;
    line-height: 1.8;
  }}

  .intro-text p {{
    margin-bottom: 20px;
  }}

  /* GALLERY SPECIFIC STYLING */
  .gallery-image {{
    max-width: 90%;
    height: auto;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    margin-top: 10px;
  }}

  /* MAIN QUOTATION TABLE STYLING */
  .page-container {{
    width: 100%;
    border-collapse: collapse;
  }}

  .print-header {{
    display: table-header-group;
  }}

  .logo-container {{
    text-align: center;
    padding-bottom: 15px;
  }}

  /* ABSOLUTE FIXED FOOTER */
  .fixed-footer {{
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 10px;
    color: #666;
    padding-bottom: 0mm; 
    background: white;
  }}
  
  .footer-line {{
    border-top: 1px solid #ccc;
    margin: 0 15mm 0mm 15mm;
  }}

  .header-banner {{ 
    background: #2D3E50; 
    color: white;
    padding: 20px 25px;
    border-radius: 8px;
    margin-bottom: 15px;
    page-break-inside: avoid;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  .header-banner h1 {{ margin: 0; font-size: 26px; text-align: center; color: white !important; }}
  
  .header-details {{ 
    margin-top: 15px; 
    display: table;
    width: 100%;
    font-size: 13px; 
    border-top: 1px solid rgba(255,255,255,0.3);
    padding-top: 10px;
  }}

  .header-detail-row {{
    display: table-row;
  }}

  .header-detail-row div {{
    display: table-cell;
    width: 50%;
    padding: 5px 0;
    color: white;
  }}
  
  h2 {{ border-bottom: 2px solid #2D3E50; padding-bottom: 5px; font-size: 18px; text-transform: uppercase; }}
  
  .data-table {{ 
    width: 100%; 
    border-collapse: collapse; 
    margin-top: 10px; 
    table-layout: fixed;
    border-bottom: 1px solid #ccc;
  }}
  
  .data-table th {{ background: #f8f9fa; padding: 10px; text-align: left; border: 1px solid #999; font-size: 12px; }}
  .data-table td {{ padding: 10px; border: 1px solid #ccc; vertical-align: top; font-size: 13px; word-wrap: break-word; }}
  
  tr {{ page-break-inside: avoid; }}
  
  .col-right {{ text-align: right; }}
  .total-row {{ font-weight: bold; background-color: #f8f9fa; color: #2D3E50; }}
  .description {{ font-size: 11px; color: #666; font-style: italic; display: block; }}
  .badge {{ font-size: 9px; padding: 3px 8px; border-radius: 3px; background: #D3D3D3; color: #333; font-weight: bold; display: inline-block; margin-left: 8px; border: 1px solid #CCCCCC; white-space: nowrap; }}\n\n  .badge:empty {{ display: none; }}
</style>
</head>
<body>

<div class="fixed-footer">
  <div class="footer-line"></div>
  <strong>Little Jalebis – Kids Catering & Delivery Co. (Unit of NC Hospitality Pvt Ltd)</strong><br>
  E 5 Kalindi Colony, New Delhi 110065 | www.littlejalebis.com | sales@littlejalebis.com
</div>

<div class="full-page-section">
  <img src="{logo_url}" style="height: 100px; margin-bottom: 30px;">
  <div class="intro-text">
    <p>Hello from Little Jalebis - Kids Catering & Delivery Co., India's first catering company designed exclusively for kids, serving all of Delhi NCR.</p>
    
    <p>With over 40 years of hospitality expertise, we're here to make your celebration stress-free and memorable, whether it's a cozy gathering of 10 kids or a lively bash with 200 guests!</p>
    
    <p>Our specially curated menu is ready for you to explore. If you have ideas or suggestions, we'd love to hear them - together, we'll create a delightful culinary experience for your young VIPs.</p>
    
    <p>Looking forward to helping make your little one's celebration extra special!</p>
    
    <div style="margin-top: 50px;">
      <p>Warm Regards,<br>
      Team Little Jalebis<br>
      +91 8130964374</p>
    </div>
  </div>
</div>

<div class="full-page-section">
  <img src="{logo_url}" style="height: 80px; margin-bottom: 10px;">
  <img src="{collage_url}" class="gallery-image">
</div>

<table class="page-container">
  <thead class="print-header">
    <tr>
      <td>
        <div class="logo-container">
          <img src="{logo_url}" style="height: 80px; width: auto;">
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
              <div><strong>DATE:</strong> {cust.get('Event Date', 'N/A')}</div>
            </div>
            <div class="header-detail-row">
              <div><strong>PAX:</strong> {cust.get('Pax', 'N/A')}</div>
              <div><strong>LOCATION:</strong> {cust.get('Location', 'N/A')}</div>
            </div>
          </div>
        </div>

        <h2>PROPOSED MENU</h2>
"""
# 3. Process Menu Items - group by Category and render a table per category
from collections import OrderedDict
categories = OrderedDict()
for item in menu_items:
    d = item.json
    if not d.get('Name') or str(d.get('Name')).strip() == "": continue
    cat = d.get('Category','Other')
    categories.setdefault(cat, []).append(d)

# Generate a separate table per category (preserves first-seen category order)
for cat, items in categories.items():
    html += f"""
        <table class="data-table" style="margin-top: 20px; margin-bottom: 0;">
          <colgroup>
            <col style="width:55%" />
            <col style="width:10%" />
            <col style="width:10%" />
            <col style="width:12.5%" />
            <col style="width:12.5%" />
          </colgroup>
          <thead>
            <tr style="page-break-inside: avoid;">
              <th style="width:55%; background: #F6B27A; color: #2D3E50; padding: 10px; text-align: left; font-size: 14px; font-weight: bold; border: 1px solid #999; -webkit-print-color-adjust: exact; print-color-adjust: exact;">{cat.upper()}</th>
              <th style="width:10%; background: #F6B27A; color: #2D3E50; padding: 10px; text-align: center; font-size: 12px; font-weight: bold; border: 1px solid #999; -webkit-print-color-adjust: exact; print-color-adjust: exact;">PCS</th>
              <th style="width:10%; background: #F6B27A; color: #2D3E50; padding: 10px; text-align: center; font-size: 12px; font-weight: bold; border: 1px solid #999; -webkit-print-color-adjust: exact; print-color-adjust: exact;">PORTION</th>
              <th style="width:12.5%; background: #F6B27A; color: #2D3E50; padding: 10px; text-align: center; font-size: 12px; font-weight: bold; border: 1px solid #999; -webkit-print-color-adjust: exact; print-color-adjust: exact;">RATE</th>
              <th style="width:12.5%; background: #F6B27A; color: #2D3E50; padding: 10px; text-align: center; font-size: 12px; font-weight: bold; border: 1px solid #999; -webkit-print-color-adjust: exact; print-color-adjust: exact;">AMOUNT</th>
            </tr>
          </thead>
          <tbody>
    """
    for d in items:
        portions = d.get('Portion','') if d.get('Portion','') not in (0,'0','') else ''
        # Format Rate
        rate_raw = d.get('Rate','')
        try:
            r_str = str(rate_raw).replace(',','').strip()
            r_val = float(r_str)
            rate_display = f"₹{int(r_val):,}" if r_val.is_integer() else f"₹{r_val:,.2f}"
        except Exception:
            rate_display = rate_raw
        
        # Get Amount directly from input (already calculated as Portion × Rate)
        amount_raw = d.get('Amount','')
        try:
            a_str = str(amount_raw).replace(',','').strip()
            a_val = float(a_str)
            amount_display = f"₹{int(a_val):,}" if a_val == int(a_val) else f"₹{a_val:,.2f}"
        except Exception:
            amount_display = amount_raw if amount_raw else ""

        html += f"""
            <tr style="page-break-inside: avoid;">
              <td>
                <strong>{d.get('Name','')}</strong><span class='badge'>{d.get('Veg/Non Veg','').strip()}</span>
                <span class='description'>{d.get('Description','')}</span>
              </td>
              <td style="text-align: center;">{d.get('Pcs','')}</td>
              <td style="text-align: center;">{portions}</td>
              <td style="text-align: center;">{rate_display}</td>
              <td style="text-align: center;">{amount_display}</td>
            </tr>"""
    html += """
          </tbody>
        </table>
    """


# 4. Other Services & Summary
html += """
        <div style="page-break-inside: avoid; margin-top: 30px;">
          <h2>OTHER SERVICES & SUMMARY</h2>
          <table class='data-table'>
            <tbody>
"""

for s in services:
    sd = s.json
    service_name = sd.get('Other Services', '')
    if not service_name or str(service_name).strip() == "": continue
    amount = sd.get('Amount', '')
    # Format numeric amounts with rupee symbol and thousand separators
    try:
        amt_str = str(amount).replace(',','').strip()
        amt_val = float(amt_str)
        if amt_val.is_integer():
            amount_display = f"₹{int(amt_val):,}"
        else:
            amount_display = f"₹{amt_val:,.2f}"
    except Exception:
        amount_display = amount

    is_total = any(x in str(service_name).upper() for x in ["TOTAL", "SUBTOTAL", "GST"])
    row_class = "class='total-row'" if is_total else ""
    html += f"<tr {row_class}><td colspan='4'>{service_name}</td><td class='col-right'>{amount_display}</td></tr>"

html += "</tbody></table></div>" 

# 5. Host Requirements
if host_reqs:
    html += """
    <div style="page-break-inside: avoid;">
        <h2>TO BE PROVIDED BY HOST</h2>
        <ul style="font-size: 13px;">"""
    for h in host_reqs:
        req = h.json.get('TO BE PROVIDED BY HOST')
        qty_req = h.json.get('QUANTITY', '')
        if req and str(req).strip() != "": 
            html += f"<li style='margin-bottom: 5px;'><strong>{req}</strong>: {qty_req}</li>"
    html += "</ul></div>"

# Close the master table
html += """
      </td>
    </tr>
  </tbody>
</table>
"""

# 6. Final "Please Note" Page
html += f"""
    <div class="last-page" style="page-break-before: always; padding-top: 20px;">
      
      <div style="text-align: center; margin-bottom: 30px;">
        <img src="{logo_url}" style="height: 80px; width: auto;">
      </div>

      <h3 style="text-decoration: underline; margin-bottom: 20px;">Please Note :</h3>
      <ul class="note-list" style="list-style-type: disc; padding-left: 20px; font-size: 14px;">
        <li style="margin-bottom: 12px;">We half-prepare snacks at our facility and finish them at your venue for maximum freshness. Main course is fully prepared in our kitchen ready to be served.</li>
        <li style="margin-bottom: 12px;">We do not require any minimum guarantees.</li>
        <li style="margin-bottom: 12px;">1 Portion of main course dish is sufficient for 3-4 Adults or 4-5 Kids.</li>
        <li style="margin-bottom: 12px;">In case kitchen access is not available, then additional charge of Rs 3000 will be applicable for stove with cylinder & other equipment.</li>
        <li style="margin-bottom: 12px;">To help us give you a flawless experience, we request for no changes in the menu 4-5 days prior to the event.</li>
        <li style="margin-bottom: 12px;">We also provide nanny boxes. Kindly connect with us for details.</li>
        <li style="margin-bottom: 12px;">Please let us know if there is an increase in the number of expected guests minimum 4-5 days prior.</li>
        <li style="margin-bottom: 12px;">All bookings are subject to availability at the time of confirmation with a non-refundable 50% advance payment.</li>
      </ul>

      <div style="text-align: center; margin-top: 60px;">
          <p style="font-weight: bold; color: #D4813E; font-size: 16px; letter-spacing: 1px;">FOLLOW US @LITTLEJALEBIS</p>
          <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" style="height: 30px; vertical-align: middle; margin-top: 10px;">
      </div>
    </div>
  </body>
  </html>
"""

return [{"html_content": html}]