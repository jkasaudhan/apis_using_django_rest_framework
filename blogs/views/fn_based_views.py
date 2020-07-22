from rest_framework.response import  Response
from rest_framework.decorators import api_view
from blogs.serializers import BlogSerializer
from blogs.models import BlogModel

@api_view(['GET', 'POST'])
def blog_view(request):
    if request.method == 'GET':
        blogs = BlogModel.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response({
                'success': True,
                'message': 'Get request fulfilled!! ',
                'data': serializer.data
            })

    if request.method == 'POST':
        return Response({
        'success': True,
        'message': 'Post request fulfilled!!',
        'data': ''
    })

    return Response({
            'success': False,
            'message': 'Invalid request',
            'data': ''
        })