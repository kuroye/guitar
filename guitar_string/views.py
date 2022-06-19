from django.shortcuts import render, redirect, reverse
from .models import Song


# Create your views here.

def song(request):
    # song = Song.objects.create(name='晴天')
    if request.method == 'GET':
        song = Song.objects.all()
        string_num = [6, 5, 4, 3, 2, 1]

        s1 = ['E4', 'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'F4', 'F#4', 'G4', 'G#4']
        s2 = ['B3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'C4', 'C#4', 'D4', 'D#4']
        s3 = ['G3', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G#3', 'A3', 'A#3', 'B3']
        s4 = ['D3', 'G2', 'G#2', 'A2', 'A#2', 'B2', 'C3', 'C#3', 'D#3', 'E3', 'F3', 'F#3']
        s5 = ['A2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A#2', 'B2', 'C3', 'C#3']
        s6 = ['E2', 'A1', 'A#1', 'B1', 'C2', 'C#2', 'D2', 'D#2', 'F2', 'F#2', 'G2', 'G#2']

        sound = {

            '6': s6,
            '5': s5,
            '4': s4,
            '3': s3,
            '2': s2,
            '1': s1,

        }

        return render(request, 'song.html', context={'songs': song,
                                                      'string_num': string_num,
                                                      'sound': sound})

    if request.method == 'POST':

        do = request.POST.get('do')

        if do == 'add':
            name = request.POST.get('name')
            guitar_string = {"s6": request.POST.get('s6'),
                             "s5": request.POST.get('s5'),
                             "s4": request.POST.get('s4'),
                             "s3": request.POST.get('s3'),
                             "s2": request.POST.get('s2'),
                             "s1": request.POST.get('s1')}

            Song.objects.create(name=name, guitar_string=guitar_string)

            return redirect(reverse('song'), kwargs={'message': 'Created successful'})

        if do == 'delete':
            song_id = request.POST.get('song_id')
            song = Song.objects.get(id=song_id)

            song.delete()

            return redirect(reverse('song'), kwargs={'message': 'Deleted successful'})
