from django.shortcuts import render

posts = [
	{
		'author' : 'Phill',
		'title' : 'First post',
		'content' : 'My first post',
		'date_posted' : '13 Nov 2020'
	},
	{
		'author' : 'Phalin',
		'title' : 'second post',
		'content' : 'My second post',
		'date_posted' : '14 Nov 2020'
	}
]

# Create your views here.
def home(request):
	context = {'posts' : posts}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request,'blog/about.html')