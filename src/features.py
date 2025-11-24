import re
import math
from urllib.parse import urlparse, parse_qs

SHORTENERS = set([
 "bit.ly","tinyurl.com","goo.gl","ow.ly","t.co","buff.ly","adf.ly","bitly.com"
])

def is_ip(host):
    return bool(re.match(r'^\d{1,3}(\.\d{1,3}){3}$', host))

def entropy(s):
    if not s:
        return 0.0
    probs = [float(s.count(c)) / len(s) for c in set(s)]
    return -sum(p * math.log2(p) for p in probs)

def count_digits(s):
    return sum(c.isdigit() for c in s)

def has_suspicious_word(s):
    words = ["secure","account","update","verify","login","confirm","bank","ebay","paypal"]
    s2 = s.lower()
    return int(any(w in s2 for w in words))

def extract_features(url):
    try:
        u = url.strip()
        p = urlparse(u if "://" in u else "http://"+u)
        host = p.hostname or ""
        path = p.path or ""
        query = p.query or ""
    except Exception:
        host = ""
        path = ""
        query = ""
        u = url

    features = {}
    features["url_length"] = len(u)
    features["num_dots"] = u.count(".")
    features["num_hyphens"] = u.count("-")
    features["num_at"] = u.count("@")
    features["has_ip"] = int(is_ip(host))
    features["num_digits"] = count_digits(u)
    features["num_subdirs"] = path.count("/")
    features["suspicious_word"] = has_suspicious_word(u)
    features["https"] = int(u.lower().startswith("https"))
    features["shortener"] = int(host in SHORTENERS)
    features["entropy"] = entropy(u)
    features["has_www"] = int(host.startswith("www"))
    features["tld_length"] = len(host.split(".")[-1]) if "." in host else 0
    features["path_length"] = len(path)
    features["num_query_params"] = len(parse_qs(query))
    return features

def extract_features_series(urls):
    rows = [extract_features(u) for u in urls]
    import pandas as pd
    return pd.DataFrame(rows)
