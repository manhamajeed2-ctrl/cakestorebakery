# SweetCrust Bakery — Streamlit

A Streamlit version of the SweetCrust Bakery website.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Put `app.py` and `requirements.txt` in a GitHub repository.
2. Create a new Streamlit app.
3. Set the **Main file path** to `app.py`.
4. Deploy.

## Before going live

Edit these values near the top of `app.py`:

- `BAKERY_NAME`
- `WHATSAPP_NUMBER`
- `PHONE`
- `EMAIL`
- `ADDRESS`
- `HOURS`

The online-payment choice is included in the checkout flow, but live payment processing still needs a payment gateway such as Razorpay or Stripe and merchant credentials.
