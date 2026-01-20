# Railway Deployment Guide

## 1. Fast Deployment
1. **Push** this code to your **GitHub** repository.
2. Go to **[Railway.app](https://railway.app)**.
3. Click **"New Project"** -> **"Deploy from GitHub repo"**.
4. Select your repository.
5. Click **"Deploy Now"**.

## 2. Environment Variables
Once deployed, go to **Settings -> Variables** in Railway.

### ✅ Required
| Variable | Value (Example) |
|----------|-----------------|
| `MONGODB_URI` | `mongodb+srv://user:pass@...` (Your MongoDB connection string) |
| `SECRET_KEY` | (Generate a random string) |
| `FLASK_ENV` | `production` |

### ⚠ Optional (Email Features)
*If you don't add these, the app will work but emails won't be sent.*
| Variable | Value |
|----------|-------|
| `EMAIL_USERNAME` | `your-email@gmail.com` |
| `EMAIL_PASSWORD` | `your-app-password` |
| `WEBHOOK_URL` | `https://...` (Your N8N webhook) |

## 3. Automatic Updates (CI/CD)
- **CI (Testing)**: A standard GitHub Actions pipeline has been added in `.github/workflows/ci.yml`. It will strictly check your code for errors on every push.
- **CD (Deployment)**: Railway will **automatically redeploy** your app whenever you push changes to the `main` branch. No extra setup needed!

## 4. Troubleshooting
- If deployment fails, check the **"Deploy Logs"** in Railway.
- If the app starts but errors occur, check the **"Service Logs"**.
