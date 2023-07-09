## SECTION 1

PostMe
Objective
This is an AI tool for content creators. The primary objective of the project is to develop an AI-powered tool that helps content creators to generate platform-specific captions and descriptions for their videos. The tool will utilize GPT-4, LangChain, and Descript's API for video transcription, and the generated captions will be tailored to meet the specific requirements of various social media platforms.

Project Components
1. Video Upload
Content creators upload their video content to our platform.

2. Video Transcription
After a video is uploaded, the content of the video will be transcribed using Descript's API. The transcriptions provide necessary context to GPT-4 to generate relevant captions.

3. User Prompt
Content creators can add a prompt telling GPT-4 what they want the video to convey. The prompt could be something like: “write me captions in the voice of Steve Jobs about why the MacBook is the best computer in the world”.

4. GPT-4 Caption Generation
The user prompt along with the video transcription is sent to GPT-4. GPT-4 generates captions in response to the user's request.

5. LangChain
LangChain is used as the decision-making layer in the process. It manages communication between GPT-4 and various social media platform agents, ensuring that the generated captions meet the specific requirements of each platform.

6. Social Media Agents
Each social media platform (Facebook, Instagram, Twitter, and TikTok.) has its own agent. These agents provide platform-specific information such as desired description length, hashtag usage, content style, etc. to LangChain, which in turn communicates these requirements to GPT-4.

7. Caption Finalization
GPT-4 tailors the captions to fit the specific constraints of each platform based on the information received from the social media agents via LangChain. Once the captions are finalized, they are added to the video.

8. Video Posting
The video, along with the platform-specific captions, is then posted on each platform when the user clicks "Post"

9. Additional Features
Additional features include AI-generated thumbnails and video upscaling using other AI plugins.

Tech Stack
server
Python Flask: The server API will be built using the Flask framework. Flask provides a lightweight and flexible framework, making it an excellent choice for the project.
Celery: Given the nature of the AI tasks being performed, these tasks will be managed using Celery. This will ensure that time-consuming tasks such as video transcription and caption generation are performed asynchronously, improving the efficiency of the system.
Redis: Redis will be used as the message broker for Celery. It will also provide caching functionalities to speed up the system.
PostgreSQL: The application's data will be stored in a PostgreSQL database. PostgreSQL is a robust and reliable database system that can handle complex data workloads.
MindsDB: Optionally MindsDB will be used due to it being highly optimized and configured for AI applications such PostMe!.
Frontend
ReactJS: The user interface of the application will be built using ReactJS. ReactJS is a powerful library for building dynamic user interfaces.
Redux: Redux will be used for state management. This will be particularly useful if the application state becomes complex.
Material-UI/Bootstrap/Tailwind CSS: These libraries will be used for designing and styling the user interface. They provide pre-built components that can significantly speed up the development process.
User Authentication and Dashboard
Sign-in Page: Users will be able to sign in to their account using their email and password. New users will be able to create an account.

Dashboard: After signing in, users will be taken to a dashboard where they can upload videos, generate captions, and post their content to various platforms.

server
Python Flask:
Develop an API that receives video files and user prompts from the frontend.
Implement endpoints that call Descript's API for video transcription.
Implement endpoints that communicate with GPT-4 for caption generation.
Use Celery and Redis for managing and speeding up AI tasks.
Store application data in a PostgreSQL database.
Frontend
ReactJS:
Create dynamic user interfaces for the application.
Use Redux for state management.
Use Material-UI, Bootstrap, and Tailwind CSS for designing and styling the user interface.

## SECTION 2
WIREFRAME AND FLOW

1. User Authentication:
    - User signs in with Google SSO or Facebook.
    - Authentication success redirects the user to the dashboard.

2. Dashboard:
    - The user connects their social media accounts (YouTube, Facebook, Instagram, TikTok).
    - The user uploads their video and optionally provides a prompt.

3. Video Transcription:
    - The uploaded video is sent to the server.
    - The server invokes the Descript API to transcribe the video.
    - The transcription result is stored in the PostgreSQL database.

4. GPT-4 Caption Generation:
    - The transcription and user prompt (if provided) are sent to GPT-4.
    - GPT-4 generates a draft description and hashtags.

5. LangChain Processing:
    - The draft description and hashtags are sent to LangChain.
    - LangChain communicates with the four GPT-4 agents, each representing a social media platform.
    - Each agent reviews the draft content and provides feedback based on platform-specific requirements.
    - LangChain compiles the feedback and sends it back to GPT-4.
    - If modifications are needed, GPT-4 adjusts the content and sends the new draft to LangChain, and the process repeats until all requirements are met.

6. Content Finalization:
    - Once all platform requirements are met, the final content (description, hashtags) is stored in the PostgreSQL database.

7. Scheduling:
    - If the user chooses to schedule the post, the schedule_agent determines the best time for posting based on real-time platform usage and engagement.
    - The user can confirm the suggested time or choose a custom time.

8. Posting:
    - At the scheduled time, each posting agent fetches the final content from the PostgreSQL database.
    - The posting agent posts the video along with the platform-specific description and hashtags on the respective platform.

================================================================================================================================================================================================================================================================================================================================

## SECTION 3
Team's Work Milestones.
1. **Project Setup**
   - Set up project repository
   - Create Flask application
   - Set up PostgreSQL database
   - Create basic React application

2. **User Authentication**
   - Implement user authentication
   - Design and implement user dashboard
   - Enable feature to connect social media accounts

3. **Video Upload and Transcription**
   - Implement video upload
   - Transcribe uploaded videos
   - Implement user prompt input feature

4. **Caption Generation**
   - Set up communication with GPT-4
   - Generate initial captions
   - Store generated captions and transcription

5. **LangChain Integration and Content Refinement**
   - Integrate LangChain
   - Implement feedback loop between LangChain, GPT-4, and agents
   - Store final content

6. **Content Review and Editing**
   - Implement functionality for users to review and edit final content

7. **Posting and Scheduling**
   - Implement posting agents
   - Implement scheduling feature
   - Set up schedule_agent
   - Implement functionality to determine optimal post times

8. **Testing**
   - Test all implemented features
   - Fix identified bugs

9. **Wrap-up and Next Steps**
   - Review project progress
   - Discuss outstanding tasks
   - Plan for next steps

Some tasks are dependent on other tasks
For example, "LangChain Integration and Content Refinement" depends on the completion of "Caption Generation". Similarly, "Posting and Scheduling" can only be implemented after "Content Review and Editing".

================================================================================================================================================================================================================================================================================================================================

## SECTION 4

```bash
/PostMe
├── client
│   ├── package.json
│   ├── package-lock.json
│   └── src
│       ├── App.js
│       ├── components
│       │   ├── auth
│       │   │   ├── Login.js
│       │   │   └── Register.js
│       │   ├── caption
│       │   │   └── CaptionGenerate.js
│       │   ├── dashboard
│       │   │   └── Dashboard.js
│       │   ├── post
│       │   │   └── PostCreate.js
│       │   └── video
│       │       ├── VideoList
│       │       └── VideoUpload.js
│       └── index.js
├── create_working_tree.sh
├── LICENSE
├── README.md
├── requirements.txt
├── Roadmap
│   ├── agenda.md
│   ├── detialed-wireframe.md
│   ├── pricing.md
│   ├── project_structure.md
│   ├── shipments.md
│   └── wireframe.md
├── server
│   ├── app
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── auth
│   │   │   ├── auth_service.py
│   │   │   ├── dashboard_service.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── social_platform_model.py
│   │   │   ├── subscription_model.py
│   │   │   ├── user_model.py
│   │   │   └── video_model.py
│   │   ├── secrets
│   │   │   ├── client_secret_978165118544-hje1b6kr557sdem81ig9n2ik9qm5udki.apps.googleusercontent.com.json
│   │   │   └── __init__.py
│   │   └── services
│   │       ├── agents
│   │       │   ├── facebook_agent_service.py
│   │       │   ├── __init__.py
│   │       │   ├── instagram_agent_service.py
│   │       │   ├── tiktok_agent_service.py
│   │       │   ├── threads_agent.py # INFO!: `threads_agent.py`(is a 4 day old app just released by Facebook, it's linked with instagram and has all twitter capabilites)
│   │       │   └── youtube-shorts_agent_service.py
│   │       ├── agent_service.py
│   │       ├── descript_transcription.py
│   │       ├── gpt4_caption.py
│   │       ├── __init__.py
│   │       ├── lang_chain_service.py
│   │       ├── schedule_service.py
│   │       └── video_service.py
│   ├── app.py
│   ├── config.py
│   ├── tests
│   └── utils
│       ├── error_handler.py
│       ├── __init__.py
│       └── logger.py
└── Team_manual.md

20 directories, 53 files

```

Here is a brief overview of what each directory and file will do:

### Files/directories and discuss their purpose:

GPT TO FILL IN THIS INFO SECTION BASED ON WORKING TREE

### server services and routes files in more detail:

#### server Services:

GPT TO FILL IN THIS INFO SECTION BASED ON WORKING TREE

================================================================================================================================================================================================================================================================================================================================

====================================

## SECTION 5
Jason's notes

this is what the user sees and deos on the dashboard

Connects either of 5 socials -- Instagram, Threads, Facebook, TikTok and YouTube (Top of page)
Upload their video (right under the connect tab, and is the far left side within the page margin)
Add optional prompt (this text field area with a palceholder, this section is in the middle)
on the rightside is a vertical beautiful tab where users can select which platform they want to post to (this gives them more flexibility to decide wether tha tparticular post should go on which platofrom)
