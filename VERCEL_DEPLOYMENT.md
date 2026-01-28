# CallGuard AI - Vercel Deployment Guide

## 🚀 Quick Deploy to Vercel

### Prerequisites
- GitHub account with the repository
- Vercel account (free tier works)
- Backend API deployed separately (Railway, Render, or similar)

---

## Step 1: Deploy Backend (Choose One)

### Option A: Railway.app (Recommended)
1. Go to [Railway.app](https://railway.app/)
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select `CallGuardAI` repository
5. Choose `backend` as root directory
6. Add environment variables:
   ```
   DATABASE_URL=sqlite:///./callguard.db
   JWT_SECRET=your-super-secret-key-change-this
   CORS_ORIGINS=https://your-vercel-app.vercel.app
   WHISPER_MODEL=base
   LOG_LEVEL=INFO
   ```
7. Deploy and note your backend URL (e.g., `https://callguard-api.railway.app`)

### Option B: Render.com
1. Go to [Render.com](https://render.com/)
2. Create new "Web Service"
3. Connect GitHub repository
4. Settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Root Directory**: `backend`
5. Add same environment variables as above
6. Deploy and note your backend URL

### Option C: Keep Backend Local (Development Only)
- Use a tunnel service like [ngrok](https://ngrok.com/):
  ```powershell
  ngrok http 8000
  ```
- Note the HTTPS URL provided by ngrok

---

## Step 2: Deploy Frontend to Vercel

### Method 1: Through Vercel Dashboard (Easiest)

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click "Add New Project"
3. Import your `CallGuardAI` repository
4. Configure:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
5. Add Environment Variables:
   ```
   VITE_API_URL=https://your-backend-url.com
   VITE_APP_ENV=production
   VITE_ENABLE_AUTH=true
   VITE_ENABLE_ANALYTICS=true
   ```
6. Click "Deploy"

### Method 2: Through Vercel CLI

```powershell
# Install Vercel CLI
npm install -g vercel

# Navigate to project
cd D:\hackathon

# Login to Vercel
vercel login

# Deploy
vercel --prod
```

When prompted:
- **Set up and deploy**: Yes
- **Which scope**: Your account
- **Link to existing project**: No
- **Project name**: callguard-ai
- **Directory**: `frontend`
- **Override settings**: No

---

## Step 3: Configure Environment Variables

### In Vercel Dashboard:

1. Go to your project → Settings → Environment Variables
2. Add the following:

| Variable | Value | Environment |
|----------|-------|-------------|
| `VITE_API_URL` | `https://your-backend-url.com` | Production |
| `VITE_APP_ENV` | `production` | Production |
| `VITE_ENABLE_AUTH` | `true` | Production |
| `VITE_ENABLE_ANALYTICS` | `true` | Production |

3. Save and redeploy

---

## Step 4: Update Backend CORS Settings

Update your backend's `CORS_ORIGINS` to include your Vercel URL:

**Railway/Render:**
```
CORS_ORIGINS=https://your-app.vercel.app,http://localhost:3000
```

**Local backend (config file):**
```python
# backend/app/core/config.py
CORS_ORIGINS = [
    "http://localhost:3000",
    "https://your-app.vercel.app"
]
```

---

## Step 5: Test Your Deployment

1. Visit your Vercel URL: `https://your-app.vercel.app`
2. Try the AI Voice Detection feature
3. Upload a test audio file
4. Check the console for any errors

---

## 🏠 Local Development Setup

### Start Backend (Terminal 1):
```powershell
# Add FFmpeg to PATH
$ffmpegPath = "C:\Users\Venkata Yadalla\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin"
$env:PATH = "$ffmpegPath;$env:PATH"

# Start backend
cd D:\hackathon\backend
D:\hackathon\.venv\Scripts\python.exe -m uvicorn main:app --host 0.0.0.0 --port 8000
```

### Start Frontend (Terminal 2):
```powershell
cd D:\hackathon\frontend
npm run dev
```

Access at: `http://localhost:3000`

---

## 📝 Deployment Checklist

### Before Deploying:
- [ ] Backend is deployed and accessible
- [ ] FFmpeg is available (for audio processing)
- [ ] Environment variables are configured
- [ ] CORS is properly configured
- [ ] Database is set up (SQLite or PostgreSQL)

### After Deploying:
- [ ] Vercel deployment succeeded
- [ ] Frontend loads without errors
- [ ] API calls work correctly
- [ ] File uploads work
- [ ] Audio analysis works
- [ ] All 5 languages work
- [ ] WebSocket connections work (if using real-time features)

---

## 🔧 Troubleshooting

### Issue: "Failed to fetch" or CORS errors
**Solution:** Update backend CORS_ORIGINS to include your Vercel URL

### Issue: "Cannot read environment variable"
**Solution:** Ensure all VITE_ variables are set in Vercel dashboard

### Issue: Audio upload fails
**Solution:** Check backend logs, ensure FFmpeg is installed on backend server

### Issue: Build fails on Vercel
**Solution:** Check `package.json` and ensure all dependencies are listed

### Issue: 404 on page refresh
**Solution:** Vercel handles this automatically with SPA, but verify `vercel.json` routing

---

## 🔄 Update/Redeploy

### Automatic (Recommended):
- Push changes to GitHub `vercel-friendly` branch
- Vercel automatically redeploys

### Manual:
```powershell
cd D:\hackathon
vercel --prod
```

---

## 📊 Monitoring

- **Vercel Analytics**: Built-in analytics in Vercel dashboard
- **Logs**: View real-time logs in Vercel dashboard
- **Performance**: Check Web Vitals in Vercel

---

## 💡 Tips

1. **Free Tier Limits:**
   - Vercel: 100 GB bandwidth/month
   - Railway: $5 free credit/month
   - Render: 750 hours/month

2. **Optimize Build:**
   - Enable build caching
   - Use environment-specific builds
   - Minimize bundle size

3. **Security:**
   - Never commit `.env` files
   - Use environment variables for secrets
   - Enable HTTPS only

4. **Performance:**
   - Enable CDN caching
   - Optimize images
   - Use lazy loading

---

## 🌐 Useful Links

- [Vercel Documentation](https://vercel.com/docs)
- [Railway Documentation](https://docs.railway.app/)
- [Render Documentation](https://render.com/docs)
- [Vite Environment Variables](https://vitejs.dev/guide/env-and-mode.html)

---

**Your deployment URLs:**
- Frontend: `https://your-app.vercel.app`
- Backend: `https://your-backend.railway.app` (or your chosen platform)
- Repository: https://github.com/Bhanutejayadalla/CallGuardAI/tree/vercel-friendly
