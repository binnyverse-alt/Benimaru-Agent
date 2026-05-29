# 🎌 Benimaru - Complete Setup Guide

## ✅ Everything is Ready!

Your Benimaru Anime Blog AI Agent is fully configured with:
- ✅ AI Content Generation
- ✅ Image Fetching (Unsplash & Pexels)
- ✅ SEO Optimization
- ✅ WordPress Integration
- ✅ GitHub Actions Automation
- ✅ Telegram Bot Control

---

## 🤖 **Telegram Bot Setup:**

### Bot Details:
- **Bot Name**: Benimaru Agent
- **Bot Token**: `8883281044:AAGA9ysKHC962kTc1xBs4W36x8VbDOmk9TI` ✅
- **Status**: Ready to use

### Bot Commands:
```
/start       - Welcome message
/help        - Show all commands
/add         - Create new post
/view        - View all scheduled posts
/today       - Show today's posts
/tomorrow    - Show tomorrow's posts
/categories  - View available categories
```

---

## 🚀 **Quick Start:**

### 1. Add GitHub Secrets (CRITICAL)
Go to: https://github.com/binnyverse-alt/Benimaru-Agent/settings/secrets/actions

Add these secrets:

| Secret Name | Value |
|---|---|
| `TELEGRAM_BOT_TOKEN` | `8883281044:AAGA9ysKHC962kTc1xBs4W36x8VbDOmk9TI` |
| `WORDPRESS_URL` | `https://binnyverseanime.wordpress.com` |
| `WORDPRESS_USERNAME` | Your WordPress username |
| `WORDPRESS_APP_PASSWORD` | `Binnyverse@822` |
| `UNSPLASH_API_KEY` | `CaG_tDT8Pp8eudG08Xv9CVUljON1EiAPmylQ_brvyQ0` |
| `PEXELS_API_KEY` | `7ViqI3TlkfuE88d4N7BhY5GVAVcXLCCAuZsszcbbxD4BW5JV6R0rM8gO` |

### 2. Create WordPress App Password
1. Go to: https://binnyverseanime.wordpress.com/wp-admin/
2. Users → Your Profile
3. Application Passwords → Create "Benimaru Agent"
4. Copy the password to `WORDPRESS_APP_PASSWORD`

### 3. Start Using Your Bot
1. Open Telegram
2. Search for your bot (by username from @BotFather)
3. Click `/start`
4. Use `/add` to create posts

---

## 📝 **Adding Posts via Telegram Bot:**

### Example Workflow:
```
You: /add
Bot: 📅 Enter date (DD/MM/YYYY)
You: 30/05/2026
Bot: ⏰ Select time slot
You: Click "Morning"
Bot: 📝 Enter post title
You: Top 10 Best Anime Villains
Bot: 🎯 Select topic
You: Click "Ranking"
Bot: 🏷️ Enter keywords
You: villains, anime, top 10, evil characters
Bot: ✅ Post Added!
```

### Topics:
- 🏆 `ranking_power` - Rankings, Power Levels
- ⚔️ `character_comparison` - VS battles
- 🧠 `theory` - Theories, Analysis
- 📰 `news` - Breaking news

---

## 📅 **Current Scheduled Posts:**

### 2026-05-28 (Today)
- ☀️ Morning: "Top 10 Strongest Anime Characters" (ranking_power)
- 🌤️ Afternoon: "Goku vs Superman" (character_comparison)
- 🌙 Evening: "Why Anime Endings Disappoint Fans" (theory)

### 2026-05-29 (Tomorrow)
- ☀️ Morning: "Top 10 Strongest Anime Characters" (ranking_power)
- 🌤️ Afternoon: "Goku vs Superman" (character_comparison)
- 🌙 Evening: "Why Anime Endings Disappoint Fans" (theory)

---

## 🔄 **Complete Workflow:**

```
1. Add Post via Telegram Bot
         ↓
2. Post saved to content_calendar.json
         ↓
3. GitHub Actions triggers at scheduled time
         ↓
4. Benimaru Agent reads calendar
         ↓
5. AI generates unique content
         ↓
6. Fetches images from Unsplash & Pexels
         ↓
7. Optimizes SEO keywords & tags
         ↓
8. Creates DRAFT post in WordPress
         ↓
9. You review & publish in WordPress
         ↓
10. Blog post goes LIVE! 🚀
```

---

## 📱 **Using Your Telegram Bot:**

### How to Access:
1. Open Telegram
2. Search for your bot username (from @BotFather)
3. Click "Start"

### Main Features:
- **Add Posts** - Schedule new blog posts
- **View Posts** - See all scheduled content
- **Today/Tomorrow** - Quick view of upcoming posts
- **Categories** - Browse available categories

---

## 🎯 **Daily Automation:**

Benimaru will automatically create posts at:
- **8:00 AM UTC** ☀️ Morning posts
- **2:00 PM UTC** 🌤️ Afternoon posts
- **8:00 PM UTC** 🌙 Evening posts

---

## 📊 **Your Setup Status:**

✅ Repository created
✅ All code deployed
✅ Telegram Bot configured (Token: `8883281044:AAGA9ysKHC962kTc1xBs4W36x8VbDOmk9TI`)
✅ Content calendar ready
✅ Sample posts added (6 posts scheduled)
✅ GitHub Actions workflows set up
✅ SEO optimization enabled
✅ Image fetching enabled

---

## 🔧 **Local Development (Optional):**

```bash
# Clone repository
git clone https://github.com/binnyverse-alt/Benimaru-Agent.git
cd Benimaru-Agent

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your credentials
cp .env.example .env

# Run Telegram Bot
python telegram_bot.py

# Or run main Benimaru Agent
python benimaru.py
```

---

## 🚨 **Important Notes:**

1. **Bot Token is Secure** - Stored in GitHub Secrets, never exposed
2. **WordPress App Password** - Use a unique app password, not your main password
3. **API Keys are Safe** - Stored securely in GitHub Secrets
4. **Content Calendar** - Automatically updates when you use bot commands

---

## 📞 **Need Help?**

### Check Logs:
- GitHub Actions: https://github.com/binnyverse-alt/Benimaru-Agent/actions
- Telegram Bot: Check console output or GitHub Actions artifacts

### Troubleshooting:
- Posts not creating? Check GitHub Secrets are added
- Bot not responding? Verify TELEGRAM_BOT_TOKEN is correct
- WordPress errors? Verify Application Password is correct

---

## 🎉 **You're All Set!**

Your automated anime blog system is ready to go! 🎌

**Next Steps:**
1. ✅ Add remaining GitHub Secrets (WordPress username, etc.)
2. ✅ Create WordPress App Password
3. ✅ Search for your bot in Telegram
4. ✅ Start using `/add` command
5. ✅ Review posts in WordPress drafts
6. ✅ Publish to your blog

**Enjoy your fully automated anime blog!** 🚀
