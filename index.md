---
layout: default
---

# GEO Array Digest

Welcome to the Geo Array Digest resource, or "GAD" for short!

<h1>Latest Digests:</h1>

<ul>
  {% for post in site.posts %}
    <li>
      <h2><a href="/geoarraydigest/{{ post.url }}">{{ post.title }}</a></h2>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>