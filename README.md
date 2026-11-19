# 19 November in One Image

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/song11071696/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/song11071696/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

This entry squeezes 19 November's world news into a single 1024x1024 image: the first-ever Trump-Xi-Putin trilateral meeting in Shenzhen leads the page, alongside the worldwide launch of GTA VI, Anthropic's $83 Nasdaq debut trading as ANT, Hakeem Jeffries being nominated Speaker by 251 votes to 11, a third strike on the Crimean Bridge, and the World Court's verdict on the Rohingya case. A ticker along the bottom carries the day's other big numbers and names — the record $190.4M Van Gogh sale, Cyclone Akvan, and the tanker mine strikes in the Strait of Hormuz. The backdrop is an AI-generated world map with no text on it at all; every headline was laid over it afterwards with PIL, so the picture reads cleanly at a glance.

## Run it

```bash
python3 main.py
```

That writes the bundled 1024x1024 image to `/output/entry.png`. The script uses only the Python standard library and makes no network calls. Run it twice and the output is byte-identical both times.

## Verification

Check the bundled image against its known hash before running:

```bash
sha256sum entry.png
```

Expected SHA-256 for `entry.png`:

```
74df631dbccdb46b2805e7387cb6078aecf858389b50fbdf7e0ecbf1a75a91cd
```

`main.py` re-checks the same hash, the file size, and the PNG magic bytes on every run, and exits non-zero if the copy in `/output/entry.png` does not match.

## Prize

This entry is for the make.fun news-image-20261119 bounty, a $250 prize pool split $50 / $30 / $15 for the top three, $5 for places 4–10, and $3 for places 11–50.
