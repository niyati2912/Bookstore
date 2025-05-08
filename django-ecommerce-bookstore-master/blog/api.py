import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify, request
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom_project.settings')
django_app = get_wsgi_application()

app = Flask(__name__)

@app.route('/api/posts', methods=['GET'])
def get_posts():
    from blog.models import BlogPost
    posts = BlogPost.objects.all().values()
    return jsonify([dict(post) for post in posts])

@app.route('/api/posts', methods=['POST'])
def create_post():
    from blog.models import BlogPost
    from django.contrib.auth import get_user_model
    data = request.get_json()
    
    User = get_user_model()
    author = User.objects.get(id=data['author_id'])
    
    post = BlogPost.objects.create(
        title=data['title'],
        content=data['content'],
        author=author
    )
    return jsonify({'id': post.id, 'message': 'Post created successfully'})

if __name__ == '__main__':
    app.run(port=5000)