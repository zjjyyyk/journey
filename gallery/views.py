import os
import re
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.core.paginator import Paginator

BASE_MEDIA = Path(settings.MEDIA_ROOT)

def slugify(s):
    return re.sub(r'[^a-z0-9]+', '_', s.lower())

def get_periods():
    media_path = settings.MEDIA_ROOT
    periods = []
    for period_name in os.listdir(media_path):
        if os.path.isdir(os.path.join(media_path, period_name)):
            slug = slugify(period_name)
            periods.append({'slug': slug})
    return periods

def index(request):
    media_path = settings.MEDIA_ROOT
    periods = []

    for period_name in os.listdir(media_path):
        period_dir = os.path.join(media_path, period_name)
        if os.path.isdir(period_dir):
            first_photo = None
            for loc_person in os.listdir(period_dir):
                subdir = os.path.join(period_dir, loc_person)
                if os.path.isdir(subdir):
                    photos = [f for f in os.listdir(subdir) if f.lower().endswith(('.jpg', '.png'))]
                    if photos:
                        first_photo = f"{settings.MEDIA_URL}{period_name}/{loc_person}/{photos[0]}"
                        break

            rep = first_photo or "/static/img/placeholder.jpg"
            if rep.startswith('/'):
                rep = rep[1:]

            periods.append({
                "name": period_name,
                "slug": slugify(period_name),
                "rep": rep
            })

    return render(request, 'index.html', {'periods': periods})

def period_view(request, period):
    period_dir = BASE_MEDIA / period
    if not period_dir.exists() or not period_dir.is_dir():
        return render(request, 'period_not_found.html', {'period': period})

    groups = []
    for subgroup in sorted([d for d in period_dir.iterdir() if d.is_dir()]):
        imgs = []
        for f in sorted(subgroup.iterdir()):
            if f.is_file() and f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
                rel = os.path.relpath(str(f), settings.MEDIA_ROOT)
                thumb = os.path.join(os.path.dirname(rel), 'thumbs', os.path.splitext(os.path.basename(rel))[0] + '_thumb.jpg')
                url = settings.MEDIA_URL + rel.replace('\\','/')
                if url.startswith('/'):
                    url = url[1:]

                thumb_url = settings.MEDIA_URL + thumb.replace('\\','/')
                if thumb_url.startswith('/'):
                    thumb_url = thumb_url[1:]

                imgs.append({'url': url, 'thumb': thumb_url, 'name': os.path.basename(rel)})
        if imgs:
            groups.append({'name': subgroup.name, 'images': imgs})

    flat = []
    for g in groups:
        for im in g['images']:
            flat.append({'group': g['name'], 'url': im['url'], 'thumb': im['thumb'], 'name': im['name']})

    per_page = int(request.GET.get('per_page', 50))
    page_number = request.GET.get('page', 1)
    paginator = Paginator(flat, per_page)
    page_obj = paginator.get_page(page_number)

    return render(request, 'period.html', {'period': period, 'page_obj': page_obj, 'paginator': paginator})
