from locust import HttpUser, task, between
import json, copy

class CCRUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        """Called once per simulated user — we’ll get the token here."""
        print("Generating token once per user...")
        self.get_token()

    def get_token(self):
        headers = {
            "Content-Type": "application/json",
            "secureKey": "15082025"
        }

        payload = {
            "SiteID": "Harsh1",
            "Password": "12345",
            "ShipperAccountNumber": "539941414"
        }

        response = self.client.post("/3c_ccr/api/auth/token", json=payload, headers=headers)

        try:
            data = response.json()
            self.token = data.get("Token") or data.get("access_token")
            print(f"✅ Token generated: {self.token}")
        except Exception as e:
            print(f"❌ Failed to get token: {e}")
            self.token = None

    @task
    def ccr_flow(self):
        """This task runs repeatedly — each time gets a new CCR number and submits."""
        if not self.token:
            print("⚠️ Skipping, token not available.")
            return

        # Step 1: Get new CCR number
        headers = {
            "Authorization": f"Bearer {self.token}",
            "secureKey": "15082025"
        }

        response = self.client.get("/3c_ccr/api/questions", headers=headers)
        try:
            data = response.json()
            self.ccr_no = data.get("ReferenceNo") or data.get("CCRNo")
            print(f"📄 CCR Number received: {self.ccr_no}")
        except Exception as e:
            print(f"❌ Failed to parse CCR number: {e}")
            return

        # Step 2: Submit CCR using the dynamic CCR number
        self.submit_ccr(headers)

    def submit_ccr(self, headers):
        try:
            # Load your large JSON template from file
            with open("submit_payload.json", "r") as f:
                payload_template = json.load(f)

            # Make a deep copy so the base template isn't modified
            payload = copy.deepcopy(payload_template)

            # Update ReferenceNo dynamically
            payload["ReferenceNo"] = self.ccr_no

            # Prepare multipart form-data
            data = {
                "RequestData": json.dumps(payload)
            }

            files = {
                "Invoice": ("invoice.pdf", open("invoice.pdf", "rb"), "application/pdf")
            }

            response = self.client.post(
                "/3c_ccr/api/submit",
                headers=headers,
                data=data,
                files=files
            )

            print(f"✅ Submit API response: {response.status_code}")
            print(response.text)

        except Exception as e:
            print(f"❌ Error in submit CCR: {e}")

        finally:
            # Always close file handles
            for f in files.values():
                f[1].close()







a='cat'
#b=['ca','ct','at','ac','tc','ta']
a1= a+a
for i in range(len(a)):
    c=a[i]
    d=i+1
    for j in range(len(a)-1):
        e=c+a1[d]
        print(e)
        d+=1

