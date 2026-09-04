import streamlit as st
from datetime import date, timedelta
from urllib.parse import quote

st.set_page_config(
    page_title="SweetCrust Bakery",
    page_icon="🧁",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------
# Bakery configuration
# ---------------------------
BAKERY_NAME = "SweetCrust Bakery"
WHATSAPP_NUMBER = "919876543210"  # Change to your WhatsApp number, country code included.
PHONE = "+91 98765 43210"
EMAIL = "hello@sweetcrustbakery.com"
ADDRESS = "123, Bakery Street, Your City, PIN - 600001"
HOURS = "Mon–Sun · 9:00 AM – 9:00 PM"

PRODUCTS = [
    {
        "name": "Chocolate Truffle Cake",
        "price": 750,
        "unit": "500g",
        "emoji": "🍫",
        "desc": "Rich chocolate sponge with silky truffle.",
    },
    {
        "name": "Black Forest Cake",
        "price": 650,
        "unit": "500g",
        "emoji": "🍒",
        "desc": "Chocolate, cherries and fluffy cream layers.",
    },
    {
        "name": "Butterscotch Cake",
        "price": 650,
        "unit": "500g",
        "emoji": "🍯",
        "desc": "Caramel crunch with creamy butterscotch.",
    },
    {
        "name": "Red Velvet Cake",
        "price": 700,
        "unit": "500g",
        "emoji": "❤️",
        "desc": "Velvety sponge with smooth cream cheese.",
    },
    {
        "name": "Chocolate Pastry",
        "price": 120,
        "unit": "piece",
        "emoji": "🍰",
        "desc": "Moist chocolate layers with ganache.",
    },
    {
        "name": "Cupcakes (Box of 6)",
        "price": 360,
        "unit": "6 pcs",
        "emoji": "🧁",
        "desc": "Chocolate, vanilla or red velvet.",
    },
]

# ---------------------------
# Styling
# ---------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

    :root {
      --cream: #fff9f1;
      --warm: #f8ede0;
      --rose: #a83255;
      --rose-dark: #7b233c;
      --brown: #4b2a20;
      --gold: #c9964a;
      --text: #3c2a24;
      --muted: #74645d;
      --line: #eadbd0;
    }

    .stApp { background: var(--cream); color: var(--text); font-family: 'DM Sans', sans-serif; }
    .block-container { max-width: 1200px; padding-top: 1rem; padding-bottom: 3rem; }
    header[data-testid="stHeader"] { background: rgba(255,249,241,.95); }

    .topbar {
      background: var(--brown); color: #fff8f0; padding: .65rem 1rem; border-radius: 0 0 12px 12px;
      text-align: center; font-size: .92rem;
    }
    .brand { padding: 1.1rem 0 .4rem; }
    .brand h1 { font-family: 'Playfair Display', serif; font-size: 2.45rem; margin: 0; color: var(--brown); }
    .brand p { margin: 0; letter-spacing: .18em; color: var(--rose); font-weight: 700; }

    .hero {
      margin-top: .8rem; padding: 3rem 3.2rem; border-radius: 22px; min-height: 390px;
      background: linear-gradient(115deg, rgba(71,31,23,.96), rgba(116,45,37,.80)),
                  radial-gradient(circle at 84% 38%, rgba(255,206,140,.35), transparent 24%);
      color: white; display: flex; align-items: center; justify-content: space-between; overflow: hidden;
      box-shadow: 0 16px 40px rgba(75,42,32,.16);
    }
    .hero-copy { max-width: 650px; }
    .hero-eyebrow { font-family: 'Playfair Display', serif; color: #f8cf82; font-size: 1.2rem; margin-bottom: .5rem; }
    .hero h2 { font-family: 'Playfair Display', serif; font-size: clamp(2.7rem, 6vw, 5.2rem); line-height: .98; margin: .1rem 0 1rem; }
    .hero p { font-size: 1.08rem; max-width: 620px; color: #fff6ef; }
    .hero-art { font-size: 10rem; filter: drop-shadow(0 14px 20px rgba(0,0,0,.2)); }

    .section-title { text-align: center; margin: 3.3rem 0 1.5rem; }
    .section-title .eyebrow { color: var(--rose); font-weight: 800; letter-spacing: .14em; font-size: .8rem; }
    .section-title h2 { font-family: 'Playfair Display', serif; font-size: 2.35rem; margin: .2rem 0; color: var(--brown); }
    .section-title p { color: var(--muted); }

    .feature { padding: 1rem; border-right: 1px solid var(--line); }
    .feature:last-child { border-right: none; }
    .feature strong { display: block; color: var(--brown); }
    .feature span { color: var(--muted); font-size: .9rem; }

    .product-card { background: white; border: 1px solid var(--line); border-radius: 18px; padding: 1rem; height: 100%; box-shadow: 0 8px 24px rgba(86,56,43,.06); }
    .product-art { background: var(--warm); border-radius: 14px; height: 145px; display: flex; align-items: center; justify-content: center; font-size: 5.5rem; }
    .product-card h3 { color: var(--brown); margin: .8rem 0 .2rem; font-family: 'Playfair Display', serif; }
    .product-card p { color: var(--muted); min-height: 45px; margin-bottom: .7rem; }
    .price { font-weight: 800; color: var(--rose); }

    .about-box, .custom-box { border-radius: 20px; padding: 2rem; height: 100%; border: 1px solid var(--line); }
    .about-box { background: #fff; }
    .custom-box { background: #f8e8ec; }
    .about-box h2, .custom-box h2 { font-family: 'Playfair Display', serif; color: var(--brown); }
    .stat { text-align: center; padding: .8rem .4rem; border-right: 1px solid var(--line); }
    .stat:last-child { border-right: none; }
    .stat b { color: var(--rose); font-size: 1.35rem; display: block; }
    .stat span { color: var(--muted); font-size: .83rem; }

    .gallery-tile { background: white; border: 1px solid var(--line); border-radius: 16px; padding: 1.4rem; text-align: center; font-size: 3.1rem; }
    .gallery-tile span { display: block; margin-top: .5rem; color: var(--brown); font-weight: 700; font-size: .95rem; }

    .quote { background: white; border: 1px solid var(--line); border-radius: 16px; padding: 1.3rem; height: 100%; }
    .quote p { font-size: 1.05rem; }
    .quote small { color: var(--rose); font-weight: 800; }

    .checkout { background: white; border: 1px solid var(--line); border-radius: 20px; padding: 1.2rem; }
    .checkout-note { background: #fff6df; border-left: 4px solid var(--gold); padding: .85rem 1rem; border-radius: 9px; color: #674a1f; }
    .success-card { background: #effaf1; border: 1px solid #bfe4c5; border-radius: 14px; padding: 1rem; }

    .contact-card { background: var(--brown); color: #fff8f0; border-radius: 20px; padding: 2rem; }
    .contact-card h3 { font-family: 'Playfair Display', serif; color: white; }
    .footer-note { text-align: center; margin-top: 2.5rem; padding: 1.3rem; color: var(--muted); border-top: 1px solid var(--line); }

    div.stButton > button, div.stFormSubmitButton > button {
      background: var(--rose); color: white; border: none; border-radius: 10px; font-weight: 700; padding: .62rem 1rem;
    }
    div.stButton > button:hover, div.stFormSubmitButton > button:hover { background: var(--rose-dark); color: white; }

    @media (max-width: 700px) {
      .hero { padding: 2rem; }
      .hero-art { font-size: 6rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Helpers
# ---------------------------
def money(amount: float) -> str:
    return f"₹{amount:,.0f}"


def product_by_name(name: str):
    return next((p for p in PRODUCTS if p["name"] == name), None)


def whatsapp_url(message: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"

# ---------------------------
# Header / hero
# ---------------------------
st.markdown("<div class='topbar'>🍰 Freshly baked every day with love & the finest ingredients.</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='brand'><h1>🧁 SweetCrust</h1><p>BAKERY</p></div>",
    unsafe_allow_html=True,
)

hero_left, hero_right = st.columns([1.7, 1], gap="large")
with hero_left:
    st.markdown(
        """
        <div class='hero-copy'>
          <div class='hero-eyebrow'>Made With Love ♡</div>
          <h2>Freshly Baked,<br>Made For You</h2>
          <p>Delicious cakes, pastries, breads and more — baked fresh every day to make your moments extra special.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with hero_right:
    st.markdown("<div class='hero-art'>🍰</div>", unsafe_allow_html=True)
    order_col, menu_col = st.columns(2)
    with order_col:
        st.link_button("🛍 Order Now", "#place-your-order", use_container_width=True)
    with menu_col:
        st.link_button("☷ View Menu", "#our-bestsellers", use_container_width=True)

# ---------------------------
# Features
# ---------------------------
features = [
    ("♨ Freshly Baked", "Made fresh every day"),
    ("◌ 100% Quality", "Fine & hygienic ingredients"),
    ("✿ Custom Made", "Cakes for every occasion"),
    ("🛵 On-time Delivery", "Timely delivery for special moments"),
]
cols = st.columns(4)
for col, (title, detail) in zip(cols, features):
    with col:
        st.markdown(f"<div class='feature'><strong>{title}</strong><span>{detail}</span></div>", unsafe_allow_html=True)

# ---------------------------
# Menu
# ---------------------------
st.markdown("<div id='our-bestsellers'></div>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-title'><div class='eyebrow'>OUR FAVORITES</div><h2>Our Bestsellers</h2><p>Customer-loved treats, made fresh and ready to make your day sweeter.</p></div>",
    unsafe_allow_html=True,
)

for row_start in range(0, len(PRODUCTS), 3):
    row = PRODUCTS[row_start:row_start + 3]
    cols = st.columns(len(row), gap="medium")
    for col, product in zip(cols, row):
        with col:
            st.markdown(
                f"""
                <div class='product-card'>
                  <div class='product-art'>{product['emoji']}</div>
                  <h3>{product['name']}</h3>
                  <p>{product['desc']}</p>
                  <div class='price'>{money(product['price'])} / {product['unit']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# ---------------------------
# About + custom cake
# ---------------------------
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("<div class='section-title'><div class='eyebrow'>A LITTLE ABOUT US</div><h2>From our oven to your happiest moments.</h2></div>", unsafe_allow_html=True)
about_col, custom_col = st.columns(2, gap="large")
with about_col:
    st.markdown(
        """
        <div class='about-box'>
          <h2>Made to bring happiness, one bite at a time.</h2>
          <p>At SweetCrust Bakery, we believe every bite should bring happiness. From our oven to your heart, we create delightful treats using fine ingredients, with love, patience and perfection.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    s1, s2, s3 = st.columns(3)
    for col, num, label in [(s1, "50+", "Delicious Items"), (s2, "1000+", "Happy Customers"), (s3, "5+", "Years of Baking")]:
        with col:
            st.markdown(f"<div class='stat'><b>{num}</b><span>{label}</span></div>", unsafe_allow_html=True)
with custom_col:
    st.markdown(
        """
        <div class='custom-box'>
          <div class='eyebrow'>FOR YOUR SPECIAL MOMENTS</div>
          <h2>Order Your Custom Cake</h2>
          <p>Tell us your theme, flavor and date — we'll create a cake made just for you.</p>
          <p>🎨 Custom Design &nbsp;&nbsp; 🍓 Flavors &nbsp;&nbsp; 🎁 Any Occasion &nbsp;&nbsp; ✨ Fresh & Delicious</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("🎂 Request a Custom Cake", use_container_width=True):
        st.session_state.custom_selected = True
        st.toast("Choose Custom Cake in the order form below.")

# ---------------------------
# Gallery
# ---------------------------
st.markdown("<div class='section-title'><div class='eyebrow'>FROM OUR KITCHEN</div><h2>Gallery</h2><p>Replace these placeholders with your own bakery photos when you're ready.</p></div>", unsafe_allow_html=True)
gallery = [("🍰", "Celebration Cakes"), ("🥐", "Fresh Pastries"), ("🍪", "Cookies & Treats"), ("🧁", "Cupcakes"), ("🍞", "Fresh Breads"), ("🎂", "Custom Orders")]
for i in range(0, 6, 3):
    cols = st.columns(3)
    for col, (emoji, label) in zip(cols, gallery[i:i+3]):
        with col:
            st.markdown(f"<div class='gallery-tile'>{emoji}<span>{label}</span></div>", unsafe_allow_html=True)

# ---------------------------
# Testimonials
# ---------------------------
st.markdown("<div class='section-title'><div class='eyebrow'>HAPPY CUSTOMERS</div><h2>What Our Customers Say</h2></div>", unsafe_allow_html=True)
testimonials = [
    ("The cake was so fresh and delicious. Everyone loved it!", "— Priya S."),
    ("Best bakery in town! Their pastries are simply amazing.", "— Rahul T."),
    ("I ordered a custom cake and it was beyond my expectations.", "— Neha K."),
]
cols = st.columns(3)
for col, (quote_text, person) in zip(cols, testimonials):
    with col:
        st.markdown(f"<div class='quote'><p>“{quote_text}”</p><small>{person}</small></div>", unsafe_allow_html=True)

# ---------------------------
# Checkout / order form
# ---------------------------
st.markdown("<div id='place-your-order'></div>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-title'><div class='eyebrow'>SECURE CHECKOUT</div><h2>Place Your Cake Order</h2><p>Choose your product, enter the delivery address, and select how you would like to pay.</p></div>",
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.markdown("### 1. Order Details")
    product_options = [p["name"] for p in PRODUCTS] + ["Custom Cake — Price on request"]
    default_product = "Custom Cake — Price on request" if st.session_state.get("custom_selected") else PRODUCTS[0]["name"]
    product_name = st.selectbox("Cake / Product", product_options, index=product_options.index(default_product))
    c1, c2 = st.columns(2)
    with c1:
        quantity = st.number_input("Quantity", min_value=1, max_value=50, value=1, step=1)
    with c2:
        delivery_date = st.date_input("Delivery Date", min_value=date.today() + timedelta(days=1), value=date.today() + timedelta(days=1))
    cake_message = st.text_input("Special message on cake", placeholder="e.g. Happy Birthday, Aisha!")
    notes = st.text_area("Additional notes", placeholder="Flavor, design, eggless request, etc.")

    st.markdown("### 2. Delivery Address")
    c1, c2 = st.columns(2)
    with c1:
        customer_name = st.text_input("Customer Name *")
    with c2:
        customer_phone = st.text_input("Phone Number *", placeholder="10-digit mobile number")
    address1 = st.text_input("House / Flat / Building *", placeholder="House no., flat, building")
    address2 = st.text_input("Street / Area *", placeholder="Street, locality, area")
    c1, c2 = st.columns(2)
    with c1:
        city = st.text_input("City *")
    with c2:
        pincode = st.text_input("PIN Code *", max_chars=6, placeholder="6-digit PIN")
    landmark = st.text_input("Landmark (optional)", placeholder="Near school, mall, etc.")

    st.markdown("### 3. Payment Method")
    payment = st.radio(
        "Choose a payment method *",
        ["UPI / Card / Net Banking", "Cash on Delivery", "Pay at Bakery"],
        index=0,
        help="The first option is ready for gateway integration. Add Razorpay/Stripe credentials when you want live payments.",
    )

    if payment == "UPI / Card / Net Banking":
        st.markdown(
            "<div class='checkout-note'>Online payment is selected. The app currently records the choice and sends the order to WhatsApp. For live payments, connect Razorpay or Stripe using your merchant credentials.</div>",
            unsafe_allow_html=True,
        )

    st.markdown("### 4. Final Confirmation")
    submit = st.button("✅ Place Order & Continue", type="primary", use_container_width=True)

if submit:
    clean_phone = "".join(ch for ch in customer_phone if ch.isdigit())
    errors = []
    if not customer_name.strip():
        errors.append("Enter the customer name.")
    if len(clean_phone) != 10:
        errors.append("Enter a valid 10-digit phone number.")
    if not address1.strip() or not address2.strip() or not city.strip():
        errors.append("Complete the delivery address.")
    if len(pincode.strip()) != 6 or not pincode.strip().isdigit():
        errors.append("Enter a valid 6-digit PIN code.")

    selected = product_by_name(product_name)
    total_text = "Price on request" if not selected else money(selected["price"] * quantity)
    address_text = f"{address1}, {address2}, {city} - {pincode}" + (f", Landmark: {landmark}" if landmark.strip() else "")
    order_message = (
        f"Hi {BAKERY_NAME}!%0A%0A"
        f"*New Cake Order*%0A"
        f"Product: {product_name}%0A"
        f"Quantity: {quantity}%0A"
        f"Delivery date: {delivery_date.strftime('%d-%m-%Y')}%0A"
        f"Cake message: {cake_message.strip() or 'None'}%0A"
        f"Notes: {notes.strip() or 'None'}%0A%0A"
        f"*Customer*%0AName: {customer_name.strip()}%0APhone: {customer_phone.strip()}%0A%0A"
        f"*Delivery Address*%0A{address_text}%0A%0A"
        f"*Payment Method*%0A{payment}%0A%0A"
        f"Estimated total: {total_text}%0A"
        f"Please confirm availability, delivery charge, and final total."
    )

    if errors:
        st.error("Please fix the following: " + " ".join(errors))
    else:
        st.markdown(
            f"<div class='success-card'><strong>Order details are ready.</strong><br>Estimated total: <b>{total_text}</b><br>Delivery to: {address_text}<br>Payment: {payment}</div>",
            unsafe_allow_html=True,
        )
        st.link_button("💬 Send Order to WhatsApp", whatsapp_url(order_message), use_container_width=True)
        if payment == "UPI / Card / Net Banking":
            st.info("For live online payment, replace the placeholder with your Razorpay/Stripe checkout after setting up your merchant account.")

# ---------------------------
# Contact / footer
# ---------------------------
st.markdown("<div class='section-title'><div class='eyebrow'>LET'S TALK SWEETS</div><h2>Ready to order?</h2><p>Call, WhatsApp, or visit us. For custom cakes, message us with your date, size, flavor and design idea.</p></div>", unsafe_allow_html=True)
contact_left, contact_right = st.columns(2, gap="large")
with contact_left:
    st.markdown(
        f"""
        <div class='contact-card'>
          <h3>{BAKERY_NAME}</h3>
          <p>📞 {PHONE}</p>
          <p>✉️ {EMAIL}</p>
          <p>📍 {ADDRESS}</p>
          <p>🕘 {HOURS}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with contact_right:
    st.markdown("### Find us")
    st.map([], zoom=12)  # Replace with a latitude/longitude point for your bakery.
    st.link_button("📍 Get Directions", "https://maps.google.com/?q=Bakery", use_container_width=True)
    st.link_button("💬 Chat on WhatsApp", f"https://wa.me/{WHATSAPP_NUMBER}", use_container_width=True)

st.markdown(
    f"<div class='footer-note'>© {date.today().year} {BAKERY_NAME}. All rights reserved. · Freshly baked happiness, every day.</div>",
    unsafe_allow_html=True,
)
