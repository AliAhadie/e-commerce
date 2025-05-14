FROM python:3.12-alpine

LABEL maintainer="ali.ahadi.official@gmail.com"

# ایجاد پوشه کاری
WORKDIR /usr/src/app

# کپی فایل های مورد نیاز
COPY ./requirements.txt .

ENV PYTHONUNBUFFERED=1

# نصب پکیج‌ها
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    # تغییر دسترسی به پوشه پروژه برای django-user
    chown -R django-user:django-user /usr/src/app

# تنظیمات برای اجرای پروژه با کاربر django-user
USER django-user

# کپی پروژه به داخل کانتینر
COPY ./core .
