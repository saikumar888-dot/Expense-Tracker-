# Deploy on Netlify (Free)

## Quick Deploy Steps:

### Method 1: Drag & Drop (Easiest)
1. Go to https://app.netlify.com/drop
2. Drag and drop your project folder (or select the folder)
3. Your site will be live in seconds!

### Method 2: Connect GitHub (Recommended)
1. Go to https://app.netlify.com/
2. Click "New site from Git"
3. Click "GitHub" and authorize Netlify
4. Select repository: `saikumar888-dot/Expense-Tracker-`
5. Build settings:
   - Build command: (leave empty)
   - Publish directory: `.` (current directory)
6. Click "Deploy site"

### Method 3: Using Netlify CLI
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login to Netlify
netlify login

# Deploy
netlify deploy --prod
```

## Your Live Site
Once deployed, you'll get a URL like:
- `https://your-site-name.netlify.app`

## Features Included:
✅ Fully functional expense tracker
✅ Add/delete transactions
✅ Real-time balance calculation
✅ Responsive design
✅ Works offline (no backend required)

## Custom Domain (Optional)
1. In Netlify dashboard, go to Domain settings
2. Click "Add custom domain"
3. Point your domain DNS to Netlify

---

**All files are ready to deploy!** Just connect your GitHub repo to Netlify.
