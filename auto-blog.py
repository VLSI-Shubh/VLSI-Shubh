#!/usr/bin/env python3
"""
Automated Blog Post Generator for VLSI Portfolio
Converts markdown to HTML in the SAME folder

Usage: python auto-blog.py <folder-path>
Example: python auto-blog.py blog/posts/rtl-design-tips
"""

import sys
import subprocess
import os
from datetime import datetime


def create_blog_post(folder_path):
    """
    Finds .md file in folder, converts to index.html in SAME folder

    Args:
        folder_path: Path to folder containing your .md file
                    (e.g., "blog/posts/rtl-design-tips")
    """

    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found!")
        print(f"Tip: Create it first: mkdir -p {folder_path}")
        sys.exit(1)

    # Find .md file in folder
    md_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]

    if len(md_files) == 0:
        print(f"Error: No .md file found in '{folder_path}'!")
        print(f"Tip: Create one first: touch {folder_path}/blog.md")
        sys.exit(1)

    if len(md_files) > 1:
        print(f"Warning: Multiple .md files found. Using: {md_files[0]}")

    markdown_file = os.path.join(folder_path, md_files[0])
    print(f"Found markdown: {markdown_file}")

    # Extract title from folder name (e.g., "rtl-design-tips" → "RTL Design Tips")
    folder_name = os.path.basename(folder_path)
    title = folder_name.replace("-", " ").title()

    # Ask user if they want to customize title
    print(f"Auto-generated title: '{title}'")
    custom_title = input("Press Enter to use this, or type a new title: ").strip()
    if custom_title:
        title = custom_title

    # 1. Convert Markdown to HTML using Pandoc
    print("Converting to HTML...")
    temp_html = os.path.join(folder_path, "_temp.html")

    try:
        subprocess.run(["pandoc", markdown_file, "-o", temp_html], check=True)
    except FileNotFoundError:
        print("Error: Pandoc not found! Install it with:")
        print("  Mac: brew install pandoc")
        print("  Ubuntu: sudo apt install pandoc")
        print("  Windows: Download from https://pandoc.org/installing.html")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print(f"Error: Failed to convert {markdown_file}")
        sys.exit(1)

    # 2. Read converted HTML content
    with open(temp_html, "r", encoding="utf-8") as f:
        content = f.read()

    # 3. Get current date
    current_date = datetime.now().strftime("%B %d, %Y")

    # 4. Calculate relative path to root (for CSS/JS links)
    depth = folder_path.count("/") - 1  # blog/posts/name = 2 levels deep
    root_path = "../" * depth

    # 5. Wrap in portfolio template
    wrapped_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title} | Shubham Upadhyay</title>

<meta name="description" content="{title} - VLSI Design Blog"/>
<meta property="og:title" content="{title}"/>
<meta property="og:type" content="article"/>

<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>

<!-- Portfolio CSS -->
<link rel="stylesheet" href="{root_path}css/style.css"/>

<!-- Blog-specific styles -->
<style>
  .blog-post {{
    max-width: 800px;
    margin: 0 auto;
    padding: calc(var(--nav-h) + 3rem) 1.5rem 4rem;
  }}

  .blog-header {{
    margin-bottom: 3rem;
    text-align: center;
  }}

  .blog-title {{
    font-size: clamp(2rem, 5vw, 3rem);
    margin-bottom: 1rem;
    color: var(--heading);
  }}

  .blog-meta {{
    color: var(--muted);
    font-size: 0.95rem;
  }}

  .blog-content {{
    line-height: 1.8;
    color: var(--text);
  }}

  .blog-content h1 {{
    font-size: 2rem;
    margin: 2.5rem 0 1rem;
    color: var(--heading);
  }}

  .blog-content h2 {{
    font-size: 1.6rem;
    margin: 2rem 0 1rem;
    color: var(--heading);
  }}

  .blog-content h3 {{
    font-size: 1.3rem;
    margin: 1.5rem 0 0.75rem;
    color: var(--heading);
  }}

  .blog-content p {{
    margin-bottom: 1.25rem;
  }}

  .blog-content ul, .blog-content ol {{
    margin: 1rem 0 1.5rem 2rem;
  }}

  .blog-content li {{
    margin-bottom: 0.5rem;
  }}

  .blog-content code {{
    background: rgba(6,182,212,.15);
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-family: 'Courier New', monospace;
    font-size: 0.9em;
    color: var(--accent);
  }}

  .blog-content pre {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1.5rem;
    overflow-x: auto;
    margin: 1.5rem 0;
  }}

  .blog-content pre code {{
    background: none;
    padding: 0;
    color: var(--text);
  }}

  .blog-content blockquote {{
    border-left: 4px solid var(--accent);
    padding-left: 1.5rem;
    margin: 1.5rem 0;
    color: var(--muted);
    font-style: italic;
  }}

  .blog-content img {{
    max-width: 100%;
    height: auto;
    border-radius: 12px;
    margin: 2rem 0;
  }}

  .blog-content a {{
    color: var(--accent);
    text-decoration: underline;
  }}

  .back-button {{
    display: inline-block;
    margin-top: 3rem;
    padding: 0.75rem 1.5rem;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    color: var(--heading);
    text-decoration: none;
    transition: all var(--dur) var(--easing);
  }}

  .back-button:hover {{
    background: rgba(6,182,212,.1);
    transform: translateX(-3px);
  }}
</style>
</head>

<body>
  <!-- Navigation -->
  <nav aria-label="Primary" class="nav-wrap">
    <div class="nav-container">
      <div class="nav-brand">
        <a href="{root_path}index.html" style="color: var(--heading); text-decoration: none;">Shubham Upadhyay</a>
      </div>
      <div class="nav-controls">
        <a href="{root_path}blog/" class="btn outline" style="font-size: 0.9rem; padding: 0.5rem 1rem;">← All Posts</a>
      </div>
    </div>
  </nav>

  <!-- Blog Post -->
  <main class="blog-post">
    <header class="blog-header">
      <h1 class="blog-title">{title}</h1>
      <p class="blog-meta">Published on {current_date}</p>
    </header>

    <article class="blog-content">
{content}
    </article>

    <a href="{root_path}blog/" class="back-button">← Back to All Posts</a>
  </main>

  <!-- Footer -->
  <footer style="text-align:center; padding:2rem 1rem; color:var(--muted); border-top:1px solid var(--border); margin-top: 3rem;">
    <p>&copy; 2025 Shubham Upadhyay. All rights reserved.</p>
  </footer>

  <!-- Go to Top Button -->
  <button class="go-to-top" id="goToTop" aria-label="Go to top">↑</button>

  <!-- JavaScript -->
  <script src="{root_path}js/script.js"></script>
</body>
</html>"""

    # 6. Save as index.html in SAME folder
    output_file = os.path.join(folder_path, "index.html")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(wrapped_html)

    # 7. Cleanup temp file
    os.remove(temp_html)

    # 8. Success message
    print("\nBlog post created successfully!")
    print(f"  Markdown: {markdown_file}")
    print(f"  HTML:     {output_file}")
    print(f"  URL:      /{folder_path}/")
    print("\nNext steps:")
    print(f"  1. git add {folder_path}")
    print(f"  2. git commit -m 'Add blog post: {title}'")
    print("  3. git push")


def print_usage():
    print("Usage: python auto-blog.py <folder-path>")
    print("\nWorkflow:")
    print("  1. Create folder: mkdir -p blog/posts/rtl-design-tips")
    print("  2. Write markdown: blog/posts/rtl-design-tips/blog1.md")
    print("  3. Run script: python auto-blog.py blog/posts/rtl-design-tips")
    print("  4. Result: blog/posts/rtl-design-tips/index.html")
    print("\nExamples:")
    print("  python auto-blog.py blog/posts/rtl-design-tips")
    print("  python auto-blog.py blog/posts/fifo-deep-dive")
    print("  python auto-blog.py blog/posts/verification-basics")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Wrong number of arguments!\n")
        print_usage()
        sys.exit(1)

    folder_path = sys.argv[1].rstrip("/")  # Remove trailing slash if present
    create_blog_post(folder_path)
