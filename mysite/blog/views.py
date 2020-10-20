from django.shortcuts import render

posts = [
    {
        'title': 'المدونه الاولي ',
        'content': 'قد حدث في الفتره الاخيره الكثير من الموارد الشيقه و الكثيره التي ادت الي حدوث الكثير من المواضيع الشيقه ',
        'post_date': '15-3-2019',
        'auther': 'mohamed magdy'
    },
        {
        'title': 'المدونه الاولي ',
        'content': 'قد حدث في الفتره الاخيره الكثير من الموارد الشيقه و الكثيره التي ادت الي حدوث الكثير من المواضيع الشيقه ',
        'post_date': '15-3-2019',
        'auther': 'mohamed magdy'
    },
        {
        'title': 'المدونه الاولي ',
        'content': 'قد حدث في الفتره الاخيره الكثير من الموارد الشيقه و الكثيره التي ادت الي حدوث الكثير من المواضيع الشيقه ',
        'post_date': '15-3-2019',
        'auther': 'mohamed magdy'
    },
        {
        'title': 'المدونه الاولي ',
        'content': 'قد حدث في الفتره الاخيره الكثير من الموارد الشيقه و الكثيره التي ادت الي حدوث الكثير من المواضيع الشيقه ',
        'post_date': '15-3-2019',
        'auther': 'mohamed magdy'
    },
       
]

def about(request):
    return render(request,'blog/about.html',{"title":"عني"})

def home(request):
    context = {
        'title': 'مدونة| الصفحه الرئيسيه',
        'posts': posts
    }

    return render(request, 'blog/index.html', context)

