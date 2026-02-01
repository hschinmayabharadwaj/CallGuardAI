# CallGuard AI Platform

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/React-18+-61DAFB.svg" alt="React">
  <img src="https://img.shields.io/badge/FastAPI-0.100+-009688.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/TypeScript-5.0+-3178C6.svg" alt="TypeScript">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Deploy-Vercel%20%2B%20Render-brightgreen.svg" alt="Deploy">
</p>

<p align="center">
  <b>A comprehensive AI-powered platform for detecting spam calls, fraud, phishing attempts, robocalls, and AI-generated voices (deepfakes) with multi-language support.</b>
</p>

---

## 🚀 Live Demo

- **Frontend (Vercel)**: [Deploy your own →](https://vercel.com)
- **Backend (Render)**: [Deploy your own →](https://render.com)
- **GitHub**: https://github.com/Bhanutejayadalla/CallGuardAI

---

## 📑 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Database & Data Storage](#-database--data-storage)
- [API Endpoints](#-api-endpoints)
- [AI Voice Detection](#-ai-voice-detection-algorithm)
- [Supported Languages](#-supported-languages)
- [Tech Stack](#-tech-stack)
- [Test Results](#-test-results)
- [Deployment](#-deployment)
- [How to Run](#-how-to-run-the-project)

---

## 🎯 Features

### 1. 🤖 AI-Generated Voice Detection (Multi-Language) ⭐ HIGHLIGHT

Our state-of-the-art deepfake voice detection system identifies AI-generated synthetic voices vs. genuine human voices using advanced acoustic analysis.

| Feature | Description |
|---------|-------------|
| **Deepfake Detection** | Identifies AI-generated/synthetic voices with high accuracy |
| **Multi-Language Support** | Tamil (தமிழ்), English, Hindi (हिंदी), Malayalam (മലയാളം), Telugu (తెలుగు) |
| **Base64 Audio Input** | API accepts Base64-encoded MP3/WAV/FLAC/OGG audio |
| **Confidence Scoring** | Returns probability score (0.0-1.0) with percentage |
| **Detailed Explanations** | Human-readable analysis with AI/human indicators |
| **Fast Processing** | ~2-3 seconds for 1 second of audio |

**How It Works:**
- **Spectral Analysis**: Analyzes frequency patterns that differ between AI and human voices
- **Temporal Features**: Examines timing patterns in speech that AI often gets wrong
- **Prosody Detection**: Evaluates pitch, rhythm, and intonation for natural speech patterns

### 2. 📞 Real-Time Call Analysis

Comprehensive call analysis system that processes audio in real-time to detect potential threats.

| Feature | Description |
|---------|-------------|
| **Live Audio Streaming** | WebSocket-based real-time audio processing |
| **Risk Scoring** | Dynamic 0-100 risk score with explainable insights |
| **Call Classification** | Categorizes as Safe, Spam, Fraud, Phishing, or Robocall |
| **Transcript Generation** | Real-time speech-to-text with highlighting |

### 3. 🔍 Spam & Fraud Detection

Advanced fraud detection using NLP and pattern matching.

| Feature | Description |
|---------|-------------|
| **Scam Keyword Detection** | Identifies suspicious phrases and keywords |
| **Intent Analysis** | NLP-based intent classification |
| **Pressure Tactic Detection** | Identifies urgency and manipulation techniques |
| **Pattern Recognition** | Learns from historical fraud patterns |

### 4. 🌐 Multi-Language Speech Recognition

Powered by OpenAI Whisper for accurate transcription across multiple languages.

| Feature | Description |
|---------|-------------|
| **7 Languages Supported** | Tamil, English, Hindi, Malayalam, Telugu, Spanish, French, German |
| **Automatic Detection** | Auto-detects spoken language |
| **High Accuracy** | State-of-the-art speech recognition |
| **Real-time Processing** | Fast transcription for live calls |

### 5. 📊 Analytics Dashboard

Comprehensive dashboard for monitoring and analyzing call patterns.

| Feature | Description |
|---------|-------------|
| **Real-time Metrics** | Live statistics and threat indicators |
| **Call History** | Searchable history with filters |
| **Risk Trends** | Visual analytics of fraud patterns |
| **Alert System** | Notifications for high-risk calls |
| **Heatmap** | Call volume by day and hour |
| **Keyword Tracking** | Top suspicious keywords detected |

### 6. 🎨 Modern User Interface

Beautiful, responsive UI built with React and Tailwind CSS.

| Feature | Description |
|---------|-------------|
| **Dark/Light Mode** | Toggle between themes |
| **Responsive Design** | Works on desktop and mobile |
| **Real-time Updates** | Live data refresh |
| **Multilingual UI** | Interface available in multiple languages |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Frontend (React + TypeScript)            │
│                     http://localhost:3000                    │
├─────────────────────────────────────────────────────────────┤
│                            ↕ REST API                        │
├─────────────────────────────────────────────────────────────┤
│                     Backend (FastAPI)                        │
│                     http://localhost:8000                    │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Whisper   │  │   Librosa   │  │   AI Voice Detector │  │
│  │   (Speech)  │  │   (Audio)   │  │   (Deepfake)        │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                     Database (SQLite/PostgreSQL)             │
│                     Async SQLAlchemy ORM                     │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗄️ Database & Data Storage

### How Data is Stored

CallGuard AI uses **SQLAlchemy ORM** with async support for efficient database operations. The system supports both **SQLite** (development) and **PostgreSQL** (production).

#### Database Tables

| Table | Purpose | Key Fields |
|-------|---------|------------|
| `calls` | Stores all call analysis records | call_id, transcript, classification, risk_score, fraud_indicators |
| `users` | User accounts for authentication | id, email, username, hashed_password |
| `detection_rules` | Custom fraud detection rules | name, keywords, category, severity |
| `call_segments` | Audio segments for long calls | call_id, segment_index, text |
| `fraud_patterns` | Known fraud patterns | pattern, category, weight |

#### Data Flow

1. **Audio Upload** → Whisper transcribes → NLP analyzes → Fraud detector scores → Stored in `calls` table
2. **Text Analysis** → NLP processes → Pattern matching → Risk calculated → Stored in `calls` table
3. **User Actions** → JWT authenticated → Validated → Stored/Retrieved from database

### Database Configuration

**SQLite (Default - Development)**
```
DATABASE_URL=sqlite+aiosqlite:///./callguard.db
```
- Zero configuration required
- File-based database (`callguard.db`)
- Perfect for development and testing
- Data persists in backend folder

**PostgreSQL (Production)**
```
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/callguard
```
- Scalable for production
- Concurrent connections supported
- Better performance for large datasets
- Requires PostgreSQL server setup

### Database Statistics (Current)

| Metric | Value |
|--------|-------|
| Total Calls Analyzed | 76+ |
| Classifications | Safe: 34, Fraud: 16, Phishing: 12, Robocall: 7, Spam: 1 |
| Detection Rules | 4 active rules |
| User Accounts | 4 registered users |
| Database Type | SQLite (auto-configured) |

---

## 🔌 API Endpoints

### Audio Analysis

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/analyze/upload` | Upload audio file for analysis |
| POST | `/api/v1/analyze/text` | Analyze text message for fraud |
| GET | `/api/v1/analyze/status/{call_id}` | Get analysis status |

### Call Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/calls/` | List calls with filters |
| GET | `/api/v1/calls/{call_id}` | Get call details |
| GET | `/api/v1/calls/count` | Get total call count |
| GET | `/api/v1/calls/recent/alerts` | Get recent high-risk alerts |
| DELETE | `/api/v1/calls/{call_id}` | Delete a call record |

**Query Parameters for `/api/v1/calls/`:**
- `classification` - Filter by type (safe, fraud, phishing, spam, robocall)
- `min_risk_score` - Filter by minimum risk score (0-100)
- `status` - Filter by status (pending, processing, completed, failed)
- `limit` - Number of results (default: 50)
- `skip` - Offset for pagination

### Analytics

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/analytics/dashboard` | Dashboard statistics |
| GET | `/api/v1/analytics/trends` | Call trends over time |
| GET | `/api/v1/analytics/heatmap` | Call volume heatmap |
| GET | `/api/v1/analytics/keywords` | Top suspicious keywords |
| GET | `/api/v1/analytics/classification-stats` | Classification breakdown |

### Admin

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/admin/stats` | System statistics |
| GET | `/api/v1/admin/rules` | List detection rules |
| POST | `/api/v1/admin/rules` | Create new rule |
| PUT | `/api/v1/admin/rules/{id}` | Update a rule |
| DELETE | `/api/v1/admin/rules/{id}` | Delete a rule |
| POST | `/api/v1/admin/rules/init-defaults` | Initialize default rules |

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register` | Register new user |
| POST | `/api/v1/auth/login` | Login and get JWT token |
| POST | `/api/v1/auth/token` | Get access token |
| GET | `/api/v1/auth/me` | Get current user profile |

### AI Voice Detection

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/ai-voice/health` | Health check |
| GET | `/api/v1/ai-voice/languages` | Supported languages |
| POST | `/api/v1/ai-voice/detect` | Detect AI-generated voice |

---

## 🧠 AI Voice Detection Algorithm

The AI voice detector uses multiple acoustic features to identify synthetic voices:

### Feature Analysis

| Feature | Description | AI Indicator |
|---------|-------------|--------------|
| Spectral Flatness | Measures tonal vs. noise-like content | Too uniform = AI |
| Pitch Variation | Natural speech has variable pitch | Too regular = AI |
| MFCC Variance | Mel-frequency cepstral coefficients | Low variance = AI |
| Onset Regularity | Timing of speech sounds | Too regular = AI |
| Harmonic-to-Noise Ratio | Voice quality measure | Abnormal = AI |
| Zero Crossing Rate | Signal oscillation frequency | Abnormal = AI |

### Classification Thresholds

- **AI Generated**: Score ≥ 0.60
- **Human**: Score ≤ 0.40
- **Uncertain**: 0.40 < Score < 0.60

---

## 📊 Supported Languages

| Code | Language | Native Name | Fraud Detection | AI Voice |
|------|----------|-------------|-----------------|----------|
| `en` | English | English | ✅ Full | ✅ |
| `hi` | Hindi | हिंदी | ✅ Full | ✅ |
| `ta` | Tamil | தமிழ் | ✅ Full | ✅ |
| `te` | Telugu | తెలుగు | ✅ Full | ✅ |
| `ml` | Malayalam | മലയാളം | ⚠️ Partial | ✅ |
| `es` | Spanish | Español | ⚠️ Partial | ❌ |
| `fr` | French | Français | ⚠️ Partial | ❌ |
| `de` | German | Deutsch | ⚠️ Partial | ❌ |

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** - High-performance Python web framework
- **Python 3.11+** - Core language
- **SQLAlchemy 2.0** - Async database ORM
- **Whisper** - OpenAI speech recognition
- **Librosa** - Audio feature extraction
- **spaCy** - NLP processing
- **bcrypt** - Password hashing

### Frontend
- **React 18** - UI framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Vite** - Build tool
- **Recharts** - Data visualization
- **Lucide React** - Icons

### Database
- **SQLite** - Development (default)
- **PostgreSQL** - Production (optional)
- **asyncpg** - Async PostgreSQL driver
- **aiosqlite** - Async SQLite driver

---

## ✅ Test Results

### Comprehensive Test Summary (February 1, 2026)

```
================================================================================
CALLGUARD AI - COMPREHENSIVE RETEST
================================================================================

✓ API Health Check           - PASS
✓ Database Connection        - PASS (SQLite, 76 calls)
✓ ML Models Operational      - PASS (Whisper, NLP, Fraud, AI Voice)
✓ Audio Analysis             - PASS (Classification, Risk Score, Transcript)
✓ Text Analysis              - PASS (Fraud detection working)
✓ Call History & Filters     - PASS (All filters working)
✓ Call Details               - PASS (Full details with fraud indicators)
✓ Analytics Dashboard        - PASS (All 5 endpoints)
✓ Recent Alerts              - PASS (Severity levels working)
✓ Admin Rules CRUD           - PASS (Create, Read, Delete)
✓ User Authentication        - PASS (Register, Login, JWT)

================================================================================
SUMMARY: 33/34 Tests Passed (97.1%)
================================================================================
```

### Multilingual Audio Test Results

| Language | Samples | Detection Rate | False Positives |
|----------|---------|----------------|-----------------|
| English | 11 | 90.9% | 6.7% |
| Hindi | 4 | 50.0% | 0% |
| Tamil | 4 | 25.0% | 0% |
| Telugu | 4 | 50.0% | 0% |
| Spanish | 3 | 0%* | 0% |
| French | 2 | 0%* | 0% |
| German | 1 | 0%* | 0% |

*European languages have limited keyword database - transcription works, detection pending expansion.

---

## 📈 Performance

| Operation | Average Time |
|-----------|--------------|
| Health Check | < 50ms |
| Text Analysis | < 1s |
| Audio Upload (30s) | 5-10s |
| AI Voice Detection (1s audio) | 2-3s |
| Call List Query | < 100ms |
| Analytics Dashboard | < 200ms |

---

## 🛡️ Security Features

- ✅ JWT Authentication with bcrypt password hashing
- ✅ Input validation and sanitization
- ✅ Rate limiting on API endpoints
- ✅ Secure file handling with temp file cleanup
- ✅ CORS configuration for frontend access
- ✅ SQL injection prevention via ORM

---

## 🌐 Deployment

### Deploy to Production

The project is configured for easy deployment to **Vercel** (frontend) and **Render** (backend).

#### 1. Deploy Backend to Render

1. Go to [render.com](https://render.com/) and sign in with GitHub
2. Create new **Web Service**
3. Connect your **CallGuardAI** repository
4. Configure:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables:
   ```env
   DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/callguard
   SECRET_KEY=your-super-secret-key-min-32-chars
   WHISPER_MODEL=base
   LOG_LEVEL=INFO
   CORS_ORIGINS=https://your-vercel-app.vercel.app
   ```
6. Deploy and copy your backend URL

#### 2. Deploy Frontend to Vercel

1. Go to [vercel.com/new](https://vercel.com/new)
2. Import your **CallGuardAI** repository
3. Configure:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
4. Add environment variable:
   ```
   VITE_API_URL=https://your-backend-url.onrender.com
   ```
5. Deploy

#### 3. Update CORS

After deploying frontend, update `CORS_ORIGINS` in Render with your Vercel URL.

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🚀 How to Run the Project

### Prerequisites

- **Python 3.11+** - [Download](https://python.org/downloads/)
- **Node.js 18+** - [Download](https://nodejs.org/)
- **FFmpeg** - [Download](https://ffmpeg.org/download.html) (for audio processing)
- **Git** - [Download](https://git-scm.com/)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Bhanutejayadalla/CallGuardAI.git
cd CallGuardAI
```

### Step 2: Set Up Python Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install Python dependencies
cd backend
pip install -r requirements.txt
```

### Step 3: Configure Database (Optional)

**For SQLite (Default - No configuration needed):**
The database file `callguard.db` will be created automatically.

**For PostgreSQL:**
1. Install PostgreSQL
2. Create a database: `createdb callguard`
3. Create `.env` file in `backend/` folder:
```env
DATABASE_URL=postgresql+asyncpg://postgres:yourpassword@localhost:5432/callguard
SECRET_KEY=your-super-secret-key-change-in-production
```

### Step 4: Start Backend Server

```bash
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Expected output:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Started reloader process
🚀 Starting CallGuard AI Platform...
✅ Database initialized
✅ ML models loaded (Whisper, NLP, Fraud, AI Voice)
INFO:     Application startup complete.
```

### Step 5: Start Frontend Server

Open a **new terminal**:

```bash
cd frontend
npm install
npm run dev
```

Expected output:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: http://192.168.x.x:3000/
```

### Step 6: Access the Application

| Service | URL |
|---------|-----|
| **Frontend** | http://localhost:3000 |
| **Backend API** | http://localhost:8000 |
| **API Documentation** | http://localhost:8000/docs |
| **ReDoc** | http://localhost:8000/redoc |

### Step 7: Test the Application

```bash
# Run comprehensive tests
cd test_samples
python retest_all.py
```

### Quick Test Commands

```bash
# Test API health
curl http://localhost:8000/

# Test text analysis
curl -X POST "http://localhost:8000/api/v1/analyze/text?text=Your+bank+account+suspended"

# Get system stats
curl http://localhost:8000/api/v1/admin/stats
```

### Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 8000 in use | Kill process: `netstat -ano \| findstr :8000` then `taskkill /PID <pid> /F` |
| Module not found | Activate venv: `.venv\Scripts\activate` |
| Database error | Delete `callguard.db` and restart server |
| FFmpeg not found | Add FFmpeg to system PATH |
| CORS error | Check CORS_ORIGINS in backend config |

---

<p align="center">
  Made with ❤️ for the Hackathon<br>
  <a href="https://github.com/Bhanutejayadalla/CallGuardAI">⭐ Star us on GitHub</a>
</p>
