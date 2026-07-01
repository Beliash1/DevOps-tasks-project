# საბაზისო image — სტაბილური Python ვერსია (არა 3.14, რომელიც ლოკალურად გაქვს)
FROM python:3.11-slim

# სამუშაო დირექტორია container-ის შიგნით
WORKDIR /app

# სისტემური დამოკიდებულებები psycopg2-ისთვის
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# jერ მხოლოდ requirements.txt ვაკოპირებთ (ეს Docker-ის caching ოპტიმიზაციაა)
COPY requirements.txt .

# Python პაკეტების დაინსტალირება
RUN pip install --no-cache-dir -r requirements.txt

# დანარჩენი კოდის კოპირება
COPY . .

# Non-root user-ის შექმნა (security best practice)
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# პორტი, რომელზეც აპლიკაცია იმუშავებს
EXPOSE 5000

# გაშვების ბრძანება — production-ready სერვერით (gunicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]