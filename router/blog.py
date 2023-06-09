from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional



router = APIRouter(
        prefix='/blog',
        tags=['blog']
        )

#@app.get('/blog/all')
#def all_blog():
#    return {'message': 'all blogs'}


@router.get('/all',
         summary='Retrieve all blogs',
         description='This api call simulates fetching all blogs',
         response_description='The list of available blogs'
         )
def get_all_blogs(page, page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}




@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog

    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}




class ResumeType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'





@router.get('/resume/type/{type}', tags=['resume'],
         summary='Retrieve resume',
         description='this api retrieve my resume')
def get_resume_type(type: ResumeType):
    return {'message': f'resume type {type}'}

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 7:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'{id} ----> {response.status_code} not found))'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f"blog with {id}"}


