FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y --no-install-recommends wget ca-certificates libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libxkbcommon0 libxcomposite1 libxrandr2 libxdamage1 libgbm1 libasound2 libpangocairo-1.0-0 libxshmfence1 libgtk-3-0 libdrm2 libxcb1 libx11-xcb1 \
    && pip install --no-cache-dir -r requirements.txt \
    && python -m playwright install --with-deps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["pytest", "--alluredir=/allure-results"]
