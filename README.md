# 🎉 Jar of Joy

A beautiful web application for capturing and revisiting moments of gratitude, joy, and inspiration throughout the year.

## ✨ Features

- **Dashboard**: View your virtual jar filling up with sparks of joy
- **Add Sparks**: Capture memories, quotes, gratitude moments, and achievements
- **Reveal**: Randomly rediscover past entries for moments of reflection
- **Collection**: Browse and search through all your saved sparks
- **Multilingual**: Full support for English and Slovak languages
- **Local Storage**: All data stored securely in your browser
- **Backup & Restore**: Export and import your data as JSON files

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/jar-of-joy.git
cd jar-of-joy
```

2. Install dependencies:
```bash
pip install jinja2
```

3. Build the site:
```bash
python build.py
```

4. Open `docs/index.html` in your browser or deploy to GitHub Pages.

## 📦 Deployment to GitHub Pages

1. Push your repository to GitHub
2. Go to repository Settings → Pages
3. Set Source to "Deploy from a branch"
4. Select branch: `main` and folder: `/docs`
5. Save and wait for deployment
6. Your site will be available at `https://yourusername.github.io/jar-of-joy/`

## 💾 Data Backup

Your data is stored locally in your browser's localStorage. To backup your data:

1. Click on your profile icon in the header
2. Go to Settings
3. Click "Export Data" to download a JSON backup file
4. Store this file safely

To restore your data:
1. Click "Import Data" in Settings
2. Select your backup JSON file
3. Choose to merge with existing data or replace all data

### Manual Backup

You can also manually backup your data by:
1. Open browser Developer Tools (F12)
2. Go to Application/Storage → Local Storage
3. Copy the value of `jarOfJoy_sparks`
4. Save it to a text file

## 🌍 Language Support

The app supports:
- English (default)
- Slovak (Slovenčina)

Switch languages using the dropdown in the header.

## 🛠️ Development

### Project Structure

```
jar-of-joy/
├── src/
│   ├── templates/          # Jinja2 HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── add.html
│   │   ├── reveal.html
│   │   └── collection.html
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── app.js
│   │   └── images/
│   │       └── favicon.svg
│   └── config.py           # Multilingual configuration
├── docs/                   # Generated static site
├── build.py               # Build script
└── README.md
```

### Building

Run the build script to generate the static site:
```bash
python build.py
```

This will:
- Generate HTML files for all languages
- Copy static assets to the docs folder
- Create language-specific directories

### Adding New Languages

1. Edit `src/config.py`
2. Add a new language entry to the `LANGUAGES` dictionary
3. Provide all translations
4. Run `python build.py`

## 🎨 Customization

### Colors

Edit CSS variables in `src/static/css/styles.css`:
```css
:root {
    --primary: #FF6B35;
    --secondary: #FFA726;
    --tertiary: #26A69A;
    /* ... */
}
```

### Quotes

Add daily inspirational quotes in `src/config.py`:
```python
DAILY_QUOTES = [
    {
        'en': {'quote': '...', 'author': '...'},
        'sk': {'quote': '...', 'author': '...'}
    }
]
```

## 📱 Browser Compatibility

- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support
- Mobile browsers: ✅ Responsive design

## 🔒 Privacy

- All data is stored locally in your browser
- No data is sent to any server
- No tracking or analytics
- Your data stays with you

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 💖 Acknowledgments

- Built with [Pure.css](https://purecss.io/)
- Icons from [Google Material Symbols](https://fonts.google.com/icons)
- Fonts from [Google Fonts](https://fonts.google.com/)

---

Made with ❤️ for spreading joy