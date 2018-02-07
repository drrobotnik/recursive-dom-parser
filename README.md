# recursive-dom-parser
Recursively parse dom objects to identify repeated patterns

## What does this do?

The idea here is to traverse a scraped website and parse each html file for each dom element. By parsing through each page you can identify re-used elements. Potentially ripe to be made into components.

`python soup.py --path="../../scraped-site/" --element=div > div.html`
