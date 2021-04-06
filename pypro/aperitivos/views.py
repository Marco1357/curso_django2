from django.shortcuts import render

videos = [
      {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivação', 'youtube_id': '2aYplgJrPDU'},
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html')


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
