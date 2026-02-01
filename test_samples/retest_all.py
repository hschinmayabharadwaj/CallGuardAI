"""
Comprehensive retest of all CallGuard AI features
"""
import requests
import json
import os
from pathlib import Path

API_BASE = "http://localhost:8000/api/v1"

print("="*80)
print("CALLGUARD AI - COMPREHENSIVE RETEST")
print("="*80)

# Track results
results = {"passed": 0, "failed": 0, "tests": []}

def test(name, condition, details=""):
    global results
    if condition:
        results["passed"] += 1
        results["tests"].append({"name": name, "status": "PASS", "details": details})
        print(f"✓ {name}")
    else:
        results["failed"] += 1
        results["tests"].append({"name": name, "status": "FAIL", "details": details})
        print(f"✗ {name}: {details}")

# ============ API Health Check ============
print("\n" + "="*40)
print("1. API HEALTH CHECK")
print("="*40)

r = requests.get("http://localhost:8000/")
test("Root endpoint", r.status_code == 200, r.text[:50] if r.status_code != 200 else "")

r = requests.get("http://localhost:8000/api/docs")
test("API docs", r.status_code == 200)

# ============ System Status ============
print("\n" + "="*40)
print("2. SYSTEM STATUS")
print("="*40)

r = requests.get(f"{API_BASE}/admin/stats")
if r.status_code == 200:
    stats = r.json()
    test("Admin stats endpoint", True)
    test("Database connected", stats.get("database_connected") == True, stats.get("database_type", ""))
    test("ML models operational", stats.get("ml_models", {}).get("overall") == "operational")
    test("Total calls tracked", stats.get("total_calls", 0) > 0, f"{stats.get('total_calls', 0)} calls")
else:
    test("Admin stats endpoint", False, str(r.status_code))

# ============ Audio Analysis ============
print("\n" + "="*40)
print("3. AUDIO ANALYSIS")
print("="*40)

test_audio = Path("d:/hackathon/test_samples/batch3/en_bank_freeze.mp3")
if test_audio.exists():
    with open(test_audio, 'rb') as f:
        files = {'file': ('test.mp3', f, 'audio/mpeg')}
        r = requests.post(f"{API_BASE}/analyze/upload", files=files)
    
    if r.status_code == 200:
        result = r.json()
        test("Audio upload", True)
        test("Call ID generated", bool(result.get("call_id")))
        test("Classification returned", result.get("classification") in ["safe", "spam", "fraud", "phishing", "robocall"])
        test("Risk score calculated", 0 <= result.get("risk_score", -1) <= 100)
        test("Transcript generated", len(result.get("transcript", "")) > 10)
    else:
        test("Audio upload", False, f"Status {r.status_code}")
else:
    test("Audio upload", False, "Test file not found")

# ============ Text Analysis ============
print("\n" + "="*40)
print("4. TEXT ANALYSIS")
print("="*40)

test_messages = [
    {"text": "Your bank account has been suspended. Call now to verify your identity.", "expected": "fraud"},
    {"text": "Hi, your appointment is confirmed for tomorrow at 3 PM.", "expected": "safe"}
]

for msg in test_messages:
    r = requests.post(f"{API_BASE}/analyze/text", params={"text": msg["text"]})
    if r.status_code == 200:
        result = r.json()
        is_correct = (msg["expected"] != "safe" and result.get("classification") != "safe") or \
                     (msg["expected"] == "safe" and result.get("classification") == "safe")
        test(f"Text analysis ({msg['expected']})", is_correct, 
             f"Got {result.get('classification')} (risk: {result.get('risk_score')})")
    else:
        test(f"Text analysis ({msg['expected']})", False, str(r.status_code))

# ============ Call History ============
print("\n" + "="*40)
print("5. CALL HISTORY")
print("="*40)

r = requests.get(f"{API_BASE}/calls/")
if r.status_code == 200:
    data = r.json()
    test("List calls", True)
    test("Calls have required fields", 
         len(data.get("calls", [])) > 0 and "call_id" in data["calls"][0] and "classification" in data["calls"][0])
else:
    test("List calls", False)

# Test filters
r = requests.get(f"{API_BASE}/calls/?classification=fraud&limit=5")
test("Filter by classification", r.status_code == 200)

r = requests.get(f"{API_BASE}/calls/?min_risk_score=50")
test("Filter by risk score", r.status_code == 200)

r = requests.get(f"{API_BASE}/calls/count")
test("Call count endpoint", r.status_code == 200)

# ============ Call Details ============
print("\n" + "="*40)
print("6. CALL DETAILS")
print("="*40)

r = requests.get(f"{API_BASE}/calls/?limit=1")
if r.status_code == 200 and r.json().get("calls"):
    call_id = r.json()["calls"][0]["call_id"]
    r_detail = requests.get(f"{API_BASE}/calls/{call_id}")
    if r_detail.status_code == 200:
        detail = r_detail.json()
        test("Get call details", True)
        test("Details include transcript", "transcript" in detail)
        test("Details include fraud_indicators", "fraud_indicators" in detail)
    else:
        test("Get call details", False, str(r_detail.status_code))
else:
    test("Get call details", False, "No calls to test")

# ============ Analytics ============
print("\n" + "="*40)
print("7. ANALYTICS")
print("="*40)

r = requests.get(f"{API_BASE}/analytics/dashboard")
test("Dashboard endpoint", r.status_code == 200)

r = requests.get(f"{API_BASE}/analytics/trends?period=7d")
test("Trends endpoint", r.status_code == 200)

r = requests.get(f"{API_BASE}/analytics/heatmap")
test("Heatmap endpoint", r.status_code == 200)

r = requests.get(f"{API_BASE}/analytics/keywords")
test("Keywords endpoint", r.status_code == 200)

r = requests.get(f"{API_BASE}/analytics/classification-stats")
test("Classification stats", r.status_code == 200)

# ============ Recent Alerts ============
print("\n" + "="*40)
print("8. RECENT ALERTS")
print("="*40)

r = requests.get(f"{API_BASE}/calls/recent/alerts?limit=5")
if r.status_code == 200:
    alerts = r.json()
    test("Recent alerts endpoint", True)
    test("Alerts have severity", len(alerts) > 0 and "severity" in alerts[0])
else:
    test("Recent alerts endpoint", False, str(r.status_code))

# ============ Admin Rules ============
print("\n" + "="*40)
print("9. ADMIN RULES")
print("="*40)

r = requests.get(f"{API_BASE}/admin/rules")
test("List rules", r.status_code == 200)

# Create a new rule
new_rule = {
    "name": f"Test Rule {os.urandom(4).hex()}",
    "rule_type": "keyword",
    "keywords": ["test", "fraud"],
    "description": "Test rule for retest",
    "is_active": True,
    "severity": "medium"
}
r = requests.post(f"{API_BASE}/admin/rules", json=new_rule)
if r.status_code in [200, 201]:
    test("Create rule", True)
    rule_id = r.json().get("id")
    
    # Delete the rule
    if rule_id:
        r_del = requests.delete(f"{API_BASE}/admin/rules/{rule_id}")
        test("Delete rule", r_del.status_code == 200)
else:
    test("Create rule", False, str(r.status_code))

# ============ Authentication ============
print("\n" + "="*40)
print("10. AUTHENTICATION")
print("="*40)

# Register new user
import random
random_suffix = random.randint(1000, 9999)
register_data = {
    "email": f"retest{random_suffix}@test.com",
    "username": f"retestuser{random_suffix}",
    "password": "testpass123",
    "full_name": "Retest User"
}
r = requests.post(f"{API_BASE}/auth/register", json=register_data)
test("User registration", r.status_code == 200, r.text[:50] if r.status_code != 200 else "")

# Login
login_data = {"username": register_data["username"], "password": register_data["password"]}
r = requests.post(f"{API_BASE}/auth/login", json=login_data)
if r.status_code == 200:
    token = r.json().get("access_token")
    test("User login", bool(token))
    
    # Get profile
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(f"{API_BASE}/auth/me", headers=headers)
    test("Get user profile", r.status_code == 200)
else:
    test("User login", False, str(r.status_code))

# ============ Summary ============
print("\n" + "="*80)
print("RETEST SUMMARY")
print("="*80)
print(f"\n✓ Passed: {results['passed']}")
print(f"✗ Failed: {results['failed']}")
print(f"Total: {results['passed'] + results['failed']}")
print(f"Success Rate: {results['passed'] / (results['passed'] + results['failed']) * 100:.1f}%")
print("\n" + "="*80)
