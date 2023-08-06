# PostMe Project Manual

## SECTION 1: Project Overview

PostMe is a tool designed to aid content creators in optimizing their social media posts. The main goal of this project is to develop a tool that leverages AI to generate platform-specific captions and descriptions for videos. The tool will use GPT-4 for captioning, LangChain for decision-making, and real-time data for post timing. The new version of PostMe will be built using no-code tools, Xano and Bubble, to streamline the development process and make it more accessible.

### Project Components

1. **Platform Selection**: The platform selection tabs will have icons representing each platform. Users can select multiple platforms to post their content simultaneously.

2. **Video Upload**: Content creators upload their video content to our platform. This process is simplified with a drag-and-drop interface in Bubble.

3. **Video Transcription**: After a video is uploaded, the content of the video will be transcribed using an API. The transcriptions provide necessary context to GPT-4 to generate relevant captions.

4. **User Prompt**: Content creators can add a prompt telling GPT-4 what they want the video to convey. This prompt input can be a textarea that clearly explains its purpose to users. It's optional and can be easily implemented in Bubble.

5. **GPT-4 Caption Generation**: The user prompt along with the video transcription is sent to GPT-4. GPT-4 generates captions in response to the user's request.

6. **LangChain**: LangChain is used as the decision-making layer in the process. It manages communication between GPT-4 and various social media platform agents, ensuring that the generated captions meet the specific requirements of each platform.

7. **Social Media Agents**: Each social media platform (Facebook, Instagram, Twitter, and TikTok.) has its own agent. These agents provide platform-specific information such as desired description length, hashtag usage, content style, etc. to LangChain, which in turn communicates these requirements to GPT-4.

8. **Caption Finalization**: GPT-4 tailors the captions to fit the specific constraints of each platform based on the information received from the social media agents via LangChain. Once the captions are finalized, they are added to the video.

9. **Video Posting**: The video, along with the platform-specific captions, is then posted on each platform when the user clicks "Post".

### Principles

The design principles remain the same, focusing on a clean, minimalist UI, animations and transitions to enhance UX, responsive design for all device sizes, and a well-planned information architecture for intuitive navigation.

### Additional Features

Additional features include AI-generated thumbnails and video upscaling using other AI plugins. These features can be implemented using various plugins available in the Bubble marketplace.

### Tech Stack

The tech stack will now include Xano and Bubble. Xano will be used for backend operations, including database management, API calls, and server-side logic. Bubble will be used for frontend operations, including UI design, user interactions, and client-side logic.

### User Authentication and Dashboard

The sign-in page and dashboard will be built using Bubble's visual programming interface. Users will be able to sign in to their account using their email and password. New users will be able to create an account. After signing in, users will be taken to a dashboard where they can upload videos, generate captions, and post their content to various platforms.


## SECTION 2: Wireframe and Flow

The user flow remains largely the same, but the implementation will now be done using Bubble's visual programming interface and Xano's backend-as-a-service.

1. **User Authentication**: Users can sign in with Google SSO or Facebook. Successful authentication redirects the user to the dashboard.

2. **Dashboard**: Here, users can connect their social media accounts (YouTube, Facebook, Instagram, TikTok), upload their videos, and optionally provide a prompt.

3. **Video Transcription**: The uploaded video is sent to the server (handled by Xano). The server invokes the transcription API to transcribe the video. The transcription result is stored in the database managed by Xano.

4. **GPT-4 Caption Generation**: The transcription and user prompt (if provided) are sent to GPT-4. GPT-4 generates a draft description and hashtags.

5. **LangChain Processing**: The draft description and hashtags are sent to LangChain. LangChain communicates with the four GPT-4 agents, each representing a social media platform. Each agent reviews the draft content and provides feedback based on platform-specific requirements. LangChain compiles the feedback and sends it back to GPT-4. If modifications are needed, GPT-4 adjusts the content and sends the new draft to LangChain, and the process repeats until all requirements are met.

6. **Content Finalization**: Once all platform requirements are met, the final content (description, hashtags) is stored in the database.

7. **Scheduling**: If the user chooses to schedule the post, the schedule_agent determines the best time for posting based on real-time platform usage and engagement. The user can confirm the suggested time or choose a custom time.

8. **Posting**: At the scheduled time, each posting agent fetches the final content from the database. The posting agent posts the video along with the platform-specific description and hashtags on the respective platform.

## SECTION 3: Team's Work Milestones

The milestones remain largely the same, but the tasks will now be performed using Bubble and Xano. The tasks include setting up the project, implementing user authentication, video upload and transcription, caption generation, LangChain integration and content refinement, content review and editing, posting and scheduling, and testing.

## SECTION 4: Project Structure

The project structure will be simplified due to the use of no-code tools. Bubble will handle the frontend, including UI components and user interactions. Xano will handle the backend, including database operations, server-side logic, and API calls.

## SECTION 5: Additional Notes on UI

The user dashboard will be designed in Bubble, providing a clean and intuitive interface. Users can connect their social media accounts, upload videos, provide prompts, and select the platforms they want to post to. The agents (facebook_agent_service.py, instagram_agent_service.py, threads_agent.py, tiktok_agent_service.py, youtube-shorts_agent_service.py) will be set up in Xano, communicating with LangChain and providing platform-specific requirements.

=====================================================================================

### Bubble Workload

**User Interface (UI) Design & User Experience (UX) Design**:
- Designing the layout of the application
- Placement of buttons, forms, text, images, and other UI elements
- Designing the flow from one page to another
- Managing the interactions users have with the application

**User Authentication**:
- User registration form design and functionality
- Login form design and functionality
- Password reset form design and functionality
- User session management on the client side

**Frontend Logic**:
- Actions that happen when a user clicks a button
- Actions that happen when a user submits a form
- Interactions when a user navigates from one page to another
- Any other client-side logic

**Data Binding**:
- Displaying data from the database in the UI
- Updating the UI when the data changes
- Binding user input to database fields

**API Integration**:
- Sending requests to the Xano backend
- Handling responses from the Xano backend
- Integrating with third-party APIs if needed

### Xano Workload

**Database Management**:
- Designing the database schema
- Creating, reading, updating, and deleting data
- Managing database queries

**Server-Side Logic**:
- Validating user input
- Processing data
- Returning responses to the Bubble frontend

**API Creation**:
- Defining API endpoints
- Managing requests and responses
- Handling errors and exceptions

**User Authentication**:
- Storing user credentials securely
- Validating user credentials
- Managing user sessions on the server side

**Third-Party API Integration**:
- Sending requests to external services
- Processing responses from external services

**Task Scheduling**:
- Scheduling posts
- Sending out automated emails
- Running periodic data updates

**Data Processing**:
- Video transcription
- AI caption generation
- Content refinement

