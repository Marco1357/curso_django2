from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao':{'titulo': 'Video Aperitivo: Motivação', 'youtube_id': '2aYplgJrPDU'},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
