# 🎌 Benimaru - Anime Blog AI Agent Setup Guide

## ✅ Complete Setup Instructions

### Step 1: GitHub Secrets Configuration

Add these secrets to your GitHub repository:

1. Go to: **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret** for each one:

| Secret Name | Value |
|---|---|
| `WORDPRESS_URL` | `https://binnyverseanime.wordpress.com` |
| `WORDPRESS_USERNAME` | Your WordPress username |
| `WORDPRESS_APP_PASSWORD` | `Binnyverse@822` |
| `UNSPLASH_API_KEY` | `CaG_tDT8Pp8eudG08Xv9CVUljON1EiAPmylQ_brvyQ0` |
| `PEXELS_API_KEY` | `7ViqI3TlkfuE88d4N7BhY5GVAVcXLCCAuZsszcbbxD4BW5JV6R0rM8gO` |

### Step 2: WordPress Setup

1. Go to: https://binnyverseanime.wordpress.com/wp-admin/
2. Navigate to **Users** → **Your Profile**
3. Scroll to **Application Passwords**
4. Enter app name: "Benimaru Agent"
5. Click **Create Application Password**
6. Copy the generated password to `WORDPRESS_APP_PASSWORD` secret

### Step 3: Configure Content Calendar

Edit `content_calendar.json` with your post ideas:

```json
{
  "posts": [
    {
      "id": 1,
      "date": "2026-05-29",
      "time_slot": "morning",
      "title": "Your Post Title",
      "topic": "ranking_power",
      "category": "Category Name",
      "keywords": ["keyword1", "keyword2"],
      "status": "draft",
      "author": "Binny"
    }
  ]
}
```

## 📅 Post Topics

- **ranking_power**: "Top 10 Strongest Anime Characters"
- **character_comparison**: "Goku vs Superman"
- **theory**: "Controversial Theory About Power Systems"
- **news**: "Breaking Anime News or Announcement"

## ⏰ Automated Schedule

Posts will automatically be created at:
- ☀️ **8:00 AM UTC** - Morning post (Anime News)
- 🌤️ **2:00 PM UTC** - Afternoon post (Comparisons & Rankings)
- 🌙 **8:00 PM UTC** - Evening post (Theories & Discussions)

## 🔄 Workflow

1. **You provide**: Post title + topic in `content_calendar.json`
2. **Benimaru does**: 
   - Generates content
   - Fetches anime images (Unsplash, Pexels)
   - Optimizes SEO keywords & meta description
   - Creates draft post
3. **You review**: Post appears as draft in WordPress
4. **You publish**: Click publish when ready

## 💻 Local Development (Optional)

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env with your values (use the secrets)

# Run agent
python benimaru.py
```

## 🐛 Troubleshooting

### Posts not being created?
- Check GitHub Actions logs: **Actions** tab in your repo
- Verify all secrets are correctly set
- Check `benimaru.log` in workflow artifacts

### Images not loading?
- Verify Unsplash/Pexels API keys in secrets
- Check your API rate limits on those platforms

### WordPress connection error?
- Verify Application Password is correct
- Ensure WordPress site URL is exactly: `https://binnyverseanime.wordpress.com`

## ✨ Features

✅ **AI Content Generation** - Creates unique, SEO-optimized content  
✅ **Image Integration** - Fetches relevant images from Unsplash & Pexels  
✅ **SEO Optimization** - Auto-generates keywords, tags, meta descriptions  
✅ **Draft Creation** - Posts saved as drafts for your review  
✅ **Scheduled Publishing** - 3 posts daily at fixed times  
✅ **Anime Focused** - News, rankings, comparisons, theories  

## 📚 Content Categories

- Anime News
- Character Comparisons
- Anime Rankings
- Power System Analysis
- Theories & Discussions
- Anime Recommendations

---

**Enjoy your automated anime blog! 🎌**

For more details, check the README.md file.
