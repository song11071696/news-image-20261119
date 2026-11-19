# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/song11071696/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/song11071696/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up Thursday, 19 November 2026: the first-ever meeting of Trump, Xi and Putin, held in Shenzhen; GTA VI launching worldwide; Anthropic's first day on the Nasdaq, opening at $83 under the ticker ANT; Hakeem Jeffries winning the Speaker nomination 251–11; a third strike on the Crimean Bridge; and the World Court's verdict in the Rohingya case. A ticker along the bottom carries the record $190.4M Van Gogh sale, Cyclone Akvan bearing down on India, and the mine strikes on tankers in the Strait of Hormuz. The background is an AI-generated world map with no text at all — every headline, date and label was drawn on top with PIL.

## Run it

```sh
python3 main.py
```

That writes the bundled 1024×1024 image to `/output/entry.png`. The program uses only the Python standard library, makes no network requests, and running it twice produces byte-identical output.

## Verification

`entry.png` is 1024×1024 and its sha256 is `74df631dbccdb46b2805e7387cb6078aecf858389b50fbdf7e0ecbf1a75a91cd`. The program checks the copy after writing it and fails loudly if the size or content differs.

The bounty pays $250 in USDC, shared by the 50 best-ranked entries: $50 for first place, $30 for second, $15 for third, $5 each for places 4–10, and $3 each for places 11–50.
