# PostMe

## Objective
This is an AI tool for content creators. The primary objective of the project is to develop an AI-powered tool that helps content creators to generate platform-specific captions and descriptions for their videos. The tool will utilize GPT-4, LangChain, and Descript's API for video transcription, and the generated captions will be tailored to meet the specific requirements of various social media platforms.

## Project Components

### 1. Video Upload
Content creators upload their video content to our platform.

### 2. Video Transcription
After a video is uploaded, the content of the video will be transcribed using Descript's API. The transcriptions provide necessary context to GPT-4 to generate relevant captions.

### 3. User Prompt
Content creators can add a prompt telling GPT-4 what they want the video to convey. The prompt could be something like: “write me captions in the voice of Steve Jobs about why the MacBook is the best computer in the world”.

### 4. GPT-4 Caption Generation
The user prompt along with the video transcription is sent to GPT-4. GPT-4 generates captions in response to the user's request.

### 5. LangChain
LangChain is used as the decision-making layer in the process. It manages communication between GPT-4 and various social media platform agents, ensuring that the generated captions meet the specific requirements of each platform.

### 6. Social Media Agents
Each social media platform (Facebook, Instagram, Twitter, and TikTok.) has its own agent. These agents provide platform-specific information such as desired description length, hashtag usage, content style, etc. to LangChain, which in turn communicates these requirements to GPT-4.

### 7. Caption Finalization
GPT-4 tailors the captions to fit the specific constraints of each platform based on the information received from the social media agents via LangChain. Once the captions are finalized, they are added to the video.

### 8. Video Posting
The video, along with the platform-specific captions, is then posted on each platform when the user clicks "Post"

### 9. Additional Features
Additional features include AI-generated thumbnails and video upscaling using other AI plugins.

## Tech Stack

### server
- **Python Flask:** The server API will be built using the Flask framework. Flask provides a lightweight and flexible framework, making it an excellent choice for the project.
- **Celery:** Given the nature of the AI tasks being performed, these tasks will be managed using Celery. This will ensure that time-consuming tasks such as video transcription and caption generation are performed asynchronously, improving the efficiency of the system.
- **Redis:** Redis will be used as the message broker for Celery. It will also provide caching functionalities to speed up the system.
- **PostgresML:** The application's data will be stored in a PostgresML database. PostgresML is a robust and reliable database system that can handle complex data workloads.
- **MindsDB**: Optionally MindsDB will be used due to it being highly optimized and configured for AI applications such PostMe!.

### Frontend
- **ReactJS:** The user interface of the application will be built using ReactJS. ReactJS is a powerful library for building dynamic user interfaces.
- **Redux:** Redux will be used for state management. This will be particularly useful if the application state becomes complex.
- **Material-UI/Bootstrap/Tailwind CSS:** These libraries will be used for designing and styling the user interface. They provide pre-built components that can significantly speed up the development process.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## User Authentication and Dashboard
1. **Sign-in Page:** Users will be able to sign in to their account using their email and password. New users will be able to create an account.

2. **Dashboard:** After signing in, users will be taken to a dashboard where they can upload videos, generate captions, and post their content to various platforms.

## server
- **Python Flask:** 
  - Develop an API that receives video files and user prompts from the frontend.
  - Implement endpoints that call Descript's API for video transcription.
  - Implement endpoints that communicate with GPT-4 for caption generation.
  - Use Celery and Redis for managing and speeding up AI tasks.
  - Store application data in a PostgresML database.

## Frontend
- **ReactJS:** 
  - Create dynamic user interfaces for the application.
  - Use Redux for state management.
  - Use Material-UI, Bootstrap, and Tailwind CSS for designing and styling the user interface.
