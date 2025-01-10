 SociaLytics_fin

Open request.py from templates , and on line number 11, insert your Astra DB token as shown below to run the program: astrakey=AstraCS:bMDNJTEYYywYDUkFuMJIsbig:e4ceab41db62b9dc82879301803e801c8a9bb9166888d7a8ce7426a1b57da5ca

🌟 Tech Titans Team: Social Media Performance Analysis Module 🌟  

Welcome to the Social Media Performance Analysis Module submission for the Level Supermind Hackathon! 🚀  
Our innovative project blends cutting-edge tools like Langflow and DataStax Astra DB to deliver actionable insights from social media engagement data.  

---

🎯 Objective  

Harness the power of AI and scalable databases to analyze engagement metrics for mock social media accounts, providing real-time insights into post performance.

---

💼 Team Members  

👨‍💻 Shreya Chadha  
👨‍💻 Ashwani Jha  
👨‍💻 Tanishk Singhal  
👨‍💻 Garv Garg 

---

 🛠️ Tools & Technologies  

- DataStax Astra DB: Scalable, cloud-native database for efficient data storage and querying.  
- Langflow: Workflow creation tool integrated with GPT for AI-driven insights.  
- Javascript: Dynamic frontend for seamless user interaction.
- Large Language Model : Gemini
- Rechart.js : Data visualisation   

---
🔢 Task Breakdown  

 1️⃣ Fetch Engagement Data  
Simulated dataset containing:  
- ❤️ Likes  
- 💬 Comments  
- 💪 Shares 
- Post Types: 🎢 Carousel, 🎥 Reels, 🖼️ Static Images  
- Stored in DataStax Astra DB for secure and scalable operations.  

 2️⃣ Analyze Post Performance  
- Langflow Workflow accepts user input and processes engagement data.  
- Queries Astra DB to calculate average metrics for each post type.  

 3️⃣ Deliver Actionable Insights  
- AI-generated insights powered by GPT, such as:  
  - 🎢 “Carousel posts have 20% higher engagement than static posts.”  
  - 🎥 “Reels generate 2x more comments than other formats.”  

---
🌟 Key Features  

- ⏳ Real-Time Analysis: Instantly analyze social media metrics.  
- 📊 Scalable Storage: Efficient data handling with Astra DB.  
- 🧠 AI-Driven Insights: Tailored recommendations using GPT.  
- 🔄 Workflow Automation: Seamless orchestration via Langflow.  

---

 📚 How It Works  

 Langflow Workflow:  
1. 🧑‍💻 Take Input: Accepts post type and user description.  
2. 🔍 Retrieve Data: Queries Astra DB for engagement metrics.  
3. 🔑 Extract User Data: Filters data by `user_id`.  
4. 🔢 Calculate Averages: Computes average engagement per post type.  
5. 🧠 AI Insights: Generates actionable insights using GPT.  

 DataStax Astra DB Schema:  
| Field      | Description                        |  
|------------|------------------------------------|  
| 👤 `user_id`   | Unique identifier for users.       |  
| 🔖 `post_type` | Type of post (e.g., reel, carousel). |  
| ❤️ `likes`     | Number of likes.                  |  
| 💬 `comments`  | Number of comments.               |  
| 💪 `shares`    | Number of shares.                 |  

---

🚀 Getting Started  

Prerequisites  
- langflow installed(if running the flow locally).  
- Access to DataStax Astra DB.
- Install the flask
- install sql-alchemy, flask-cors
- Gemini API key
    

Steps to Run  

1. Clone the Repository:  
   ```bash  
   git clone [https://github.com/Hack-jack-Electronics/SociaLytics_fin]  
   cd final
2. Run the backend:
     python app.py
    

