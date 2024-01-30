import hmac
import hashlib
import json

def validate_hmac_signature(secret_key, payload, signature_header):
    client_signature = hmac.new(secret_key.encode(), json.dumps(payload).encode(), digestmod=hashlib.sha256).hexdigest()
    print("client_signature:", client_signature)
    return hmac.compare_digest(client_signature, signature_header)

# secret key shared to the client
secret_key = 'NGK1EVz34NHf-Yq0UALetrQkZbi0PGNx'
# payload sent in webhook
payload = {
  "loan_id": "Tech internal testing 46",
  "event": "payment",
  "data": {
    "amount_recovered": 1000,
    "final_status": "Partially Recovered",
    "recovery_method": "",
    "payment_method": "",
    "payment_mode": "",
    "reference_number": "",
    "closure_with": "",
    "recovery_date": "2023-02-08 19:47:34.414759",
    "allocation_month": "2023-2-01",
    "author": "joginder.singh@credgenics.com",
    "amount_recovered_breakdown": None
  },
  "event_id": "hUYgLYGq"
}
# signature received in webhook (headers)
signature_header = 'fac499eb2feb1854632949ae90fc3632b7202807992ceef278a32ae7f3872dfa'

result = validate_hmac_signature(secret_key, payload, signature_header)

print(result)
