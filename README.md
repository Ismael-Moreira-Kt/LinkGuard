# LinkGuard
**LinkGuard** is a tool for checking broken links on a website. The script scans a web page, extracts all the links found and checks that they are working correctly.

## Features
- **Link check:** Identifies broken links (HTTP status other than 200) on a web page.
- **Extract Links:** Collects all links found in `<a>` tags with the `href` attribute.

## Requirements
- Python 3.6 or higher;

## Installation
1. Clone the repository:
```bash
git clone https://github.com/seuusuario/LinkGuard.git
cd LinkGuard
```

2. Install the necessary dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```