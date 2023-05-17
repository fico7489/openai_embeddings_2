# Openai_embeddings_2

## Questions

### we have one question which will user ask, 

**question_1**:

```
what is the status of the my order?
```

### we have 3 question for which we will calculate similarity:

**question_2**:

```
when my order will arrive?
```

**question_3**:

```
what is with my order?
```

**question_4**:

```
what is the status of the my order?
```

## Embeddings

For each question embedding is fetched from the openai with this code:

```
curl --location 'https://api.openai.com/v1/embeddings' \
--header 'Authorization: Bearer {TOKEN}' \
--header 'Content-Type: application/json' \
--data '{
    "input": "{TEXT}",
    "model": "text-embedding-ada-002"
  }'
```

Embeddings for each question is stored in folder "embeddings"
