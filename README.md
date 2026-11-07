# CVE-2026-113593 Proof of Concept (POC)

- https://www.tenable.com/cve/CVE-2026-113593

Long story short. In specific versions of Django there is a problem with cache mechanisms. I tried this with `LocMemCache`. Basically it's about creating keys in keys-values cache store. That produces problem with varying headers used in requests when cache is used. The same problem occurs with other cache backends like `redis`. That's because the issue occurs on Django layer, when creating keys.

To cache some view we use:

```python
@cache_page(20)
```

But when important header comes in, we can invalidate cache based on that information:

```python
@vary_on_headers('X-USER-ID')
```

Based on that, when the response depends on specific request header, we can tell Django to vary the cache key based on that header.
The problem occurs because the django doesn't differ header with value `''` and no header at all.

That is why we witness <mark>Cross-User Data Leakage</mark>


# Disclaimer

It's `LOW SEVERITY` CVE but in specific situations it could lead to data disclousure and could be potentially dangerous.

|CVSS version|Score|
|----|----|
|v2|2.6|
|v3|3.1|
|v4|2.3|
