# checkstatuslistofurls
Checks the status of a list of URLs

# Requirements
Python packages:
* requests
* fake-UserAgent

# Usage
```python3 main.py```

# Notes
The web is the wild west. So just because status code 200 is returned doesn't mean the page you want exists. eg. pages that give you 200 to send you to their normal webpage that says '404'; If the domain doesn't exist, it will be sent to the bad list, but this domain might just be inside China and if you're outside China you can't access it. Double check what the case is with your browser.
