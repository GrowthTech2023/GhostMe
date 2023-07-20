## SECTION 1

PostMe
Objective
This is an AI tool for content creators. The primary objective of the project is to develop an AI-powered tool that helps content creators to generate platform-specific captions and descriptions for their videos. The tool will utilize GPT-4, LangChain, and Descript's API for video transcription, and the generated captions will be tailored to meet the specific requirements of various social media platforms.

Project Components
0. The platform selection tabs will have icons representing each platform. Allow multiple selections so users can post to different platforms.

1. Video Upload
Content creators upload their video content to our platform.

2. Video Transcription
After a video is uploaded, the content of the video will be transcribed using Descript's API. The transcriptions provide necessary context to GPT-4 to generate relevant captions.
The video upload section will have a drag and drop interface for simplicity. Show video thumbnail previews after uploading.

3. User Prompt
Content creators can add a prompt telling GPT-4 what they want the video to convey. The prompt could be something like: “write me captions in the voice of Steve Jobs about why the MacBook is the best computer in the world”.
The prompt input can be a textarea that clearly explains its purpose to users. Make it optional.

4. GPT-4 Caption Generation
The user prompt along with the video transcription is sent to GPT-4. GPT-4 generates captions in response to the user's request.

5. LangChain
LangChain is used as the decision-making layer in the process. It manages communication between GPT-4 and various social media platform agents, ensuring that the generated captions meet the specific requirements of each platform.

6. Social Media Agents
Each social media platform (Facebook, Instagram, Twitter, and TikTok.) has its own agent. These agents provide platform-specific information such as desired description length, hashtag usage, content style, etc. to LangChain, which in turn communicates these requirements to GPT-4.

7. Caption Finalization
GPT-4 tailors the captions to fit the specific constraints of each platform based on the information received from the social media agents via LangChain. Once the captions are finalized, they are added to the video.

8. Add a preview section that shows how the final captions/text will look on different platforms after processing.
Include options to edit the generated captions before posting.

9. The scheduling section should have a calendar picker to select dates/times. Show suggested best times and allow custom scheduling.

10. Video Posting
The video, along with the platform-specific captions, is then posted on each platform when the user clicks "Post"

### Principles
- Use clean, minimalist UI elements in line with platform branding. Follow Material Design principles for usability.
- Make use of animations and transitions to enhance UX and provide user feedback.
- Implement responsive design to optimize on all device sizes. Focus on mobile experience.
- Carefully plan information architecture and intuitive navigation between sections.


- Additional Features
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

### Files and client and discuss their purpose:
## Client Directory
1. **`package.json`**: Contains the list of dependencies that the React app needs, as well as scripts for starting, building, and testing the app.
2. **`package-lock.json`**: Ensures that the installed dependencies match the ones in `package.json` for consistent environments.
3. **`src/App.js`**: Serves as the root component of the React application. It is where the main layout of the application resides, including the navigation and routing.
4. **`src/index.js`**: Renders the `App.js` component into the root of the `index.html` file.
5. **`src/components`**: Contains all React components that build up the UI of the application.

    - **`auth/Login.js`**: Handles the login process of users by interfacing with the backend's authentication service.
    - **`auth/Register.js`**: Handles the registration process of new users by interfacing with the backend's user creation service.
    - **`caption/CaptionGenerate.js`**: Takes the uploaded video transcript and user-provided prompt, sends them to GPT-4, receives the generated captions, and displays them to the user.
    - **`dashboard/Dashboard.js`**: Renders the user dashboard where users can connect their social media accounts, upload videos, provide a prompt, and post their content.
    - **`post/PostCreate.js`**: Allows users to create a new post by providing a video and optional prompt. It then sends this data to the backend for processing.
    - **`video/VideoUpload.js`**: Provides a form for users to upload their videos. Once a video is uploaded, it's sent to the backend for transcription.
    - **`video/VideoList`**: Displays a list of videos that the user has uploaded and their current processing status.

### server services and routes files in more detail:
## Server Directory
1. **`app.py`**: Creates the Flask application and sets up the database connection.
2. **`config.py`**: Contains configuration variables for the Flask application and database connection.
3. **`app/__init__.py`**: Initializes the Flask application and its blueprints.
4. **`app/api/routes.py`**: Defines the endpoints for the Flask application, such as user registration, login, video upload, and caption generation.
5. **`app/auth/auth_service.py`**: Handles the registration and login processes by validating user input and interacting with the user database model.
6. **`app/auth/dashboard_service.py`**: Handles requests from the user's dashboard, such as fetching the user's social media connections and videos.
7. **`app/models`**: Contains the ORM models for the application's PostgreSQL database.

    - **`user_model.py`**: Defines the user model including fields like username, email, password, etc., and methods for handling password hashing and verification.
    - **`social_platform_model.py`**: Defines the model for storing user's social media accounts.
    - **`subscription_model.py`**: Defines the model for storing user's subscription status and details.
    - **`video_model.py`**: Defines the model for storing uploaded video details and generated captions.
8. **`app/secrets/client_secret_978165118544-hje1b6kr557sdem81ig9n2ik9qm5udki.apps.googleusercontent.com.json`**: Contains the client secret for Google OAuth.
9. **`app/services`**: Contains services that handle the core business logic of the application.

    - **`agents/facebook_agent_service.py`**: Communicates with the Facebook API to post content and fetch platform-specific rules.
    - **`agents/instagram_agent_service.py`**: Communicates with the Instagram API to post content and fetch platform-specific rules.
    - **`agents/tiktok_agent_service.py`**: Communicates with the TikTok API to post content and fetch platform-specific rules.
    - **`agents/threads_agent.py`**: Communicates with the Threads API to post content and fetch platform-specific rules.
    - **`agents/youtube-shorts_agent_service.py`**: Communicates with the YouTube API to post content and fetch platform-specific rules.
    - **`descript_transcription.py`**: Sends the uploaded video to Descript's API for transcription, receives the transcription and saves it in a PostgreSQL database.
    - **`gpt4_caption.py`**: Sends the video transcript and user-provided prompt to GPT-4, receives the generated captions, and sends them to LangChain for refinement.
    - **`lang_chain_service.py`**: Receives initial captions from GPT-4, sends them to social media agents for feedback, and sends the feedback to GPT-4 for caption refinement.
    - **`schedule_service.py`**: Determines the optimal post times based on real-time platform usage and engagement.
    - **`video_service.py`**: Handles video upload requests, initiates video transcription, and stores the video details in the database.
10. **`utils/error_handler.py`**: Handles any errors that occur during the execution of the application.
11. **`utils/logger.py`**: Logs application events, such as login, registration, video upload, and caption generation.

================================================================================================================================================================================================================================================================================================================================

====================================

## SECTION 5
Additional Notes on UI

this is what the user sees and deos on the dashboard

Connects either of 5 socials -- Instagram, Threads, Facebook, TikTok and YouTube (Top of page)
Upload their video (right under the connect tab, and is the far left side within the page margin)
Add optional prompt (this text field area with a placeholder, this section is in the middle)
on the right side is a vertical beautiful tab where users can select which platform they want to post to (this gives them more flexibility to decide wether tha tparticular post should go on which platofrom)


===============================================
now lets move to the agents side

facebook_agent_service.py

instagram_agent_service.py

threads_agent.py

tiktok_agent_service.py

youtube-shorts_agent_service.py

per the project requirements they will be communicating with langchainEach agent reviews the draft content and provides feedback based on platform-specific requirements.

 LangChain compiles the feedback and sends it back to GPT-4

What are the platform requiremtns?

1. `FaceBook`
    - Description length
    - Number of paragraphs (if description length needs to be long)
    - Hashtags - based on context goten from transcription
    - Tags
    - Keywords

2. `Instagram`
    - Description length
    - Number of paragraphs (Instagram length needs to be long with at least 3 paragraphs)
    - Hashtags - based on context gotten from transcription
    - Tags
    - Keywords

3. `TikTok`
    - Description length
    - Number of paragraphs (TikTok likes one sentence captions )
    - Hashtags - based on context gotten from transcription
    - Tags
    - Keywords

4. `Threads`
    - Description length
    - Number of paragraphs (if description length needs to be long)
    - Hashtags - based on context gotten from transcription
    - Tags
    - Keywords

5. `YouTube Shorts`
    - Description length
    - Number of paragraphs (if description length needs to be long)
    - Hashtags - based on context gotten from transcription
    - Tags
    - Keywords
