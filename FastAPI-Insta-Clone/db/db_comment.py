from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db.models import DbComment
from routers.schemas import PostBase, CommentBase


def create_comment(db: Session, request: CommentBase):
    new_comment = DbComment(
        text=request.text,
        username=request.username,
        post_id=request.post_id,
        timestamp=datetime.now()
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return 'Comment created'


def get_all_comments(db: Session, post_id: int):
    return db.query(DbComment).filter(DbComment.post_id==post_id).all()
