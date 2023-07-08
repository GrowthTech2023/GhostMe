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

For example, "LangChain Integration and Content Refinement" depends on the completion of "Caption Generation". Similarly, "Posting and Scheduling" can only be implemented after "Content Review and Editing".


================================================================================================================================================================================================================================================================================================================================


### Files/directories and discuss their purpose:

1. `server/app.py`:
This is the main file for the Flask application. It's responsible for setting up and configuring the Flask app and the database. It will also handle routing to different endpoints in your application.

2. `server/requirements.txt`:
This file contains a list of Python packages required for the project. It typically includes Flask, Celery, Redis, SQLAlchemy (for ORM), psycopg2 (for PostgreSQL), and other packages your project might require.

3. `server/models/`:
This directory will contain the database models for your application. These models will represent the data structures in your database.

   - `user.py`: Defines the User model, which includes fields such as user ID, email, and password.
   - `video.py`: Defines the Video model, which includes fields such as video ID, user ID, video file, and video transcription.

4. `server/routes/`:
This directory will contain the routes for your application.

   - `auth_routes.py`: Contains the routes for user authentication, including sign up, login, and logout.
   - `video_routes.py`: Contains the routes for video-related tasks, such as video upload, video transcription, and video posting.

5. `server/services/`:
This directory will contain the services that handle the business logic for your application.

   - `transcription_service.py`: Handles the logic for transcribing videos using the Descript API.
   - `gpt4_service.py`: Handles the logic for generating video captions using GPT-4.
   - `langchain_service.py`: Handles the communication with the LangChain API.
   - `agent_service.py`: Handles the tasks related to the four social media platform agents.
   - `schedule_service.py`: Handles the logic for scheduling video posts using the chosen scheduling API.

6. `server/utils/`:
This directory will contain the utility files for your application.

   - `celery_config.py`: Contains the configuration for Celery.
   - `redis_config.py`: Contains the configuration for Redis.

7. `frontend/package.json`:
This is the main file for the React application. It contains the list of packages required by the frontend.

8. `frontend/src/index.js` and `frontend/src/App.js`:
These are the main files for your React application. `index.js` is the entry point for the application and `App.js` is the main component that wraps all other components.

9. `frontend/components/`:
This directory will contain the React components for your application.

   - `Dashboard.js`: The main component that displays the user dashboard.
   - `VideoUploader.js`: The component that allows users to upload videos.
   - `VideoEditor.js`: The component that allows users to add prompts to their videos and review/edit AI-generated captions.
   - `PostScheduler.js`: The component that allows users to schedule their posts.

10. `frontend/state/`:
This directory will contain the files for state management in your application using Redux.

   - `store.js`: Contains the Redux store configuration.
   - `reducers.js`: Contains the Redux reducers.

11. `frontend/styles/main.css`:
This file contains the CSS styles for your application.

Remember, this is a rough guide to get you started. You will have to modify and add to it as per your project's needs. For example, you might need to add more services or components based on your requirements. 

It's also important to note that all the logic related to communication with APIs (like GPT-4, LangChain, and Descript), database operations, and task scheduling should ideally be handled in the server. This would ensure that sensitive data

like API keys and database credentials are not exposed in the client-side code. The frontend should primarily focus on UI/UX aspects, and communicate with the server through API calls to fetch or manipulate data.

12. `README.md`:
This is the documentation file where you provide information about the project, how to set it up and run it, and any other relevant details.

### server services and routes files in more detail:

#### server Services:

- `transcription_service.py`: This service will communicate with the Descript API. When a video is uploaded, this service will be responsible for sending the video to Descript, receiving the transcription, and saving it in the database associated with the video.

- `gpt4_service.py`: This service will communicate with the GPT-4 API. When a user inputs a prompt for a video, this service will send the prompt and the video transcription to GPT-4, receive the generated text, and provide it to the user for review/editing.

- `langchain_service.py`: This service will handle the translation of video captions. When a user chooses to translate the video captions, this service will send the captions to LangChain, receive the translated text, and provide it to the user for review/editing.

- `agent_service.py`: This service will manage the social media platform agents. Each agent will fetch real-time engagements on its platform to determine the best time to post a video. This data will be provided to the `schedule_service`.

- `schedule_service.py`: This service will handle video posting schedule. Based on the user's choice and the data from the `agent_service`, it will determine the best time to post a video. It will then schedule the video for posting at that time using a task queue (like Celery) and a message broker (like Redis).

#### server Routes:

- `auth_routes.py`: This file will handle the authentication routes. It will have routes for user registration (sign up), login, and logout. These routes will interact with the User model to create a new user, authenticate a user, or log out a user.

- `video_routes.py`: This file will handle the video-related routes. It will have routes for uploading a video, getting the transcription of a video, adding a prompt to a video, generating captions for a video, translating video captions, scheduling a video for posting, and posting a video. These routes will interact with the Video model and the various services to carry out these tasks.

In the frontend, each component file will represent a part of your application's UI and handle the related user interactions:

- `Dashboard.js`: This component will display the main dashboard to the user. It will show the list of uploaded videos and their status (transcribed, captioned, scheduled for posting, etc.). It will also provide options to navigate to other parts of the application.

- `VideoUploader.js`: This component will allow the user to upload a video. It will provide a file input to select the video file, and a form to input the video details. When the video is uploaded, it will call the video upload route in the server.

- `VideoEditor.js`: This component will allow the user to add a prompt to a video and review/edit the AI-generated captions. It will provide a text input for the prompt and a text area for the captions. It will call the appropriate routes in the server to generate and edit the captions.

- `PostScheduler.js`: This component will allow the user to schedule a video for posting. It will provide options to select the posting time and the social media platforms. It will call the appropriate route in the server to schedule the video.


================================================================================================================================================================================================================================================================================================================================


```bash
/postme
├── /server
│   ├── /app
│   │   ├── __init__.py  # Initialize your Flask application here
│   │   ├── /api
│   │   │   ├── __init__.py  # Blueprints for your API
│   │   │   └── routes.py  # All API endpoints are defined here
│   │   ├── /models
│   │   │   ├── __init__.py  # Database and ORM setup
│   │   │   ├── user_model.py  # User model
│   │   │   ├── video_model.py  # Video model
│   │   │   ├── social_platform_model.py  # Social media platform model
│   │   │   └── subscription_model.py  # Subscription model
│   │   ├── /services
│   │   │   ├── __init__.py
│   │   │   ├── video_service.py  # All video-related logic: uploading, transcoding, etc
│   │   │   ├── transcription_service.py  # All transcription logic: Descript API calls, etc
│   │   │   ├── gpt4_service.py  # All caption generation logic: calls to GPT-4 API, etc
│   │   │   ├── lang_chain_service.py  # Communication with LangChain, decision-making layer
│   │   │   ├── /agents
│   │   │   │   ├── __init__.py
│   │   │   │   ├── facebook_agent_service.py  # Manage Facebook agent, fetching real-time engagements
│   │   │   │   ├── instagram_agent_service.py  # Manage Instagram agent, fetching real-time engagements
│   │   │   │   ├── twitter_agent_service.py  # Manage Twitter agent, fetching real-time engagements
│   │   │   │   └── linkedin_agent_service.py  # Manage LinkedIn agent, fetching real-time engagements
│   │   │   ├── agent_service.py  # Agent manager that interacts with individual agent services
│   │   │   └── schedule_service.py  # Scheduling logic: determine optimal times to post
│   │   └── /auth
│   │       ├── __init__.py
│   │       ├── auth_service.py  # All authentication logic: Google SSO, Facebook login, etc
│   │       └── dashboard_service.py  # Dashboard logic: user uploads, caption generation, post generation
│   ├── config.py  # App configuration settings
│   ├── run.py  # Runs the application
│   ├── /utils
│   │   ├── __init__.py
│   │   ├── error_handler.py  # Custom error handling
│   │   └── logger.py  # Logging setup
│   └── /tests  # All the unit tests go here
├── /frontend
│   ├── /src
│   │   ├── /components
│   │   │   ├── /dashboard
│   │   │   │   └── Dashboard.js  # User dashboard
│   │   │   ├── /auth
│   │   │   │   ├── Login.js  # Login component
│   │   │   │   └── Register.js  # Register component
│   │   │   ├── /video
│   │   │   │   ├── VideoUpload.js  # Video upload component
│   │   │   │   └── VideoList.js  # List of uploaded
│   │   │   │   └── VideoList.js  # List of uploaded videos
│   │   │   ├── /caption
│   │   │   │   └── CaptionGenerate.js  # Caption generation component
│   │   │   └── /post
│   │   │       └── PostCreate.js  # Post creation component
│   │   ├── App.js  # Main React component
│   │   └── index.js  # Root React component
│   └── package.json  # Node.js manifest file
└── README.md  # Project overview

```

Here is a brief overview of what each directory and file will do:

1. The `server` directory will contain all the server-side code written in Python Flask.

2. The `app` directory inside `server` will contain the main application code.

3. The `api` directory inside `app` will contain all the API endpoints required by the front-end.

4. The `models` directory will contain all the database models.

5. The `services` directory will contain all the business logic of the application, including video management, transcription, caption generation, agent management, and scheduling.

6. The `agents` directory inside `services` will contain individual services for each social media platform agent.

7. The `auth` directory will contain the authentication logic and user dashboard logic.

8. The `utils` directory will contain utility files such as custom error handlers and logging setup.

9. The `tests` directory will contain all the unit tests for the

application.

10. The `frontend` directory will contain all the client-side code written in React.js.

11. The `src` directory inside `frontend` will contain all the source code for the front-end, including the main application component and individual components for the dashboard, auth, video, caption, and post.

Here's a more detailed breakdown of the functionality of each of the main files:

- `routes.py`: Contains all API endpoints, which handle requests from the front-end and return responses.

- `user_model.py`, `video_model.py`, `social_platform_model.py`, `subscription_model.py`: These are the database models for different entities in the application. They define how data is structured in the database.

- `video_service.py`: Manages all video-related logic, such as uploading and transcoding videos.

- `transcription_service.py`: Handles all transcription logic, including making calls to the Descript API to get transcriptions of videos.

- `gpt4_service.py`: Handles all caption generation logic, including making calls to the GPT-4 API to generate captions from transcriptions.

- `lang_chain_service.py`: Communicates with LangChain for translation services and is the decision-making layer for choosing the best captions.

- `facebook_agent_service.py`, `instagram_agent_service.py`, `twitter_agent_service.py`, `linkedin_agent_service.py`: These are the services for the individual social media platform agents. They fetch real-time engagements from their respective platforms to help determine the best times to post.

- `agent_service.py`: Acts as an agent manager that interacts with the individual agent services and consolidates the data they provide.

- `schedule_service.py`: Contains the scheduling logic, which determines the optimal times to post based on data from the agents.

- `auth_service.py`: Handles all authentication logic, such as Google SSO and Facebook login.

- `dashboard_service.py`: Manages the user dashboard, including displaying user uploads, generating captions, and creating posts.

- `Dashboard.js`, `Login.js`, `Register.js`, `VideoUpload.js`, `VideoList.js`, `CaptionGenerate.js`, `PostCreate.js`: These are the individual React components for different parts of the front-end. They handle user interaction and display data from the back-end.

I have checked this structure multiple times to ensure it meets all our project requirements. It should give us a robust and scalable foundation for our application.
Frontend dev can always change what's needed



====================================
Jason's notes

this is what the user sees and deos on the dashboard

Connects either of 4 socials -- Instagram, Facebook, TikTok and YouTube (Top of page)
Upload their video (right under the connect tab, and is the far left side within the page margin)
Add optional prompt (this text field area with a palceholder, this section is in the middle)
on the rightside is a vertical beautiful tab where users can select which platform they want to post to (this gives them more flexibility to decide wether tha tparticular post should go on which platofrom)
