#!/bin/bash

NAME="test_user"
EMAIL="test@mlh.io"
CONTENT="test post"

echo "Creating timeline post.."
POST_RESPONSE=$(curl -s -X POST http://localhost:5001/api/timeline_post -d "name=$NAME&email=$EMAIL&content=$CONTENT")

echo $POST_RESPONSE
POST_ID=$(echo $POST_RESPONSE | jq '.id')

echo "Fetching all timeline posts.."
GET_RESPONSE=$(curl -s http://localhost:5001/api/timeline_post)

echo $GET_RESPONSE

MATCH=$(echo $GET_RESPONSE | jq ".timeline_posts[] | select(.id == $POST_ID)")

if [ -n "$MATCH" ]; then
    echo "SUCCESS"
else
    echo "FAILURE"
fi