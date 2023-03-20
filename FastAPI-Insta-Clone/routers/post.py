import random
import shutil
import string
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db.database import get_db
from db.db_post import create_post_db, posts_db, delete_post_db
from routers.schemas import PostBase, PostDisplay, UserAuth

router = APIRouter(
    prefix='/post',
    tags=['post']
)

image_url_types = ['absolute', 'relative']


@router.post('', response_model=PostDisplay)
def create_post(request: PostBase,
                db: Session = Depends(get_db),
                current_user: UserAuth = Depends(get_current_user)
                ):
    if request.image_url_type not in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Parameter image_url_type can only take "
                                   "values absolute or relative")
    return create_post_db(db, request)


@router.get('/all', response_model=List[PostDisplay])
def posts(db: Session = Depends(get_db)):
    return posts_db(db)


@router.post('/image')
def upload_image(image: UploadFile = File(...),
                 current_user: UserAuth = Depends(get_current_user)):
    rand_str = '_' + ''.join(random.choices(string.ascii_letters, k=6)) + '.'
    filename = rand_str.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': path}


@router.delete('/delete/{post_id}')
def delete_post(post_id: int, db: Session = Depends(get_db),
                current_user: UserAuth = Depends(get_current_user)):
    return delete_post_db(db, post_id, current_user.id)
